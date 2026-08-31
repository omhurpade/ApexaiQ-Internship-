import pandas as pd
import numpy as np
import re
import time
from concurrent.futures import ThreadPoolExecutor


class DataProcessor:

    def read_file(self, file):
        try:
            if file == "data1.csv":
                return pd.DataFrame({
                    "id": [1, 2, 3, 3],
                    "sales": [100, 200, 300, 300]
                })

            if file == "data2.csv":
                return pd.DataFrame({
                    "id": [4, 5, 6],
                    "sales": [400, 500, 600]
                })

            if file == "server.log":
                text = "status=200\nstatus=500\nlatency=120"
                data = re.findall(r"(\w+)=(\d+)", text)
                return pd.DataFrame(data, columns=["name", "value"])

        except Exception as e:
            print("Error:", e)

        return pd.DataFrame()

    def process(self, file):
        df = self.read_file(file)

        if df.empty:
            return 0

        # Clean data
        df = df.dropna().drop_duplicates()

        # Select numeric columns
        numbers = df.select_dtypes(include=[np.number])

        print(f"[{file}] Cleaned Records: {len(df)}")

        if not numbers.empty:
            avg = numbers.values.mean()
            print(f"[{file}] Numeric Average: {avg:.2f}")

        return len(df)


if __name__ == "__main__":

    files = ["data1.csv", "data2.csv", "server.log"]
    processor = DataProcessor()

    # Sequential
    print("--- Running Sequential ---")
    start = time.time()

    for file in files:
        processor.process(file)

    seq_time = time.time() - start

    # Concurrent
    print("\n--- Running Concurrent ---")
    start = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(processor.process, files))

    con_time = time.time() - start

    # Benchmark
    print("\n================ Benchmark Summary ================")
    print(f"Sequential Time : {seq_time:.4f} seconds")
    print(f"Concurrent Time : {con_time:.4f} seconds")
    print("===================================================")
