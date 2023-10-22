import zipfile

archive_file_path = "digits.zip"

digit_counts = {str(i): 0 for i in range(10)}

ascii_to_digit = {str(i): i for i in range(10)}

with zipfile.ZipFile(archive_file_path, 'r') as archive:
    for file_name in archive.namelist():
        with archive.open(file_name) as file:
            content = file.read()
            
            for byte in content:
                byte_str = chr(byte) 
                if byte_str in ascii_to_digit:
                    digit = ascii_to_digit[byte_str]
                    digit_counts[str(digit)] += 1

for digit, count in digit_counts.items():
    print(f'Digit {digit}: {count} occurrences')
