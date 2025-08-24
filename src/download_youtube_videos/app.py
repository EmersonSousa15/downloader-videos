import yt_dlp
import streamlit as st
import os

os.makedirs("downloads", exist_ok=True)
os.makedirs("downloads/audios", exist_ok=True)
os.makedirs("downloads/videos", exist_ok=True)

st.title("Downloader do YouTube")

url_video = st.text_input("Paste you video url:")
import streamlit as st

formats = {
    'Áudio': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': 'downloads/audios/%(title)s.%(ext)s',
    },
    'Vídeo': {
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm',   
        }],
        'outtmpl': 'downloads/videos/%(title)s.%(ext)s',
    }
}


format_labels = list(formats.keys())
format_selected = st.selectbox("Selecione o formato que deseja baixar", format_labels, 0)

ydl_opts = {
    'format': formats[format_selected]['format'],
    'outtmpl': formats[format_selected]['outtmpl'],
    'postprocessors': formats[format_selected]['postprocessors']
}

if st.button("Baixar áudio") and url_video:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_video])
    st.success("Download concluído!")



diretory_audio_path = "C:/Users/Emerson/Documents/projetos/downloader_youtube_videos/downloads/audios"
dir_audios_list = os.listdir(diretory_audio_path)

st.write("Áudios baixados:")

if (len(dir_audios_list) == 0):
    st.write("Nenhuma áudio encontrado!") 

for audio in dir_audios_list:
    path_audio = diretory_audio_path+'/'+audio
    st.text(audio.split('.')[0]+':')
    with open(path_audio, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
        
diretory_video_path = "C:/Users/Emerson/Documents/projetos/downloader_youtube_videos/downloads/videos"
dir_videos_list = os.listdir(diretory_video_path)

st.write("Vídeos baixados:") 

if (len(dir_videos_list) == 0):
    st.write("Nenhum vídeo encontrado!") 

for video in dir_videos_list:
    path_audio = diretory_video_path+'/'+video
    st.text(audio.split('.')[0]+':')
    with open(path_audio, "rb") as f:
        st.video(f.read(), format="video/webm")