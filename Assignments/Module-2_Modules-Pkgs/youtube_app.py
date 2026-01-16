from pytubefix import YouTube

url="https://www.youtube.com/watch?v=u4yGpeunVAA&list=RDu4yGpeunVAA&start_radio=1"

YouTube(url).streams.first().download()