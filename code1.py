import csv
import sys
import os
import dotenv
dotenv.load_dotenv()


# Reading CSV file
file=os.getenv("filename")
print ("file name: ", file)
with open(file, 'r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Get headers

    # Buffer output and write once instead of calling print() per row
    sys.stdout.write(''.join(f'{row}\n' for row in reader))
