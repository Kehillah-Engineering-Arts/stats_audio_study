import os, sys, secrets
from pydub import AudioSegment

audio_source_file = sys.argv[1] #get first argument from command line
song_name = audio_source_file.split('.')[0].split('/')[1]
print(song_name)

#import audio file
lossless_audio = AudioSegment.from_file(
    audio_source_file,
    format='aiff'
)

#make a directory for mp3s with same name as song
if not os.path.exists('mp3s/' + song_name):
    os.makedirs('mp3s/' + song_name)

#export mp3s with random extensions
bitrates_to_export = ['96k', '128k', '320k']
for br in bitrates_to_export:
    random_suffix = secrets.token_hex(4)
    output_path = "mp3s/%s/%s_%s.mp3" % (song_name, song_name, random_suffix)
    lossless_audio.export(
        output_path,
        format="mp3",
        bitrate=br
    )
