from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixel_data = np.array(image)
    
    # Encrypt the image by XORing each pixel with the key
    encrypted_data = pixel_data ^ key
    
    # Convert back to an image
    encrypted_image = Image.fromarray(encrypted_data)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # Decryption is the same as encryption due to XOR properties
    encrypt_image(input_path, output_path, key)
    print(f"Image decrypted and saved to {output_path}")

def main():
    while True:
        choice = input("Enter E to encrypt or D to decrypt (Enter 'Q' to quit)")
        if choice == 'Q':
            print("Exiting the program.")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue
        
        input_path = input("Enter the path to the input image: ")
        output_path = input("Enter the path to save the output image: ")
        try:
            key = int(input("Enter the encryption key (integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue
        
        if choice == 'E':
            encrypt_image(input_path, output_path, key)
        elif choice == 'D':
            decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()


