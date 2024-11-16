from PIL import Image
import numpy as np
import sys

# Load the original image and the mask
image_path = 'output_image.png'  # Replace with your image path
mask_path = 'attack_mask.png'    # Replace with your mask path

def mask_image(image_path, mask_path, name):
    # Open the images and convert them to RGBA
    image = Image.open(image_path).convert("RGBA")
    resized_image = image.resize((500, 380), Image.BILINEAR)
    mask = Image.open(mask_path).convert("RGBA")

    # Convert images to numpy arrays
    image_array = np.array(resized_image)
    mask_array = np.array(mask)


    # Extract the alpha channel from the mask
    alpha_channel = mask_array[:, :, 3]

    # Set image alpha to 0 where the mask alpha is 0 (fully transparent)
    image_array[:, :, 3] = np.where(alpha_channel == 0, 0, image_array[:, :, 3])

    # Convert the modified array back to an image
    output_image = Image.fromarray(image_array, "RGBA")
    smaller_image  = output_image.resize((250,190), Image.NEAREST)
    # Save the result
    output_image.save(f"{name}_p.png")
    smaller_image.save(f"{name}.png")

def main():
    # Ensure the script has the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <image_path> <mask_path> <output_name>")
        sys.exit(1)

    # Get arguments from the command line
    image_path = sys.argv[1]
    mask_path = sys.argv[2]
    name = sys.argv[3]

    # Call the mask_image function with the provided arguments
    mask_image(image_path, mask_path, name)

if __name__ == "__main__":
    main()