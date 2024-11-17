def text_file_merger(fileURL1, fileURL2, mergedfile):
    # Open the merged file for writing
    with open(mergedfile, 'w') as merged:
        # Read from the first file and write its contents to the merged file
        with open(fileURL1, 'r') as file1:
            for line in file1:
                merged.write(line)
                print(line.strip())  # Display the line without extra spaces
        
        # Read from the second file and append its contents to the merged file
        with open(fileURL2, 'r') as file2:
            for line in file2:
                merged.write(line)
                print(line.strip())  # Display the line without extra spaces

# Example usage
text_file_merger('/home/aryan/pyt/filemerger/file1.txt', '/home/aryan/pyt/filemerger/file2.txt', '/home/aryan/pyt/filemerger/file3.txt')
