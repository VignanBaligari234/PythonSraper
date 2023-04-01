from newscraper import get_similar_image_urls 
from newscraper import image_url

def get_urls():
    urls = get_similar_image_urls(image_url)
    if urls:
        # do something with urls
        print(urls)
        return urls
    else:
        print("Error: no URLs found")
        return None
