import json
import requests


class Imgdownload:

    def __init__(self, json_file):
        self.json_file = json_file
        self.image_list = []

    def read_json_file(self):

        with open(self.json_file, "r") as json_file:

            json_file = json.load(json_file)

            for url in json_file.values():
                if url.endswith(".png") or url.endswith(".jpg"):
                    self.image_list.append(url)

        return self.image_list

    def download_png(self, img_name):
        
        for url in self.image_list:
            
            if url.endswith(".png"):
                response = requests.get(url)
            
                with open(f"{img_name}.png", "wb") as img:
                    img.write(response.content)
                
    def download_jpg(self, img_name):
        
        for url in self.image_list:
            
            if url.endswith(".jpg"):
                response = requests.get(url)
            
                with open(f"{img_name}.jpg", "wb") as img:
                    img.write(response.content)


picture = Imgdownload("image.json")
print(picture.read_json_file())
picture.download_png(img_name="png_image")
picture.download_jpg(img_name="jpg_image")