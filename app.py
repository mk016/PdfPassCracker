import itertools
from PyPDF2 import PdfReader

# Function to attempt to open the PDF with the given password
def try_password(pdf_reader, password):
    try:
        if pdf_reader.decrypt(password) == 1:
            print(f"Password found: {password}")
            return True
    except Exception as e:
        print(f"Error with password {password}: {str(e)}")
    return False

# Brute-force attack
def brute_force_pdf(pdf_path):
    # Define character and number sets
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    # Load the PDF
    pdf_reader = PdfReader(open(pdf_path, "rb"))

    # Generate all possible 8-character passwords
    for combo in itertools.product(characters, repeat=4):
        for num_combo in itertools.product(numbers, repeat=4):
            # Combine characters and numbers to form a password
            password = ''.join(combo) + ''.join(num_combo)
            print(f"Trying password: {password}")
            if try_password(pdf_reader, password):
                return

    print("Password not found.")

# Usage example:
pdf_path = 'EAadhaar_0516146870913520240506122925_3008202423400.pdf'
brute_force_pdf(pdf_path)
