# Automate-images-download

# Introduction :   
Data collection is one of the important steps in Data analysis , Machine learning and Deep learning.
It is the process of gathering information of our interest, in our case it's the images of any type we want to gather.
Without data, we can't model our problem and do analysis of it.  

# Objective :
👉 Automate the downloading of images using Google Custom search API.   
👉 Optional : Resizing the images, Zipping the images and Sending a mail to yourself.    

# Getting credentials from Google Custom Search API :   

> Get the detailed steps and some troubleshooting help [here](https://github.com/souravs17031999/Automate-images-download/blob/master/google_api.txt).

* First, Create a [Gmail account](http://gmail.com/) for developement (or testing).
* Next , head on to [google developers console](https://console.developers.google.com/) and follow the steps below to create the new project (if you don't have any), you can skip this step if you already have some running project.     

![api1](/images/API1.gif)      

* Enable the API from [API explorer](https://console.developers.google.com/apis/) and Get the credentials as API KEY for accesing the API.       
 
![api2](/images/API2.gif)    

* Create Google Custom search engine [here](https://cse.google.com/cse/all) which will search and return the results.

![api3](/images/API3.gif)

# Getting Started Locally : 

* After getting the credentials , we can now run the script for automation.   

> Example :     
* Firstly, open the [script file](https://github.com/souravs17031999/Automate-images-download/blob/master/automate_images_download.py) and edit the sender_email, receiver_email and password available under main_run() function directly in the file (for privacy reasons).   
* Run Command prompt (or terminal).    
* Move to the directory where script is downloaded.    
* Now run the script in following way :     

positional arguments:   
| arguments  | details |
| ------------- | ------------- |
| dir_path | Output working directory |  
| query | Query string to search for |
| API | API KEY FOR GOOGLE CUSTOM SEARCH API |
| CX | CUSTOM SEARCH ENGINE ID  |
| imgSize | Size of image [icon/small/medium/large/xlarge/xxlarge/huge] |
| imgType | Type of image[clipart/face/lineart/stock/photo/animated] |
| imgColorType | Color of image[color/gray/mono] |     

optional arguments:         
  -h, --help  :  show this help message and exit     
  
```script_images_download.py C:/Users/DELL/Desktop "query" API CX huge photo color```      

![output](/images/output1.JPG)       

# Output :    
* All images (100 per call to script, can be changed from script) will be directly downloaded at new directory created : 'dataset_images'.
> Some samples of images : 
![output](/images/output5.JPG)         
![output](/images/output6.JPG)         
![output](/images/output2.JPG)         
![output](/images/output3.JPG)    
![output](/images/output4.JPG)          

