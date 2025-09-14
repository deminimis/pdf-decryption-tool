import pikepdf
import os
import sys

def get_unique_filename(path):
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(f"{base}({counter}){ext}"):
        counter += 1
    return f"{base}({counter}){ext}"

def decrypt_pdf(input_file, password):
    if not os.path.exists(input_file):
        print(f"[-] Error: The file '{input_file}' was not found.")
        return

    try:
        pdf = pikepdf.open(input_file, password=password, allow_overwriting_input=True)
        
        if not pdf.is_encrypted:
            print("[-] Info: This PDF is not encrypted. No action needed.")
            pdf.close()
            return

        base, ext = os.path.splitext(input_file)
        output_file = get_unique_filename(f"{base}_decrypted{ext}")
        
        pdf.save(output_file)
        pdf.close()
        print(f"[+] Success! Decrypted PDF saved as: {output_file}")

    except pikepdf.PasswordError:
        print("[-] Wrong password! Please check and try again.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("=== PDF Decryption Tool ===")
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1].strip().strip('"')
    else:
        input_file = input("Enter the path to the encrypted PDF: ").strip().strip('"')
    
    password = input("Enter the PDF password: ").strip()
    decrypt_pdf(input_file, password)
