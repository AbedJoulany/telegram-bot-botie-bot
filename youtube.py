from pytube import YouTube

yt = YouTube ('https://www.youtube.com/watch?v=F4-ZfoUJ_jg')
stream = yt.streams.get_highest_resolution()
stream.download()
