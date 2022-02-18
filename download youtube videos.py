from pytube import YouTube 
SAVE_PATH = "E:/" 
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
try: 
    yt = YouTube(link) 
except: 
    print("Connection Error")  
mp4files = yt.filter('mp4') 
  
yt.set_filename('YouTube Video')  
  

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    d_video.download(SAVE_PATH) 
except: 
    print("Ther is some Error!") 
print('Task Completed!') 
