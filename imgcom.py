from PIL import Image
from tkinter import Tk, filedialog
import os

def resize_image(image_path, output_path, target_size):
    with Image.open(image_path) as image:
        # Calculate the target width and height based on the target size
        width, height = image.size
        current_size = os.path.getsize(image_path) / 1024  # File size in KB
        ratio = (target_size / current_size) ** 0.5
        new_width = int(width * ratio)
        new_height = int(height * ratio)

        # Resize the image using the new dimensions
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Save the resized image to the output path
        resized_image.save(output_path, optimize=True, quality=95)

        # Get the new file size
        new_file_size = os.path.getsize(output_path) / 1024  # File size in KB

        return new_file_size


# Open file selection dialog to choose the input image file
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select JPEG Image File", filetypes=[("JPEG Files", "*.jpg;*.jpeg")])

# Check if a file was selected
if image_path:
    # Open file selection dialog to choose the output path
    output_path = filedialog.asksaveasfilename(title="Save Resized Image", defaultextension=".jpg",
                                               filetypes=[("JPEG Files", "*.jpg;*.jpeg")])
    
    if output_path:
        target_size = int(input("Enter the target size in kilobytes: "))

        # Resize the image
        new_size = resize_image(image_path, output_path, target_size)

        print(f"The image has been resized and saved to {output_path}")
        print(f"The new file size is {new_size} KB.")
    else:
        print("No output path selected.")
else:
    print("No file selected.")
