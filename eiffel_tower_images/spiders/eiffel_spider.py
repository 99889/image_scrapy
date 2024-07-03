import scrapy
from scrapy.pipelines.images import ImagesPipeline

class EiffelSpider(scrapy.Spider):
    name = 'eiffel'
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        # Extracting the specific image URL from the srcset attribute
        image_url = response.css('a.mw-file-description img::attr(srcset)').get()
        
        if image_url:
            # Extract the highest resolution URL
            image_url = image_url.split(', ')[-1].split(' ')[0]
            # Construct the full URL
            full_image_url = response.urljoin(image_url)
            
            yield {
                'image_urls': [full_image_url]
            }

# Custom ImagesPipeline to save images in a specific folder
class CustomImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        return 'eiffel_tower_image.jpg'

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
