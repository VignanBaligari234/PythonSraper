from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import requests

# Set up the Google Cloud Vision API client
client = vision_v1.ImageAnnotatorClient.from_service_account_file('/Users/jovi/Documents/secret key gcp/secret-code-382403-1b71500e0c96.json')

# Function to get similar image URLs
def get_similar_image_urls(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    image_content = response.content

    # Create a Vision API image object from the downloaded image
    image = types.Image(content=image_content)

    # Call the Vision API to detect similar images
    response = client.web_detection(image=image)
    annotations = response.web_detection

    # Extract the URLs of web pages that contain similar images
    similar_images = annotations.visually_similar_images
    urls = [similar_image.url for similar_image in similar_images]

    return urls

# Example usage
image_url = 'https://ireland.apollo.olxcdn.com/v1/files/tfesmmmhxwjr3-PL/image;s=2000x2000'
similar_image_urls = get_similar_image_urls(image_url)
print(similar_image_urls)
