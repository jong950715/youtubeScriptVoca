import youtube_transcript_api
import re
from youtube_transcript_api import YouTubeTranscriptApi
from functools import reduce

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

def getWordsFromYoutube(videoId):
    tf, text, possibelLang = getCaptionByVideoid(videoId)
    if not tf:
        return [False, []]
    words = getWords(text)
    return [True, words]

if __name__ == "__main__":
    print(getWordsFromYoutube("FWTNMzK9vG4"))