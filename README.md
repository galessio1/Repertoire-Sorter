# Repertoire Sorter

This Python program reads data from a CSV file containing information about authors and their pieces, sorts them alphabetically by surname, and writes the sorted data to a text file.

# Usage
Input File: Provide the input CSV file containing the author information. 
The CSV file should have columns named "Name", "Surname", and "Piece".

Output File: Specify the name of the output text file where the sorted data will be written.

# Command-line Usage:
```python repertoire_sorter.py input_file.csv output_file.txt```

Example:
```python repertoire_sorter.py authors.csv sorted_authors.txt```

# Functionality
Reading Input: The program reads data from the provided CSV file.

Sorting: It sorts the data alphabetically by surname.

Output: The sorted data is then written to the specified output text file.

# Requirements
Python 3.x
Libraries: sys, csv