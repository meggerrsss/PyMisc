__author__ = 'Meghan'

import random
import datetime
import ephem

# upgrade ideas
# sunset including episode length
# more user-friendly (input screen)
# lists from a different file

new = ['flarrow','chicago','criminal minds','ncis','new girl','gotham','motive','once upon a time','scorpion','sherlock','big bang theory','night shift','vamporiginals','whose line','izombie','librarians','cyber']
anime = ['code geass','death note','gurren','log horizon','pokemon']
cartoon = ['dcau','teen titans go','fairly oddparents']
airing = ['bones','hawaii five-o','teen wolf','sheild/carter','red band','madam secretary']
old = ['sabrina','addams','big wolf','malcolm','smallville','drake and josh','pushing daisies','human target',]
shows = anime+cartoon+new+airing+old+['movie']
books = ['new 52', 'old', 'book']
both = shows+books
inactive = []
night = ['criminal minds']
started = ['vamporiginals','once upon a time','big bang theory','motive','cyber','night shift','chicago','scorpion','daredevil','whose line','dcau','smallville','flarrow','new girl','gotham','sherlock','dcau']
priority = shows+started

def sunset():
    o=ephem.Observer()
    o.lat='44.6'
    o.long='-63.5'
    s=ephem.Sun()
    s.compute()
    set = ephem.localtime(o.next_setting(s))
    return set

def isnight():
    now = datetime.datetime.now().hour
    suns = sunset().hour
    night = suns < now
    return night

def filt(li):
    if isnight():
        for y in night:
            if y in li:
                li.remove(y)
    for x in inactive:
        if x in li:
            li.remove(x)
    return li

f = filt(both)
g = filt(started)
h = filt(filt(priority))

def randombinlist(n):
    return [random.randint(0,1) for b in range(1,n+1)]

def tournament(lis):
    print lis
    l = len(lis)
    r = randombinlist(l)
    s = sum(r)
    new = []
    print r
    if l == 1:
        print lis[0]
    elif s == 0 or s == l:
        tournament(lis)
    else:
        for i in range(0,l):
            if r[i] == 1:
                new.append(lis[i])
        tournament(new)

def tournoprint(lis):
    l = len(lis)
    r = randombinlist(l)
    s = sum(r)
    new = []
    if l == 1:
        return lis[0]
    elif s == 0 or s == l:
        return tournoprint(lis)
    else:
        for i in range(0,l):
            if r[i] == 1:
                new.append(lis[i])
        return tournoprint(new)

def multi(n, lis):
    li = [0]*n
    for i in range(0,n):
        li[i] = tournoprint(lis)
    return li
    print li

multi(shows,1)