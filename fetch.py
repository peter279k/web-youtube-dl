import sys
import youtube_dl

format = {'error': None}
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

try:
    results = ydl.extract_info(
        url,
        download=False)
except Exception as e:
    format['error'] = e

if format['error'] is not None:
    print(format)


format = {'links': []}
for result in results['formats']:
    if result['vcodec'] == 'none' or result['acodec'] == 'none':
        continue
    video_info = {}
    format_info = result['format'].split(' - ')
    quality = result['format'].split()[-1].replace(')', '').replace('(', '')
    video_quality = "%s, video, %s, audio"
    video_info['format'] = video_quality % (result['ext'], quality)
    video_info['itag'] = int(format_info[0])
    video_info['url'] = result['url']
    format['links'].append(video_info)

print(format)
