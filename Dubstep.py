import re
def song_decoder(song):
    str1 = []
    for i in song.split('WUB'):
        if i == '':
            pass
        else:      
            str1.append(i)
    return ' '.join(str1).strip()


#def song_decoder(song):
    #return re.sub('(WUB)+', ' ', song).strip()
