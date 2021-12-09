from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from re import search
def searchVideo():
    ydl_opts = {'format': 'mp4'}
    searchTerms = input("Search Query: ")
    isUrl = search("http", searchTerms)
    if isUrl:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(searchTerms)
        return 0
    else:      
        info = YoutubeSearch(searchTerms, max_results=5).to_dict()
        print("\nVideo selection. Type the video number to continue.\n")
        for i, video in enumerate(info, start=1):
	        video["no"] = i
	        print(f"{video.get('no')}. {video.get('title')} - {video.get('duration')}")
        selected = (input("\n"))
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download("https://www.youtube.com/watch?v=" + info[int(selected)-1].get('id'))    	
        return 0
searchVideo()        
