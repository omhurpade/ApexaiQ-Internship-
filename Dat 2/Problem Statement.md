# Problem 23 — Mini Enterprise Data Processing Platform

## Problem Statement

Build a mini enterprise data-processing platform that receives data from multiple sources such as CSV files, log files, API responses, and web pages.

The platform should contain the following stages:

- Data Collection
- Data Validation
- Data Normalization
- Data Processing
- Data Analytics
- Data Reporting

The platform must support:

- CSV and log file processing
- API data collection
- Selenium-based web scraping
- Regex-based data extraction
- Pandas and NumPy processing
- Object-oriented programming
- Exception handling
- Concurrent or parallel processing

The final report should include:

- Records processed
- Failed records
- Skipped records
- Processing time
- Data-quality issues
- Errors
- Summary statistics

The sequential implementation should also be compared with a concurrent implementation using measured benchmark results.

---

## Solution

The solution uses an object-oriented data processing pipeline.

### Processing Flow

```text
Data Sources
     ↓
Collection
     ↓
Validation
     ↓
Normalization
     ↓
Processing
     ↓
Analytics
     ↓
Reporting
```

### Technologies Used

- Python
- Pandas
- NumPy
- Regular Expressions
- Selenium
- ThreadPoolExecutor
- CSV
- Logging

### Features

1. Reads data from CSV files.
2. Reads and extracts information from log files using Regex.
3. Demonstrates API data collection.
4. Uses Selenium for web scraping.
5. Validates missing and invalid records.
6. Normalizes data using Pandas.
7. Performs basic analytics using Pandas and NumPy.
8. Handles errors using exception handling.
9. Processes files sequentially and concurrently.
10. Generates a processing report.
11. Measures and compares execution time.

---

## Benchmark

The program measures the execution time of:

- Sequential processing
- Concurrent processing

The results are displayed at the end of the program.

```text
Sequential Time : X.XXXX seconds
Concurrent Time : X.XXXX seconds
Speed Improvement : XX.XX%
```

---

## Conclusion

The concurrent implementation can process independent data sources simultaneously. This can reduce overall processing time compared with sequential execution, especially when the workload contains multiple independent files or I/O operations.

📄 **Python Implementation:**  
[View Problem_23.py](Solution.py)
