# Automate-Images + Videos-download

# Introduction :   
Data collection is one of the important steps in Data analysis , Machine learning and Deep learning.
It is the process of gathering information of our interest, in our case it's the images of any type we want to gather.
Without data, we can't model our problem and do analysis of it.  

# Objective :
👉 Automate the collection and building of images using Google API's for search and videos using Youtube API's.            
👉 Option to send mails to anyone containing collected datasets as attachment.       


# Getting credentials for Google API and Youtube API:   

> For [Google image API](https://github.com/souravs17031999/AUTOMATE-DATA-PIPELINE/blob/master/Google_API_images.md)
> For [Youtube API]()

# Getting Started Locally : 

* After getting the credentials , we can now run the script for automation.  
* Firstly download all the files on your system using cmd (terminal) or git bash :     
```git clone https://github.com/souravs17031999/AUTOMATE-DATA-PIPELINE```   

## With Tkinter GUI :    
### For IMAGES : 
* Move to the directory where script is downloaded.    
* Now run the script in following way :  
```python data_image_automation.py```          
and arguments can be passed from interactive GUI.           

### For VIDEOS :  
* Move to the directory where script is downloaded.    
* Now run the script in following way :  
```python data_video_automation.py```          
and arguments can be passed from interactive GUI.        
Note : Two important args :         
> Client secrets file path: Give absolute path.    
> Chrome driver path : Give absolute path with .exe extension.   

# Output :       
> Some samples of images :
![output](/images/output5.JPG)         
![output](/images/output6.JPG)         
![output](/images/output2.JPG)         
![output](/images/output4.JPG)          
![output](/images/output10.JPG)          


### Limitations and Scope for future work:  
There are few limitations :   
* Currently Google and Youtube allows 100 requests in one API call and so the script is able to download in total 100API's in one go but this behaviour can be changed from the script by calling it multiple times after tweaking some parameters which controls the after and before id's of returned images and videos and can be checked in their API documentation.        
* Considering big file sizes for sending as mails, i have resized , gray-scaled and then zipped the files and upload as attachment.    
This behaviour can be changed from the script by disabling some of the functions passing a optional parameter.  
* Also, mail can be only sent for GMAIL users as of now, this can also be changed by manipulating the Ports of all email servers and controlling their behaviours in the script.   
