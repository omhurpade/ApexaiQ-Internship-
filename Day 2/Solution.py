import pandas as pd
import numpy as np
import re
import time
from concurrent.futures import ThreadPoolExecutor


class DataProcessor:

    def read_file(self, file):
        try:
            if file.endswith(".csv"):
                return pd.read_csv(file)

            if file.endswith(".log"):
                data = []
                with open(file) as f:
                    for line in f:
                        m = re.search(r"(\w+)=(\d+)", line)
                        if m:
                            data.append([m.group(1), int(m.group(2))])

                return pd.DataFrame(data, columns=["name", "value"])

        except Exception as e:
            print("Error:", e)

        return pd.DataFrame()

    def process(self, file):
        df = self.read_file(file)

        if df.empty:
            return 0

        df = df.dropna().drop_duplicates()

        numbers = df.select_dtypes(include=np.number)

        print(file, "Records:", len(df))

        if not numbers.empty:
            print("Average:", numbers.mean().mean())

        return len(df)


files = ["data1.csv", "data2.csv", "server.log"]

# Sequential
start = time.time()

for file in files:
    DataProcessor().process(file)

seq_time = time.time() - start


# Concurrent
start = time.time()

with ThreadPoolExecutor() as executor:
    results = list(executor.map(DataProcessor().process, files))

con_time = time.time() - start


print("\n--- Benchmark ---")
print("Sequential:", round(seq_time, 4), "seconds")
print("Concurrent:", round(con_time, 4), "seconds")
