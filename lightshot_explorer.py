from bs4 import BeautifulSoup as BS
import requests
import random
import string
from user_agent import generate_user_agent
import shutil
from time import sleep


class LightshotExplorer:

    def generate_link(self):
        # A random lightshot link is generated from 5 lowercase letters and a number
        link = ''.join(random.choice(string.ascii_lowercase) for s in range(5)) + str(random.randint(0,10))
        # Shuffles the above sequence so a static formula isn't always used
        sr = ''.join(random.sample(link, 6))
        return "https://prnt.sc/" + sr

    def download_img(self, link):
        # Identifies the script as a user
        headers = {"user-agent": generate_user_agent()}

        # Accesses and parses the html for the random link
        html = requests.get(link, headers=headers)
        soup = BS(html.text, 'html.parser')

        # Filters only img results on the webpage from the requests result
        image_html = soup.find("img", class_="screenshot-image")
        if image_html:
            img_url = image_html.get("src")
            file_path = img_url.split("/")[-1]

            # Skips the "SCREENSHOT REMOVED" picture and marks as dead link
            if file_path == "0_173a7b_211be8ff.png":
                return 1
            if "http" not in img_url:
                img_url = "http:" + img_url

            r = requests.get(img_url, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                # Saves image to the results folder
                with open(file_path, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                shutil.move(str(file_path), "results")
            else:
                print("No image found at " + link)


def main():
    downloads = input("How many attempts? ")
    deadlinks = 0
    for i in range(int(downloads)):
        explorer = LightshotExplorer()
        link = explorer.generate_link()
        dl = explorer.download_img(link)
        if dl == 1:
            deadlinks += 1
        # Slight delay to prevent lightshot blacklisting
        sleep(.5)
    print("DONE | " + str(int(downloads)-dl) + " images downloaded with " + str(deadlinks) + " dead links.")

main()
