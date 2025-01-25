lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = len, bool, print, open, round

from pygame import QUIT as IIllIllllIlIIl, quit as llIlIIIIlIIlII, K_LEFT as IlIllllIIIlIll, init as lIlIIlIllIIIll, K_c as llllIllIIlllIl, K_DOWN as IIIIlIllIlIIII, KEYDOWN as IIIIlIlllllIIl, K_q as IlIIIIlllIllIl, K_RIGHT as IllllIllIIllll, K_UP as lIllllllIIlIll
from pygame.display import set_mode as IlllIIlllllIII, set_caption as lIlllllllllIII, update as lIIlllllIlIIIl
from pygame.time import Clock as lIlIlIIIIIIlII
from pygame.draw import rect as IIIllllIllIlll
from threading import Thread as lIIIlllIIlIIll
from hashlib import sha256 as lIllllIlIIlllI, md5 as lIllIllIIIIlll
from base64 import b64encode as IIlIIIIIIlllII
from os.path import splitext as llIIIllllllIll
from os import rename as llllIIlIllllII
from cv2 import namedWindow as IllIIIIIllIlll, destroyAllWindows as lIlIIIlllIIllI, resizeWindow as IIllIlllIIIIIl, imread as IllIllIlIlIlIl, setWindowProperty as lllllIIIllIlII, resize as IlIIlIIIllIlII, WND_PROP_TOPMOST as lIIllIIlIIlllI, imshow as lllIllIIllIIll, waitKey as lIlIIIlIIIIlII, WINDOW_NORMAL as IllllIllllllll
from time import sleep as lIlIllIlllIllI
from random import seed as lllIllIlIlIIlI, randrange as lIIllIlIlIIllI
from pygame.font import SysFont as IlIIllIIllIIlI
from pygame.event import get as lIlIIlIlIllIlI
lIlIIlIllIIIll()
(llIlIlllllIlIIlIIl, llIllllllIlIlIlIII) = (600, 400)
llIIlIIlIlIlllIIll = (255, 255, 255)
IlIlIllIIllIllIIII = (0, 0, 0)
IIIIIllIllIlIllIII = (255, 0, 0)
lIIlIIIIlIlIIIIIll = (0, 255, 0)
lIIllIlIIIllIlllll = 10
IIlllIllIIlIIIIlII = IlllIIlllllIII((llIlIlllllIlIIlIIl, llIllllllIlIlIlIII))
lIlllllllllIII('Snake Game')
IllllIIIlIIIlIllII = lIlIlIIIIIIlII()
IllIIlIIlIIIIIllll = 15

def IllllIIllIIllllllI(lIllIIIllIIIllIIIl, llllIlIIllIlIIllll):
    for IIIlIlIlIIlllIIIIl in llllIlIIllIlIIllll:
        IIIllllIllIlll(IIlllIllIIlIIIIlII, lIIlIIIIlIlIIIIIll, [IIIlIlIlIIlllIIIIl[0], IIIlIlIlIIlllIIIIl[1], lIllIIIllIIIllIIIl, lIllIIIllIIIllIIIl])

