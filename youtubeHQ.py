from pytube import YouTube
import os
import string
import sys


if len(sys.argv) > 1:
    VIDEO = sys.argv[1]
else:
    # Default
    VIDEO = 'https://www.youtube.com/watch?v=o2IJaj3nUmU'

# Get video link
yt = YouTube(VIDEO)

# Title
author = yt.author
titulo = yt.title
dirname = str(titulo) + str(author)
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
diretorio = dirname.translate(remove_punctuation_map)

# Create a folder
try:
    os.mkdir(diretorio)
except OSError:
    print ("Failed to create directory")

# Downloading text
print(f'Baixando {str(titulo)} do canal {str(author)} ...')
print('Aguarde alguns minutos')

# Video and Audio - Download
audiotitulo = yt.streams.filter(only_audio=True).first().download(diretorio, filename = diretorio + '_audio')
videotitulo = yt.streams.filter(adaptive=True).first().download(diretorio, filename = diretorio + '_video')

# Merge Video and Audio
cmd = f'ffmpeg -i "{os.path.normpath(videotitulo)}" -i "{os.path.normpath(audiotitulo)}" -c copy "{os.path.join(os.getcwd(), diretorio, "resultant_video.mp4")}" -v quiet'
os.system(cmd)

# Subtitles - Download
my_captions = yt.captions
if len(my_captions) > 0:
    for subtitle in my_captions:
        subtitle_name = str(subtitle).split('"')[1]
        with open(diretorio + "\\" + subtitle_name + ".srt", "w", encoding="utf-8") as f:
            f.write(subtitle.generate_srt_captions())

# End
print('Finalizado')