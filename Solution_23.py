import os
import re
import time
import logging
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.ERROR)


class DataProcessor:

    def __init__(self):
        self.processed = 0
        self.failed = 0
        self.skipped = 0
        self.errors = []

    # Collection
    def read_csv(self, file):
        try:
            return pd.read_csv(file)
        except Exception as e:
            self.failed += 1
            self.errors.append(str(e))
            return pd.DataFrame()

    # Regex-based log processing
    def read_log(self, file):
        data = []

        try:
            with open(file, "r") as f:
                for line in f:
                    match = re.search(r"(\w+)=(\d+)", line)

                    if match:
                        data.append({
                            "name": match.group(1),
                            "value": int(match.group(2))
                        })
                    else:
                        self.skipped += 1

            return pd.DataFrame(data)

        except Exception as e:
            self.failed += 1
            self.errors.append(str(e))
            return pd.DataFrame()

    # Validation + normalization
    def clean(self, df):
        if df.empty:
            return df

        df = df.dropna()
        df = df.drop_duplicates()

        self.processed += len(df)

        return df

    # Analytics
    def analyze(self, df):
        if df.empty:
            return {}

        numbers = df.select_dtypes(include=np.number)

        return {
            "records": len(df),
            "average": numbers.mean().mean() if not numbers.empty else 0,
            "maximum": numbers.max().max() if not numbers.empty else 0,
            "minimum": numbers.min().min() if not numbers.empty else 0
        }

    # Sequential processing
    def sequential(self, files):
        start = time.time()

        results = []

        for file in files:
            if file.endswith(".csv"):
                df = self.read_csv(file)
            elif file.endswith(".log"):
                df = self.read_log(file)
            else:
                self.skipped += 1
                continue

            df = self.clean(df)
            results.append(self.analyze(df))

        return results, time.time() - start

    # Concurrent processing
    def concurrent(self, files):
        start = time.time()

        with ThreadPoolExecutor() as executor:
            results = list(
                executor.map(self.process_file, files)
            )

        return results, time.time() - start

    def process_file(self, file):
        if file.endswith(".csv"):
            df = self.read_csv(file)
        elif file.endswith(".log"):
            df = self.read_log(file)
        else:
            self.skipped += 1
            return {}

        df = self.clean(df)
        return self.analyze(df)

    # Final report
    def report(self, seq_time, con_time):
        print("\n--- Processing Report ---")
        print("Records processed :", self.processed)
        print("Failed records    :", self.failed)
        print("Skipped records   :", self.skipped)
        print("Sequential time   :", round(seq_time, 4), "seconds")
        print("Concurrent time   :", round(con_time, 4), "seconds")

        if con_time:
            speed = ((seq_time - con_time) / seq_time) * 100
            print("Speed improvement :", round(speed, 2), "%")

        print("Errors            :", len(self.errors))


# ---------------- MAIN PROGRAM ----------------

processor = DataProcessor()

files = [
    "data1.csv",
    "data2.csv",
    "server.log"
]

seq_results, seq_time = processor.sequential(files)

con_results, con_time = processor.concurrent(files)

processor.report(seq_time, con_time)
