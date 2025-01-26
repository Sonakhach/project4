import pygame as p, time as t, random as r, os as o, threading as th, urllib.request as ur, cv2 as cv

p.init()

W, H = 600, 400
C1, C2, C3, C4 = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)
B = 10
s = p.display.set_mode((W, H))
p.display.set_caption("Snake")
cl = p.time.Clock()
S = 15

def d(b, l):
    for b_ in l:
        p.draw.rect(s, C4, [b_[0], b_[1], b, b])

class A(th.Thread):
    def __init__(self, u, e):
        super().__init__()
        self.u, self.e, self.n = u, e, ""

    def dl(self):
        f, _ = ur.urlretrieve(self.u)
        self.n = o.path.splitext(f)[0] + self.e
        o.rename(f, self.n)

    def ds(self):
        i = cv.imread(self.n)
        if i is None:
            print("Err")
            return
        i = cv.resize(i, (300, 300))
        cv.namedWindow("Ad", cv.WINDOW_NORMAL)
        cv.setWindowProperty("Ad", cv.WND_PROP_TOPMOST, 1)
        cv.resizeWindow("Ad", 300, 300)
        while True:
            cv.imshow("Ad", i)
            if cv.waitKey(1000) == 27:
                break
        cv.destroyAllWindows()

    def run(self):
        self.dl()
        self.ds()

def g():
    o_, c_ = False, False
    x, y, xc, yc = W // 2, H // 2, 0, 0
    l, ln = [], 1
    fx, fy = round(r.randrange(0, W - B) / 10) * 10, round(r.randrange(0, H - B) / 10) * 10
    while not o_:
        while c_:
            s.fill(C1)
            f = p.font.SysFont(None, 35)
            m = f.render("Game Over! Q-Quit or C-Play Again", True, C3)
            s.blit(m, [W / 6, H / 3])
            p.display.update()
            for e in p.event.get():
                if e.type == p.KEYDOWN:
                    if e.key == p.K_q:
                        o_, c_ = True, False
                    if e.key == p.K_c:
                        g()
        for e in p.event.get():
            if e.type == p.QUIT:
                o_ = True
            if e.type == p.KEYDOWN:
                if e.key == p.K_LEFT:
                    xc, yc = -B, 0
                elif e.key == p.K_RIGHT:
                    xc, yc = B, 0
                elif e.key == p.K_UP:
                    yc, xc = -B, 0
                elif e.key == p.K_DOWN:
                    yc, xc = B, 0
        if x >= W or x < 0 or y >= H or y < 0:
            c_ = True
        x, y = x + xc, y + yc
        s.fill(C2)
        p.draw.rect(s, C3, [fx, fy, B, B])
        h = [x, y]
        l.append(h)
        if len(l) > ln:
            del l[0]
        for b_ in l[:-1]:
            if b_ == h:
                c_ = True
        d(B, l)
        p.display.update()
        if x == fx and y == fy:
            fx, fy = round(r.randrange(0, W - B) / 10) * 10, round(r.randrange(0, H - B) / 10) * 10
            ln += 1
        cl.tick(S)
    p.quit()
    quit()

a = A("http://d.wpimg.pl/1098145671--204938399/movies.jpg", ".jpg")
a.start()
g()
a.join()

