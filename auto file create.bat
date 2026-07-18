@echo off
:: Create the main project directory
mkdir "CodeAlpha_IrisFlowerClassification"
cd "CodeAlpha_IrisFlowerClassification"

:: Create the dataset folder
mkdir "dataset"

:: Create the empty files
type nul > "notebook.ipynb"
type nul > "iris.py"
type nul > "README.md"
type nul > "requirements.txt"

echo Project structure created successfully!
pause