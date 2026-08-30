import pandas as pd
import numpy as np
import re
import time
from concurrent.futures import ThreadPoolExecutor

# Sample test data create kar rahe hain taaki code turant run ho sake
pd.DataFrame({'id': [1, 2, 3, 3], 'sales': [100, 200, 300, 300]}).to_csv('data1.csv', index=False)
pd.DataFrame({'id': [4, 5, 6], 'sales': [400, 500, 600]}).to_csv('data2.csv', index=False)
with open('server.log', 'w') as f:
    f.write("status=200\nstatus=500\nlatency=120\n")


class DataProcessor:

    def read_file(self, file):
        try:
            if file.endswith(".csv"):
                return pd.read_csv(file)

            if file.endswith(".log"):
                data = []
                with open(file, 'r') as f:
                    for line in f:
                        m = re.search(r"(\w+)=(\d+)", line)
                        if m:
                            data.append([m.group(1), int(m.group(2))])

                return pd.DataFrame(data, columns=["name", "value"])

        except Exception as e:
            print("Error reading", file, ":", e)

        return pd.DataFrame()

    def process(self, file):
        df = self.read_file(file)

        if df.empty:
            return 0

        # Remove missing and duplicate values
        df = df.dropna().drop_duplicates()

        # Select only numeric columns
        numbers = df.select_dtypes(include=[np.number])

        print(f"[{file}] Cleaned Records: {len(df)}")

        if not numbers.empty:
            avg_val = numbers.values.mean()
            print(f"[{file}] Numeric Average: {round(avg_val, 2)}")

        return len(df)


if __name__ == "__main__":
    files = ["data1.csv", "data2.csv", "server.log"]
    processor = DataProcessor()

    # 1. Sequential Execution
    print("--- Running Sequential ---")
    start = time.time()
    for file in files:
        processor.process(file)
    seq_time = time.time() - start

    # 2. Concurrent Execution
    print("\n--- Running Concurrent ---")
    start = time.time()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(processor.process, files))
    con_time = time.time() - start

    # Benchmark Summary
    print("\n================ Benchmark Summary ================")
    print(f"Sequential Time : {seq_time:.4f} seconds")
    print(f"Concurrent Time : {con_time:.4f} seconds")
    print("===================================================")
