import os
import random
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip
import json
import shutil
from zipfile import ZipFile
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

# IMPORTANT NOTE --------------------------------------------------------
# * AUTHETICATION CLIENT SECRETS FILE IS DOWNLOADED FROM GOOGLE API CONSOLE BY creating new
# credentials for any existing project (if any) , otherwise create new project first.
# * FFMPEG should be downloaded from here : https://ffmpeg.zeranoe.com/builds/
# add its PATH to env variable by copying absolute path where ffmpeg.exe is stored (usually its in /bin)
# Check out this : https://www.youtube.com/watch?v=qjtmgCb8NcE
# * Chrome driver should be downloaded for selenium from : https://chromedriver.chromium.org/downloads
# STEPS FOR CREATING OAUTH CREDENTIALS and using API is written in youtube_api.txt
# -----------------------------------------------------------------------

# Main class for the methods defined for the complete software
class automate_videos_download:

    # function for closing the browser automatically
    def browser_close(self, driver):
        # this handles the case whenever redirects are opened on clicking
        # due to popups or ads, so it closes them automatically
        tabs = len(driver.window_handles)
        if tabs > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        return

    # function for getting directory length
    def get_dir_length(self, full_path):
        return len(os.listdir(full_path))

    # function for downloading videos using web automation through selenium
    def Download_videos(self, mod_path, chrome_driver_path, video_links):
        # creating youtube video links
        video_links = ['youtube.com/watch?v=' + x for x in video_links]
        # instantiating web driver
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--disable-notifications')
        # setting preferences
        prefs = {"profile.default_content_settings.popups": 0,
                "download.default_directory":rf"{mod_path}",
                "directory_upgrade": True}
        options.add_experimental_option('prefs', prefs)

        # initiating driver for chrome
        driver = webdriver.Chrome(chrome_driver_path, options=options)
        driver.get("https://ytmp3.cc/en13/")
        driver.implicitly_wait(random.randint(10, 20))
        print("Downloading Videos....")
        # starting downloading from the above url's created from the
        # website link : https://ytmp3.cc/en13/
        for i in video_links:
            try:
                self.browser_close(driver)
                #print(f"downloading {i}")
                driver.find_element_by_name("video").send_keys(i)
                self.browser_close(driver)
                driver.implicitly_wait(20)
                driver.find_element_by_xpath('//*[@id="submit"]').click()
                self.browser_close(driver)
                driver.implicitly_wait(50)
                driver.find_element_by_xpath('//*[@id="buttons"]/a[1]').click()
                self.browser_close(driver)
                driver.implicitly_wait(20)
                driver.find_element_by_xpath('//*[@id="buttons"]/a[3]').click()
                self.browser_close(driver)
            except Exception as e:
                pass
        driver.close()
        print(f"Newly downloaded and converted audio files can be found at : {mod_path}")

    # function for renaming files for convinience
    def rename_files(self, full_path):
        print("Files are being renamed for convinience...")
        if not os.path.isdir(full_path):
            print("Given directory doesn't exists, There are no downloaded videos directory found !")
            return
        for i, filename in enumerate(os.listdir(full_path)):
            os.rename(full_path + '/' + filename, full_path + '/video' + str(i) + '.mp3')

    # function for trimming audio files
    def trim_audio(self, dir_path):
        full_path = dir_path + '/sourav'
        # check if download original path is present
        if os.path.isdir(full_path):
            full_path_trim = dir_path + '/sourav_new'
            # check whether already files are trimmed
            if not os.path.isdir(full_path_trim):
                print(f"Constructing new directory...")
                os.mkdir(full_path_trim)
                print("Trimming files....")
                # progress bar pretty print -----------------------------
                counter = 0
                for i, filename in enumerate(os.listdir(full_path)):
                    if i % 7 == 0:
                        if i == 49:
                            counter = 20
                        else:
                            counter += 3
                        sys.stdout.write('\r')
                        sys.stdout.write("[%-50s] %d%%" % ('='*i, 5*counter))
                        sys.stdout.flush()
                        sleep(0.25)
                #-------------------------------------------------------
                    input_file = full_path + '/' + filename
                    output_file = full_path_trim + '/video' + str(i) + '.mp3'
                    # using ffmpeg to trim the audio files - trimming first 2 minutes
                    # this command shall only be run on command prompt (terminal)
                    # after setting the PATH for env variable
                    os.system(f'ffmpeg -ss 120 -i {input_file} {output_file} -loglevel quiet')
                print()
                print(f"All audios trimmed succesfully ! Find new audio files at {full_path_trim}")
            else:
                print("Already treamed audio directory exists !, Delete the older directory first and then try again !")
                return
        else:
            print("Given directory doesn't exists !, There are no downloaded videos directory found !")
            return

    # this is a short helper function for zipping files
    # while returning batches of files
    def zip_helper(self, zipped_path, batch, start, end):
        file_paths = []
        for root, directories, files in os.walk(zipped_path):
            for filename in files[start:end + 1]:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        with ZipFile(zipped_path +'/music' + str(batch) +  '.zip', 'w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file)

    # function for zipping the files one by one
    def zip_files(self, dir_path):
        zipped_path = dir_path + '/sourav_new'
        if os.path.isdir(zipped_path):
            print("Zipping file started...")
            batch = 0
            for i in range(0, 50, 7):
                self.zip_helper(zipped_path, batch, i, i + 7)
                batch += 1
            print(f"Complete files zipped succesfully ! Total {batch} batches created !")
            zipped_paths = []
            for filenames in os.listdir(zipped_path):
                if filenames.startswith('music'):
                    zipped_paths.append(zipped_path + '/' + filenames)
            return zipped_paths
        else:
            print("Required directory of trimmed audio files not found !, First trimming shoud be done.")

    # function for sending mails as and when required , may it be one or batches
    def sent_mail(self, zipped_path, subject, body, sender_email, receiver_email, password, batch):

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
        sent_filename = 'music' + str(batch) + '.zip'
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
    def main(self, dir_path, client_secrets_file_path, chrome_driver_path, username, password, query_string, sender_email, receiver_email, email_password):

        full_path = dir_path + '/sourav'
        mod_path = full_path.split('/')
        mod_path = "\\".join(mod_path) + "\\\\"

        # check whether directory is already present, then no need to fire API
        if not os.path.isdir(full_path):
            # the following code describes the firing of YOUTUBE Data V3 API
            # using Google Oauth authorization flow
            # The authorization is automated through web using selenium
            scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

            api_service_name = "youtube"
            api_version = "v3"
            # this file is very important in determing tokens for authorization
            # set it's path correctly
            client_secrets_file = client_secrets_file_path
            # Get credentials and create an API client
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
            driver = webdriver.Chrome(chrome_driver_path)
            # going to authorization url
            # everything below is automated process
            driver.get("https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=744704855386-ov8kf1j3eagfcthepkliprjb4ok4nho4.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.force-ssl&state=AySChscgPs1jYjuald3bRiOiMU1kgC&prompt=consent&access_type=offline")
            try:
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_name("identifier").send_keys(username)
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_name("password").send_keys(password)
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[1]/div[1]/a').click()
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[1]/div[2]/p[2]/a').click()
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_xpath('//*[@id="oauthScopeDialog"]/div[3]/div[1]/span/span').click()
                driver.implicitly_wait(random.randint(10, 20))
                driver.find_element_by_xpath('//*[@id="submit_approve_access"]/span/span').click()
                driver.implicitly_wait(random.randint(10, 20))
                token = driver.find_element_by_class_name('qBHUIf').get_attribute('value')
                pyperclip.copy(token)
            except Exception as e:
                print("AUTHORIZATION ERROR !")
            driver.close()
            # Now here only, we need to press one time CTRL + V to put the authorization token which is already been copied to clipboard
            if pyperclip.is_available():
                credentials = flow.run_console(authorization_prompt_message="", authorization_code_message="Press CTRL+V to paste the token and then Press Enter : ")
                # stdout.write(token)
                youtube = googleapiclient.discovery.build(
                    api_service_name, api_version, credentials=credentials)

                # firing API and fetching the results
                request = youtube.search().list(
                    part="snippet",
                    maxResults = 50,
                    type = 'video',
                    videoDuration = 'short',
                    q=query_string
                )
                response = request.execute()
                # scraping the results and construcing the list of video id's
                video_links = []
                for i in range(0, 50):
                    try:
                        video_id = response['items'][i]['id']['videoId']
                        video_links.append(video_id)
                    except Exception as e:
                        print(f"failed to retrieve video_links{i}")

                os.mkdir(full_path)
                # call download function for downloading these created video id's
                self.Download_videos(mod_path, chrome_driver_path, video_links)
            else:
                print("Could not retrive the links ! Program Exits without Accesing API.")


        else:
            print("Directory already exists !, Skipping Youtube Data API Search...")


        # all other functions
        self.rename_files(full_path)
        self.trim_audio(dir_path)
        zipped_paths = self.zip_files(dir_path)
        if len(zipped_paths) == 0:
            print("No Zipped files found ! Unable to send mail.")

        else:
            subject = "An email with attachment of audio files from Python"
            body = f"This is an email with zipped attachment of 100 videos converted to audio downloaded according to given query :  {query}"

            for batch, path in enumerate(zipped_paths):
                self.sent_mail(path, subject, body, sender_email, receiver_email, email_password, batch)


if __name__ == "__main__":
    print("WELCOME TO AUTOMATING GOOGLE IMAGES DOWNLOAD")
    parser = argparse.ArgumentParser(description='Automating Google images download', epilog='Happy automation :)')
    parser.add_argument('dir_path', type=str, help='Output working directory')
    parser.add_argument('client_secrets_file_path', type=str, help='Client secrets file OAuth 2.0')
    parser.add_argument('chrome_driver_path', type=str, help='Path where chrome driver is stored')
    parser.add_argument('username', type=str, help='Username for google account OAuth')
    parser.add_argument('password', type=str, help='Password for google account OAuth')
    parser.add_argument('query_string', type=str, help='Query string to search for')
    parser.add_argument('sender_email', type=str, help='Sender\'s email for sending mails')
    parser.add_argument('receiver_email', type=str, help='receiver_email for sending mails')
    parser.add_argument('email_password', type=str, help='Password for email authorization')
    args = parser.parse_args()

    a_v_d = automate_videos_download()
    a_v_d.main(args.dir_path, args.client_secrets_file_path, args.chrome_driver_path, args.username, args.password, args.query_string, args.sender_email, args.receiver_email, args.email_password)

    #dir_path = "C:/users/DELL/Desktop"
    # client_secrets_file is downloaded from API console , by creating Oauth credentials
    # for any already existing project
    #client_secrets_file_path ="C:/Users/DELL/Desktop/YOUR_CLIENT_SECRET_FILE.json"
    # chrome_driver_path = "C:/Users/DELL/Desktop/chromedriver.exe"
    # username = "skumar4_be17@thapar.edu"
    # password = "SOURAVs99@"
    # query_string = "sharry mann"
    # a_v_d = automate_videos_download()
    #
    # sender_email = "skumar4_be17@thapar.edu"
    # receiver_email = "sauravkumarsct@gmail.com"
    # email_password = "SOURAVs99@"
    #
    # a_v_d.main(dir_path, client_secrets_file_path, chrome_driver_path, username, password, query_string, sender_email, receiver_email, email_password)
