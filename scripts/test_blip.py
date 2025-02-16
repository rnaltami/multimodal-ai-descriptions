import os
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Folder where images are stored
image_folder = "images"

def list_images():
    """Lists available image files in the images folder."""
    abs_path = os.path.abspath(image_folder)
    print(f"\n🔍 Looking for images in: {abs_path}")

    if not os.path.exists(image_folder):
        print("  ❌ No image folder found.")
        return

    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    if images:
        print("\n🖼️ Available Images:")
        for img in images:
            print(f"  - {img}")
    else:
        print("  ❌ No image files found in the folder.")
    print("\n")

while True:
    # List available images before asking
    list_images()
    
    # Ask for image input
    image_path = input("Enter the image filename (or type 'exit' to quit): ").strip()
    
    if image_path.lower() == "exit":
        print("\n👋 Exiting program. Goodbye!")
        break  # Exit the loop

    full_image_path = os.path.join(image_folder, image_path)

    try:
        # Load the selected image
        image = Image.open(full_image_path)

        # Process the image and generate a caption
        inputs = processor(image, return_tensors="pt")
        output = model.generate(**inputs)

        # Decode the generated caption
        caption = processor.decode(output[0], skip_special_tokens=True)
        print(f"\n📝 Generated Caption: {caption}\n")

    except FileNotFoundError:
        print("\n❌ Error: File not found. Make sure the image is in the 'images/' folder.")
    except Exception as e:
        print(f"\n❌ Error loading image: {e}")
