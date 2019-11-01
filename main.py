from random import shuffle, randint
text = ''
def getfile():
    file = input('File? >>> ').replace('\\','/')
    try:
        with open(file) as f:
            text = f.read()
        f.closed
    except:
        print("Invalid file!")
        return False
    for i in range(len(text)):
        if text[i].lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            text = text[:i]+'!'+text[i+1:]
    text = text.split('!')
    i = 0
    while i in range(len(text)):
        if text[i] == '':
            del text[i]
            i -= 0
        else:
            text[i] = text[i].lower()
            i += 1
    shuffle(text)
    return text[:3]

def lastpunc(li,hs):
    softpunc, hardpunc = '',''
    for i in range(len(li)-1,0,-1):
        if li[i][-1] in ',;:' and not softpunc: softpunc = len(li)-i
        elif li[i][-1] in '?!.' and not hardpunc: hardpunc = len(li)-i
    if hs == 'hard' and hardpunc: return hardpunc
    elif hs == 'soft' and softpunc: return softpunc
    elif hs == 'both' and hardpunc and softpunc: return [softpunc, hardpunc]
    else:
        if hs == 'hard': return len(li)
        elif hs == 'soft': return len(li)
        else: return [len(li),len(li)]

def addpunc(hs):
    punc_num = randint(0,6)
    if hs == 'soft':
        if punc_num == 5: return ';'
        elif punc_num == 6: return ':'
        else: return ','
    elif hs == 'hard':
        if punc_num == 5: return '?'
        elif punc_num == 6: return '!'
        else: return '.'
    else:
        punc_num = randint(0,12)
        if punc_num == 5: return ';'
        elif punc_num == 6: return ':'
        elif punc_num < 5: return ','
        elif punc_num == 11: return '?'
        elif punc_num == 12: return '!'
        else: return '.'
    
while not text:
    text = getfile()
text = text + [','] + [';'] + [':'] + ['?'] + ['!'] + ['.']
wordcount = randint(60,100)
speech = [text[randint(0,2)],text[randint(0,2)]]
for i in range(wordcount-2):
    speech.append(text[randint(0,2)])
    punc = lastpunc(speech,'both') #[0] is soft, [1] is hard
    if punc[0] < punc[1] and punc[1] <= 2*punc[0]: punc.append(punc[0])
    else: punc.append(punc[1])
    if 9-punc[2] < 0: punc[2] = 9
    if punc[1] > 2 and punc[0] > 1 and randint(0,18-2*punc[2]) == 0:
        speech[-1] = str(speech[-1]) + addpunc('')

if not speech[-1][-1] in '?!.':
    if not speech[-1][-1] in ',;:': speech[-1] = str(speech[-1]) + addpunc('hard') #ending punctuation
    else: speech[-1] = str(speech[-1][:-1]) + addpunc('hard')
speech[0] = speech[0][0].upper() + speech[0][1:] #capitalise first letter
for i in range(1,len(speech)): #capitalise first letter in each sentence
    if speech[i-1][-1] in '?!.': speech[i] = speech[i][0].upper() + speech[i][1:]

print('\n',' '.join(speech))
