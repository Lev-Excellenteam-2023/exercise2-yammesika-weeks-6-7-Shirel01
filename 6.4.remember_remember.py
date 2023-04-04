from PIL import Image

def decrypt_message(path):
    # Load the image and convert to grayscale. The objective is to receive the picture in black and white
    img = Image.open(path).convert('L')

    # Get the dimensions of the image
    width, height = img.size
    # 54*255
    # Iterate over each column of the image
    black_pixel_positions = []
    for x in range(width):
        # Find the first black pixel in the column
        for y in range(height):
            pixel_color = img.getpixel((x, y))  # Returns the pixel value at a given position.
            if pixel_color == 0:
                # Record the position of the black pixel
                black_pixel_positions.append((x, y))
                break

    # Use the black pixel positions to reconstruct the message
    message = ''
    for x, y in black_pixel_positions:
        # Determine the character based on the y coordinate of the black pixel
        char_code = y % 256
        message += chr(char_code)

    return (message)


def main():
    print(decrypt_message('code.png'))

if __name__ == "__main__":
    main()