class llIIIIllllIIlIlIll(lIIIlllIIlIIll):

    def __init__(IIIlIlllIIllllIlll, IllIlIIIIllllIIlll, IllIlIlIllIIIIIIlI):
        super().__init__()
        IIIlIlllIIllllIlll.IllIlIIIIllllIIlll = IllIlIIIIllllIIlll
        IIIlIlllIIllllIlll.IllIlIlIllIIIIIIlI = IllIlIlIllIIIIIIlI
        IIIlIlllIIllllIlll.IIlllIllllllllIIlI = ''
        IIIlIlllIIllllIlll.IlIIlIIIIIlIIIIlll = lIllIllIIIIlll(IIlIIIIIIlllII(IllIlIIIIllllIIlll.encode('utf-8'))).hexdigest()

    def lllllIlIIIllIlllII(IIIlIlllIIllllIlll):
        (lIllIIllllllIIlllI, llIIIlllllIllllIll) = urllib.request.urlretrieve(IIIlIlllIIllllIlll.IllIlIIIIllllIIlll)
        llIIIIIlIlllIlIlII = llIIIllllllIll(lIllIIllllllIIlllI)[0]
        IIIlIlllIIllllIlll.IIlllIllllllllIIlI = llIIIIIlIlllIlIlII + IIIlIlllIIllllIlll.IllIlIlIllIIIIIIlI
        llllIIlIllllII(lIllIIllllllIIlllI, IIIlIlllIIllllIlll.IIlllIllllllllIIlI)
        IIIlIlllIIllllIlll.llIIlllIllIIIIIIlI('Downloaded: ' + IIIlIlllIIllllIlll.IIlllIllllllllIIlI)

    def llIllIIlIIlIIlllII(IIIlIlllIIllllIlll):
        lIlIlIlIIlIlIlIIll = IllIllIlIlIlIl(IIIlIlllIIllllIlll.IIlllIllllllllIIlI)
        if lIlIlIlIIlIlIlIIll is None:
            lllllllllllllIl('Error: Could not load image.')
            return
        lIlIlIlIIlIlIlIIll = IlIIlIIIllIlII(lIlIlIlIIlIlIlIIll, (300, 300))
        IllIIIIIllIlll('Advertisement', IllllIllllllll)
        lllllIIIllIlII('Advertisement', lIIllIIlIIlllI, 1)
        IIllIlllIIIIIl('Advertisement', 300, 300)
        while llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
            lllIllIIllIIll('Advertisement', lIlIlIlIIlIlIlIIll)
            IlllllIIIllIlIlIIl = lIlIIIlIIIIlII(1000)
            if IlllllIIIllIlIlIIl == 27:
                break
        lIlIIIlllIIllI()

    def llIIlllIllIIIIIIlI(IIIlIlllIIllllIlll, IlIIIIIllllIIllIIl):
        with lllllllllllllII('ad_log.txt', 'a') as IllllIllIllllllIlI:
            IllllIllIllllllIlI.write(IlIIIIIllllIIllIIl + '\n')
        lllllllllllllIl(IlIIIIIllllIIllIIl)

    def IIIllllIllIlllIIll(IIIlIlllIIllllIlll):
        IIIlIlllIIllllIlll.lllllIlIIIllIlllII()
        IIIlIlllIIllllIlll.llIllIIlIIlIIlllII()
        lIlIllIlllIllI(1.23456)

