# Below are steps for Getting auth tokens for Youtube Videos API.

* Create a google account for developement   
* Create a new project first from developers console if there is no existing project    
* Go to API explorer from developers console and enable "YouTube Data API v3"     
* Authenticate first from "OAuth consent screen" configuration from left side of console        
* Then come to "credentials" , create credentials by selecting "OAuth client ID " , then download the client secrets file and copy the 
API key and keep it safe.       
* Here we are using Google-Oauthlib-flow library for making authorization flow easier.   
* In this automation, we need to know that CMD is very important as we have to copy the token granted by google OAuth to the terminal.   
> Getting troubleshoot [help](youtube_api.txt)    
> For more help, [API docs](https://developers.google.com/youtube/v3/docs/videos/list)    
