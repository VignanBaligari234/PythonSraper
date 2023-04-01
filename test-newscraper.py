import unittest
from unittest.mock import patch, MagicMock

from newscraper import get_similar_image_urls


class TestImageSimilarity(unittest.TestCase):
    def setUp(self):
        self.test_image_url = 'https://ireland.apollo.olxcdn.com/v1/files/tfesmmmhxwjr3-PL/image;s=2000x2000'

    @patch('app.client')
    @patch('app.requests.get')
    def test_get_similar_image_urls(self, mock_get, mock_client):
        # Set up mock response from requests.get()
        mock_response = MagicMock()
        mock_response.content = b'mock_response_content'
        mock_get.return_value = mock_response

        # Set up mock response from client.web_detection()
        mock_annotations = MagicMock()
        mock_similar_image_1 = MagicMock()
        mock_similar_image_2 = MagicMock()
        mock_similar_image_1.url = 'https://i.pinimg.com/736x/77/48/04/774804634b4c52cf47e8946b04012f26.jpg'
        mock_similar_image_2.url = 'https://imagedelivery.net/ePR8PyKf84wPHx7_RYmEag/1922967e-e68b-485e-2dfe-587b7fa21f00/86'
        mock_annotations.visually_similar_images = [mock_similar_image_1, mock_similar_image_2]
        mock_response = MagicMock()
        mock_response.web_detection = mock_annotations
        mock_client.return_value = mock_response

        # Call the function and check output
        similar_image_urls = get_similar_image_urls(self.test_image_url)
        self.assertEqual(similar_image_urls, ['https://i.pinimg.com/736x/77/48/04/774804634b4c52cf47e8946b04012f26.jpg', 'https://imagedelivery.net/ePR8PyKf84wPHx7_RYmEag/1922967e-e68b-485e-2dfe-587b7fa21f00/86'])
