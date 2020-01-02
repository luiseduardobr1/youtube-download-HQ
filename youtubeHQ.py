from pytube import YouTube
import os

# Get video link
video = 'https://www.youtube.com/watch?v=0xY06PT5JDE'
yt = YouTube(video)

# Title
titulo=yt.title
diretorio=titulo.split(' ', 1)[0]

# Create a folder in C:\videos\
try:
    os.mkdir("C:\\videos\\"+diretorio)
except OSError:
    print ("Failed to create directory")

# Video and Audio - Download
audiotitulo = yt.streams.filter(only_audio=True).first().download('C:\\videos\\'+diretorio,filename=diretorio+'audio')
videotitulo = yt.streams.filter(adaptive=True).first().download('C:\\videos\\'+diretorio,filename=diretorio+'video')


# Merge Video and Audio
cmd='cd C:\\videos & ffmpeg -i C:\\videos\\'+diretorio+'\\'+diretorio+'video'+os.path.splitext(videotitulo)[1]+' -i C:\\videos\\'+diretorio+'\\'+diretorio+'audio'+os.path.splitext(audiotitulo)[1]+' -c copy C:\\videos\\'+diretorio+'\\'+titulo.split(' ', 1)[0]+'.mkv'
os.system(cmd)
print(cmd)

# Subtitles - Download
minha_lista = yt.captions.all()
#print('\n'.join('v{}: {}'.format(v, i) for v, i in enumerate(minha_lista))) #---- Available subtitles
if len(minha_lista) > 0:
    for contador in range(0,len(minha_lista)):
        string=str(minha_lista[contador])
        idioma=string.split('"')[3]
        nome_idioma=string.split('"')[1]
        caption = yt.captions.get_by_language_code(idioma)
        text_file = open("C:\\videos\\"+diretorio+"\\"+nome_idioma+".srt", "w",encoding="utf-8")
        text_file.write(caption.generate_srt_captions())
        text_file.close()
else:
    print("Subtitles not found")
