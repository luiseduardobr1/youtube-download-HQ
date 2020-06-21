# Youtube Download - High Quality
Download the maximum quality resolution videos on Youtube and all the captions available.

# Why to use it
This code use [pytube library](https://python-pytube.readthedocs.io/en/latest/) to download youtube videos and their captions. However, there is a [youtube limitation](https://github.com/nficano/pytube) to download high quality video and audio codec's together in same file, then it's only possible to download audio and video (above 720p) separately. In this sense, this code can download both maximum quality video and audio files, merge them with [ffmpeg](https://www.ffmpeg.org/documentation.html) and get all captions available. The output files are: merged file (in *.mkv*), audio file, video file and the captions (in *.srt*). 

# Requirements
First, it's necessary to install **pytube**. If you are using [Jupyter Notebook](https://jupyter.org/), just paste this code in cell:
```
pip install pytube3
```
You may need to install [K-Lite Mega Codec Pack](https://k-lite-mega-codec-pack.br.uptodown.com/windows) too. 

# How to use
In **youtubeHQ.py**, get the youtube video link and paste on:
```Python
# Get video link
VIDEO = 'https://www.youtube.com/watch?v=0xY06PT5JDE'
```

or, on command-prompt:

```Python
> python youtubeHQ.py YOUTUBE_LINK_HERE
```

After that, create the directory **C:\\videos\\**, because that's where the files will be saved. This can be changed in the code. If subtitles are available, they will be downloaded and saved in the same folder. Don't forget to put **youtubeHQ.py** and **ffmpeg.exe** in the same folder. 

# Screenshot
![Output files](https://user-images.githubusercontent.com/56649205/71645595-63040080-2cb9-11ea-85be-08f04d7e2c6b.PNG)
