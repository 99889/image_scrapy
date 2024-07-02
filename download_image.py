import json
import requests

# Load JSON data
with open('eiffel_images.json', 'r') as f:
    data = json.load(f)

# Extract the image URL
if data:
    image_url = data[0]['image_url']  # Adjust this if you have multiple images

    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open('eiffel_tower_image.jpg', 'wb') as f:
            f.write(response.content)
        print('Image downloaded successfully!')
    else:
        print(f'Failed to download image. Status code: {response.status_code}')
else:
    print('No image URLs found in the JSON file.')
