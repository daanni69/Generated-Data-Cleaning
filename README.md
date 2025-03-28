Generated-Data-Cleaning
This project demonstrates how to clean and preprocess an employee dataset using Python and pandas. The script performs essential data cleaning tasks to ensure the dataset is ready for analysis or further processing. It handles missing values, fixes formatting issues, replaces invalid values, standardizes date formats, and removes duplicate rows.

Features
The script includes the following data cleaning steps:
1. Handle Missing Values:
   - Fill missing `Age` values with the median age.
   - Fill missing `Salary` values with the median salary.
2. Fix Formatting Issues:
   - Remove extra spaces from the `Name` column.
   - Standardize the `Department` column to lowercase.
3. Fix Invalid Values:
   - Replace negative `Salary` values with `0`.
4. Standardize Date Format:
   - Convert the `Joining_Date` column to the `YYYY-MM-DD` format.
   - Identify and handle invalid dates.
5. Remove Duplicate Rows:
   - Check for and remove duplicate rows in the dataset.
