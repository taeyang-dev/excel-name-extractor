# excel-name-extractor
Extract names from Excel using Python

## 💡 What is this?
This is a simple automation tool that extracts the "Name" column from an Excel spreadsheet and saves it as a plain text file.

## 🔧 How it works
1. Open the Excel file named `sample.xlsx`
2. Read the "이름" (Name) column
3. Save the names into a new file called `output_names.txt`

## 📁 Files
- `extract_names.py` – Python script to run the automation
- `sample.xlsx` – Example Excel file
- `output_names.txt` – Output file after running the script

## ▶️ How to run
1. Make sure Python and `pandas` are installed.
2. Place `sample.xlsx` in the same folder.
3. Run the script:

```bash
python extract_names.py

## 📄 Example Output
이태양
김유진
박지훈
