import requests
import json
import threading


class Download:

    def __init__(self, json_file):
        self.json = json_file

    def download_pics(self):

        with open(self.json, "r") as file:
            file = json.load(file)

            for name_url in file:
                for name, url in name_url.items():
                    response = requests.get(url)

                    with open(f"{name}.jpeg", "wb") as pic:
                        pic.write(response.content)

    def download_pics_faster(self):

        thread_list = []
        for i in range(10):
            x = threading.Thread(target=self.download_pics())
            thread_list.append(x)
            x.start()

        for thread in thread_list:
            thread.join()


pic_download = Download("img.json")
pic_download.download_pics_faster()
print("Download completed")
