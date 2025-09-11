import pikepdf
import os

def decrypt_pdf(input_file, output_file, password):
    try:
        # Open the PDF with the password
        pdf = pikepdf.open(input_file, password=password)

        # Save a new copy without password or restrictions
        pdf.save(output_file)
        pdf.close()

        print(f"[+] Success! Decrypted PDF saved as: {output_file}")

    except pikepdf._qpdf.PasswordError:
        print("[-] Wrong password! Please check and try again.")
    except Exception as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    print("=== PDF Decryption Tool ===")

    # Get input from user
    input_file = input("Enter the path to the encrypted PDF: ").strip()
    password = input("Enter the PDF password: ").strip()

    # Default output name (same name + '_decrypted.pdf')
    base, ext = os.path.splitext(input_file)
    output_file = base + "_decrypted.pdf"

    decrypt_pdf(input_file, output_file, password)
