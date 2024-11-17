# Text File Merger

## Overview

The `text_file_merger` function is a simple Python utility to merge the contents of two text files into a third file. It reads the lines from the first two files and combines them sequentially into the output file.

---

## How It Works

1. Opens the first file (`fileURL1`) in read mode and writes its contents to the output file (`mergedfile`).
2. Opens the second file (`fileURL2`) in read mode and appends its contents to the same output file.
3. Prints the content of both files to the console while processing.

---

## Function Signature

```python
def text_file_merger(fileURL1, fileURL2, mergedfile):
Parameters:
fileURL1: (str) - The file path of the first input text file.
fileURL2: (str) - The file path of the second input text file.
mergedfile: (str) - The file path where the merged content will be saved.
Example Usage
python
Copy code
# Merge the contents of file1.txt and file2.txt into file3.txt
text_file_merger('/home/aryan/pyt/filemerger/file1.txt', 
                 '/home/aryan/pyt/filemerger/file2.txt', 
                 '/home/aryan/pyt/filemerger/file3.txt')
Output
If the contents of the input files are as follows:

file1.txt:

kotlin
Copy code
Hello, this is file 1.
It has multiple lines.
file2.txt:

csharp
Copy code
This is file 2.
It also has multiple lines.
The resulting file3.txt will contain:

kotlin
Copy code
Hello, this is file 1.
It has multiple lines.
This is file 2.
It also has multiple lines.
Notes
The output file (mergedfile) will be overwritten if it already exists.
Ensure all file paths are correct and accessible.
The function does not include error handling for missing or inaccessible files.
