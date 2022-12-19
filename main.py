import youtube_transcript_api
import re
from youtube_transcript_api import YouTubeTranscriptApi
from functools import reduce
from bs4 import BeautifulSoup
import requests
import urllib

def getCaptionByVideoid(videoId, lang = 'en'):
    transcriptList = YouTubeTranscriptApi.list_transcripts(videoId)
    possibleLang = list(transcriptList._manually_created_transcripts.keys())
    possibleLang.extend(list(transcriptList._generated_transcripts.keys()))

    try:
        srt = transcriptList.find_transcript((lang,)).fetch()
    except youtube_transcript_api.NoTranscriptFound as e:
        return (False, "", possibleLang)

    text = reduce(lambda x,y:x+y['text'], srt,"")
    
    return (True, text, possibleLang)

def getWords(text):
    p = re.compile('[a-zA-Z]+')
    res = p.findall(text)
    res = list(filter(lambda x: len(x) > 2, res))
    return res

def naverEngToKor(word):
    '''
    _url = "http://m.endic.naver.com/search.nhn?searchOption=entryIdiom&query={}".format(word)
    resp = urllib.request.urlopen(_url).read()
    soup = BeautifulSoup(resp, 'html.parser')
    print(resp)
    '''

    url = 'http://m.endic.naver.com/search.nhn?searchOption=entryIdiom&query=' + word
    url = urllib.request.quote(url, '/:?=&')
    resp = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(resp, "html.parser")

    ## CSS Selector를 통해 html요소들을 찾아낸다.
    my_titles = soup.select('#searchPage_entry > div')
    print(resp)


if __name__ == "__main__":
    naverEngToKor('like')
    #caption = getCaptionByVideoid("FWTNMzK9vG4")
    #words = getWords(caption[1])