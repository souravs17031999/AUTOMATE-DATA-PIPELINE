from bs4 import BeautifulSoup
import requests
import json
import os
import urllib.request as ulib
from urllib.request import Request, urlopen
from PIL import Image
from zipfile import ZipFile
import shutil
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
from tqdm import tqdm

# IMPORTANT note----------------------------------------------------------
# STEPS FOR CREATING AND USING GOOGLE CUSTOM SEARCH API Has been written in
# google_api.txt
#--------------------------------------------------------------------------

# Main class for the methods defined for the complete software

class automate_images_download:

    # function for downloading images
    def download_images(self, dir_path, query, KEY, CX):

        # Use the below code for browser automation by editing the browser and driver accordingly
        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(executable_path='C:/Users/DELL/Desktop/chromedriver.exe')
        # driver.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyDSlcYciCo0pXE3v3QB1lo9Xh3bb4hS7c0&cx=004504403258812559156:su54o48corh&q=bike')
        # content = driver.find_elements_by_tag_name('pre')
        # for image in content:
        #     print(image.get_attribute('src'))

        # Urls is a list of all the images scraped from google images in real time
        if not os.path.isdir(dir_path):
            print("Image scraping using Google Custom Image Search Engine API....")
            print("Making 10 requests at a time , total of 100 requests in one Go !")
            urls = []
            print("FETCHING...")
            for i in tqdm(range(0, 100, 10)):
                try:
                    source = requests.get(f'https://www.googleapis.com/customsearch/v1?key={KEY}&cx={CX}&q={query}&searchType=image&num=10&start={i}').text
                    content = json.loads(source)
                    total_length = len(content['items'])
                except Exception as error:
                    print("API ERROR , EITHER CREDENTIALS FAILED OR REQUEST LIMIT REACHED !")
                    return
                for i in range(0, total_length):
                    try:
                        urls.append(content['items'][i]['link'])
                    except Exception as e:
                        pass
                print('\r', end="")

            print()
            # links are referencing the same urls , just giving convinient name to avoid confusion
            links = urls
            os.mkdir(dir_path)
            print(f"Creating {dir_path} to download images there directly....")
            print(f"Downloading images...")
            for link in tqdm(range(0, 100)):
                try:
                    full_path = dir_path + f"/image{link}" + ".png"
                    ulib.urlretrieve(links[link], full_path)
                    #print(f"downloaded image{link}")
                except Exception as HTTPError:
                    try:
                        req = Request(links[link], headers={'User-Agent': 'Mozilla/5.0'})
                        webpage = urlopen(req).read()
                        with open(full_path, 'wb') as f:
                            f.write(webpage)
                        # print(f"downloaded image{link}")
                    except Exception as e:
                        pass
                print('\r', end="")
            print(f"Total {len(links)} Images downloaded")
            print(f"Downloaded images can be found at {dir_path}")
            return 200
        else:
            print("Given directory already detected")
            if not len(os.listdir(dir_path)):
                print("directory is empty !")
                option = input("would you like to start download again ? [Y/N]")
                if option.lower() == 'y':
                    shutil.rmtree(dir_path)
                    self.download_images(dir_path, query)
                else:
                    print("Skipping downloading of images !")
            else:
                print("Skipping downloading of images !, Delete the old directory first !")

    # function for resizing images to 50%
    def resize_images(self, dir_path):
        # resizing every image by 50% using pillow library
        print("Starting Resizing images one by one....")
        for i in tqdm(range(0, 100)):
            try:
                full_path_open = dir_path + f"/image{i}" + ".png"
                image = Image.open(full_path_open)
                width, height = image.size[0] // 2, image.size[1] // 2
                image.thumbnail((width, height))
                image.save(full_path_open)
            except Exception as e:
                pass

            print('\r', end="")
        print("All images resized succesfully !")

    # function for converting images to grayscale
    def convert_images(self, dir_path):
        print("Starting conversion of images to GreyScale one by one....")
        for i in tqdm(range(0, 100)):
            try:
                full_path_open = dir_path + f"/image{i}" + ".png"
                image = Image.open(full_path_open)
                image = image.convert(mode='L')
                image.save(full_path_open)
            except Exception as e:
                pass
            print('\r', end="")
        print("All images converted to GreyScale succesfully !")

    # function for zipping the files one by one
    def zip_images(self, dir_path):
        print("Zipping downloaded files...")
        file_paths = []
        for root, directories, files in os.walk(dir_path):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        with ZipFile(dir_path+'/images.zip', 'w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file)
        print("Complete files zipped succesfully !")

    # function for sending mails as and when required , may it be one or batches
    def sent_mail(self, zipped_path, subject, body, sender_email, receiver_email, password):
        print("Sending EMAIL...")
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = zipped_path  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)
        sent_filename = 'images.zip'
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {sent_filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        print("Created SSL server for SMTP transfer using GMAIL")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            print("Login success !")
            print(f"Sender email : {sender_email}")
            print(f"Receiver email : {receiver_email}")
            print(f"Subject : {subject}")
            print("Sending Mail....")
            server.sendmail(sender_email, receiver_email, text)
            print("Mail sent succesfully !")

    # main controlling function of the software
    def main_run_download(self, dir_path, query, KEY, CX):
        self.download_images(dir_path, query, KEY, CX)

    def main_run_mail(self, query, dir_path, sender_email, receiver_email, password):
        self.resize_images(dir_path)
        self.convert_images(dir_path)
        self.zip_images(dir_path)
        zipped_path = dir_path+'/images.zip'
        subject = "This is mail from sourav kumar"
        body = f"Following is the attachment which you have requested on your query : {query}"
        self.sent_mail(zipped_path, subject, body, sender_email, receiver_email, password)


# if __name__ == '__main__':
    # print("WELCOME TO AUTOMATING GOOGLE IMAGES DOWNLOAD")
    # parser = argparse.ArgumentParser(description='Automating Google images download', epilog='Happy automation :)')
    # parser.add_argument('dir_path', type=str, help='Output working directory')
    # parser.add_argument('query', type=str, help='Query string to search for')
    # parser.add_argument('KEY', type=str, help='API KEY')
    # parser.add_argument('CX', type=str, help='SEARCH ENGINE ID')
    # parser.add_argument('sender_email', type=str, help='sender_email')
    # parser.add_argument('receiver_email', type=str, help='receiver_email')
    # parser.add_argument('password', type=str, help='password for email sending')
    # args = parser.parse_args()
    # dir_path = args.dir_path+'/sourav_image'
    # query = args.query
    # a_i_d = automate_images_download()
    # a_i_d.main_run(dir_path, query, args.KEY, args.CX, args.sender_email, args.receiver_email, args.password)
    # # dir_path = "C:/Users/DELL/Desktop/sourav"
    # # query = 'bike'
    # # if len(dir_path) > 0:
    # #     automate = automate_images_download()
    # #     automate.main_run(dir_path, query)
    # # else:
    # #     print("Wrong file name !")
