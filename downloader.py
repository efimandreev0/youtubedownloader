import sys
from pytube import YouTube

def info():
    print("Usage: python toolName.py linkToVideo resolution(High\low)")
    
def main():
    Link = sys.argv[1]
    video = YouTube(Link)
    
    if sys.argv[2] == "High":
        output = video.streams.get_highest_resolution()
    else:
        output = video.streams.get_lowest_resolution()
    
    output.download()
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        info()
    else:
        main()