# Automate-Images + Videos-download

# Introduction :   
Data collection is one of the important steps in Data analysis , Machine learning and Deep learning.
It is the process of gathering information of our interest, in our case it's the images of any type we want to gather.
Without data, we can't model our problem and do analysis of it.  

# Objective :
👉 Automate the collection and building of images using Google API's for search and videos using Youtube API's.            
👉 Option to send mails to anyone containing collected datasets as attachment.       


# Getting credentials from Google Custom Search API :   

> Get the detailed steps and some troubleshooting help [here](https://github.com/souravs17031999/AUTOMATE-DATA-PIPELINE/blob/master/google_api.txt).

* First, Create a [Gmail account](http://gmail.com/) for developement (or testing).
* Next , head on to [google developers console](https://console.developers.google.com/) and follow the steps below to create the new project (if you don't have any), you can skip this step if you already have some running project.     

![api1](/images/API1.gif)      

* Enable the API from [API explorer](https://console.developers.google.com/apis/) and Get the credentials as API KEY for accesing the API.       
 
![api2](/images/API2.gif)    

* Create Google Custom search engine [here](https://cse.google.com/cse/all) which will search and return the results.

![api3](/images/API3.gif)

# Getting Started Locally : 

* After getting the credentials , we can now run the script for automation.  
* Firstly download all the files on your system using cmd (terminal) or git bash :     
```git clone https://github.com/souravs17031999/AUTOMATE-DATA-PIPELINE```   

## With Tkinter GUI : 
* Move to the directory where script is downloaded.    
* Now run the script in following way :  
```python data_automation.py```          
and arguments can be passed from interactive GUI.         

# Output :       
> Some samples of images :
![output](/images/output5.JPG)         
![output](/images/output6.JPG)         
![output](/images/output2.JPG)         
![output](/images/output4.JPG)          


### Limitations :  
There are few limitations :   
* Currently Google and Youtube allows 100 requests in one API call and so the script is able to download in total 100API's in one go but this behaviour can be changed from the script by calling it multiple times after tweaking some parameters which controls the after and before id's of returned images and videos and can be checked in their API documentation.        
* Considering big file sizes for sending as mails, i have resized , gray-scaled and then zipped the files and upload as attachment.    
This behaviour can be changed from the script by disabling some of the functions passing a optional parameter.       
