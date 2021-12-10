    from yt_dlp import YoutubeDL
    from youtube_search import YoutubeSearch
    from re import search
    from time import sleep

    ydl_opts = {'format': 'mp4',
                'quiet': True,
                'x': True,
                'audio-format': 'mp3'}
    querysize = 10
    def changeOpt(opt):
        pass
    def searchVideo():
        while True:
            query = input("\nSearch Query (type 'quit' to quit): ")
            if query == 'quit' or query == 'q':
                break
            if "https://www.youtube.com/watch?v=" in query:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(query)
                    print('Video Downloaded.')
                pass
            else:
                info = YoutubeSearch(query, max_results=querysize).to_dict()
                while True:
                    print("\nVideo selection. Type the video number to continue.\n")
                    for i, video in enumerate(info, start=1):
                        video["no"] = i
                        sleep(0.05)
                        print(f"{video.get('no')}. {video.get('title')} - {video.get('duration')}")
                    selected = (input("\n"))
                    if int(selected) not in range(1, querysize+1):
                        print(f"please input a number between 1 and {querysize}.")
                        sleep(1)
                        pass
                    break
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download("https://www.youtube.com/watch?v=" + info[int(selected)-1].get('id'))    	
                    print('Video Downloaded.')
    if __name__ == '__main__' :
            searchVideo()    