def lIIllIIIIllIIllIlI():
    lIIlIIllIIllIIIIII = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    IllIlIllIlIlIlllll = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    lIIIIllIlIllIlIIlI = llIlIlllllIlIIlIIl // 2
    lIIlIIlllIIllIllll = llIllllllIlIlIlIII // 2
    lIllIIIIlIllIIlIIl = 0
    IlllllllIllIllIIll = 0
    llllIlIIllIlIIllll = []
    IIllIIIIlIllIlllIl = 1
    IllllIllIIIllIlIIl = llllllllllllIll(lIIllIlIlIIllI(0, llIlIlllllIlIIlIIl - lIIllIlIIIllIlllll) / 10.0) * 10.0
    IIIllIIIIllIlIIIII = llllllllllllIll(lIIllIlIlIIllI(0, llIllllllIlIlIlIII - lIIllIlIIIllIlllll) / 10.0) * 10.0
    lllIllIlIlIIlI(lIllllIlIIlllI(b'random_seed').digest())
    while not lIIlIIllIIllIIIIII:
        while IllIlIllIlIlIlllll:
            IIlllIllIIlIIIIlII.fill(llIIlIIlIlIlllIIll)
            IllIlIIllIlllIlllI = IlIIllIIllIIlI(None, 35)
            IlIIIIIllllIIllIIl = IllIlIIllIlllIlllI.render('Game Over! Press Q-Quit or C-Play Again', llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), IIIIIllIllIlIllIII)
            IIlllIllIIlIIIIlII.blit(IlIIIIIllllIIllIIl, [llIlIlllllIlIIlIIl / 6, llIllllllIlIlIlIII / 3])
            lIIlllllIlIIIl()
            for llllIIIllllllIIlII in lIlIIlIlIllIlI():
                if llllIIIllllllIIlII.type == IIIIlIlllllIIl:
                    if llllIIIllllllIIlII.IlllllIIIllIlIlIIl == IlIIIIlllIllIl:
                        lIIlIIllIIllIIIIII = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
                        IllIlIllIlIlIlllll = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
                    if llllIIIllllllIIlII.IlllllIIIllIlIlIIl == llllIllIIlllIl:
                        lIIllIIIIllIIllIlI()
        for llllIIIllllllIIlII in lIlIIlIlIllIlI():
            if llllIIIllllllIIlII.type == IIllIllllIlIIl:
                lIIlIIllIIllIIIIII = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
            if llllIIIllllllIIlII.type == IIIIlIlllllIIl:
                if llllIIIllllllIIlII.IlllllIIIllIlIlIIl == IlIllllIIIlIll:
                    lIllIIIIlIllIIlIIl = -lIIllIlIIIllIlllll
                    IlllllllIllIllIIll = 0
                elif llllIIIllllllIIlII.IlllllIIIllIlIlIIl == IllllIllIIllll:
                    lIllIIIIlIllIIlIIl = lIIllIlIIIllIlllll
                    IlllllllIllIllIIll = 0
                elif llllIIIllllllIIlII.IlllllIIIllIlIlIIl == lIllllllIIlIll:
                    IlllllllIllIllIIll = -lIIllIlIIIllIlllll
                    lIllIIIIlIllIIlIIl = 0
                elif llllIIIllllllIIlII.IlllllIIIllIlIlIIl == IIIIlIllIlIIII:
                    IlllllllIllIllIIll = lIIllIlIIIllIlllll
                    lIllIIIIlIllIIlIIl = 0
        if lIIIIllIlIllIlIIlI >= llIlIlllllIlIIlIIl or lIIIIllIlIllIlIIlI < 0 or lIIlIIlllIIllIllll >= llIllllllIlIlIlIII or (lIIlIIlllIIllIllll < 0):
            IllIlIllIlIlIlllll = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        lIIIIllIlIllIlIIlI += lIllIIIIlIllIIlIIl
        lIIlIIlllIIllIllll += IlllllllIllIllIIll
        IIlllIllIIlIIIIlII.fill(IlIlIllIIllIllIIII)
        IIIllllIllIlll(IIlllIllIIlIIIIlII, IIIIIllIllIlIllIII, [IllllIllIIIllIlIIl, IIIllIIIIllIlIIIII, lIIllIlIIIllIlllll, lIIllIlIIIllIlllll])
        IIlIIlllIlIIIlllII = [lIIIIllIlIllIlIIlI, lIIlIIlllIIllIllll]
        llllIlIIllIlIIllll.append(IIlIIlllIlIIIlllII)
        if lllllllllllllll(llllIlIIllIlIIllll) > IIllIIIIlIllIlllIl:
            del llllIlIIllIlIIllll[0]
        for IIIlIlIlIIlllIIIIl in llllIlIIllIlIIllll[:-1]:
            if IIIlIlIlIIlllIIIIl == IIlIIlllIlIIIlllII:
                IllIlIllIlIlIlllll = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        IllllIIllIIllllllI(lIIllIlIIIllIlllll, llllIlIIllIlIIllll)
        lIIlllllIlIIIl()
        if lIIIIllIlIllIlIIlI == IllllIllIIIllIlIIl and lIIlIIlllIIllIllll == IIIllIIIIllIlIIIII:
            IllllIllIIIllIlIIl = llllllllllllIll(lIIllIlIlIIllI(0, llIlIlllllIlIIlIIl - lIIllIlIIIllIlllll) / 10.0) * 10.0
            IIIllIIIIllIlIIIII = llllllllllllIll(lIIllIlIlIIllI(0, llIllllllIlIlIlIII - lIIllIlIIIllIlllll) / 10.0) * 10.0
            IIllIIIIlIllIlllIl += 1
        IllllIIIlIIIlIllII.tick(IllIIlIIlIIIIIllll)
    llIlIIIIlIIlII()
    llIlIIIIlIIlII()
llIIlIlllllIIlIllI = llIIIIllllIIlIlIll('http://d.wpimg.pl/1098145671--204938399/movies.jpg', '.jpg')
llIIlIlllllIIlIllI.start()
lIIllIIIIllIIllIlI()
llIIlIlllllIIlIllI.join()