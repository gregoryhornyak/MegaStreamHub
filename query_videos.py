from pytube import YouTube
import sys 
  
print("Argument List:", str(sys.argv)) 

URL = sys.argv[1]
VIDEO_NAME = sys.argv[2]

YouTube(URL).streams.get_highest_resolution().download(filename=VIDEO_NAME,output_path="./media_dir")