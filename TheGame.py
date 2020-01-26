import math, pygame, os

pygame.init()
size = width, height = 960, 520
screen = pygame.display.set_mode(size)
background1 = pygame.sprite.Group()
background2 = pygame.sprite.Group()
choose = pygame.sprite.Group()
friend = pygame.sprite.Group()
persF = pygame.sprite.Group()
persE = pygame.sprite.Group()
Heads = pygame.sprite.Group()
deads = pygame.sprite.Group()
snipeFire = pygame.mixer.Sound('data\snipeFire.wav')
gun = pygame.sprite.Group()
shild = pygame.sprite.Group()
aim = pygame.sprite.Group()
FPS = 60
ZX = 0


def load_image(name, k, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k)))
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, group):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.k = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        if self.k != 0:
            self.cur_frame = (self.cur_frame + 7 / FPS * self.k)
            if math.fabs(self.cur_frame) > len(self.frames):
                self.cur_frame = 0
                self.k = 0
            self.image = self.frames[int(self.cur_frame)]


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(aim)
        self.image = load_image('aim.png', 1 / 24)
        self.rect = pygame.Rect(0, 0, self.image.get_width() * 0.3, self.image.get_height() * 0.3)
        self.y = (self.rect.x - 260) // 50
        self.x = 0
        self.tipe = 0
        self.f = False
        self.mask = pygame.mask.from_surface(self.image)

    def opr(self):
        if pygame.sprite.spritecollideany(self, persF) and not self.f:
            self.image = load_image('aimFriend.png', 1 / 16)
        elif self.f and any(i.activ == 1 for i in PERSES):
            self.image = load_image('aimTarg.png', 1 / 32)
            self.rect.x -= self.image.get_width() // 2
            self.rect.y -= self.image.get_height() // 2
        else:
            self.image = load_image('aim.png', 1 / 24)

    def update(self):
        self.y = (self.rect.y - 260) // 50
        self.x = int(self.rect.x - (self.rect.y - 260) + 170 + ZX) // 100
        if 0 <= self.y <= 2 and 0 <= self.x < len(MAP[0]):
            MAP[self.y][self.x] = 2

    def action(self):
        if pygame.sprite.spritecollideany(self, persF) and not self.f:
            for i in PERSES:
                if i.activ == 1 and pygame.sprite.spritecollideany(self, persF).tipe[0] != i.tipe:
                    i.activ = -1
                    break
            PERSES[[i.tipe for i in PERSES].index(pygame.sprite.spritecollide(self, persF, False)[0].tipe[0])].activ *= -1
        elif not self.f and any(i.activ == 1 for i in PERSES) \
                and not self.f and any(i.activ == 1 for i in PERSES):
            if 0 <= self.y <= 2 and 0 <= self.x <= len(MAP[0]):
                for i in PERSES:
                    if i.activ == 1:
                        i.ytarg = (self.rect.y - 260) // 50
                        i.xtarg = int(self.rect.x - (self.rect.y - 260) + 170 + ZX) // 100
        elif self.f and any(i.activ == 1 for i in PERSES):
            if pygame.sprite.spritecollideany(self, persE):
                PERSES[[i.activ for i in PERSES].index(True)].targ \
                    = [pygame.sprite.spritecollideany(self, persE).mommy,
                pygame.sprite.spritecollideany(self, persE).tipe[1]]


class Pers:
    def __init__(self, stats, pazzle, t, x, y):
        self.maxhp = stats[0]
        self.hp = self.maxhp
        self.dmg = stats[1]
        self.armor = stats[2]
        self.dodge = stats[3]
        self.aim = stats[4]
        self.speed = stats[5]
        self.pazzle = pazzle
        self.miniPazzle = pazzle.copy()
        self.revers = 1
        self.dk = 1
        self.tipe = t
        self.activ = -1
        self.targ = ''
        self.y = y * 50 + 290
        self.x = x * 100 + y * 50
        self.pazzle[-1].x = self.x - self.pazzle[-1].image.get_width() // 2 - 100
        self.pazzle[-1].y = self.y - self.pazzle[-1].image.get_height()
        self.pazzle[-1].rect.x = int(self.pazzle[-1].x)
        self.pazzle[-1].rect.y = int(self.pazzle[-1].y)
        for i in pazzle:
            i.mommy = self
        self.xp = x
        self.yp = y
        self.xtarg = x
        self.ytarg = y
        for i in range(len(self.pazzle[:-1]) - 1, -1, -1):
            self.pazzle[i].x = self.pazzle[i + 1].x + self.pazzle[i].sx
            self.pazzle[i].rect.x = int(self.pazzle[i].x)
            self.pazzle[i].y = self.pazzle[i + 1].y - self.pazzle[i].image.get_height() + self.pazzle[i].sy
            self.pazzle[i].rect.y = int(self.pazzle[i].y)

    def update(self):
        for i in self.pazzle + [self]:
            if i.hp <= 0:
                self.hp = 0
                self.dead()
                break
        pygame.draw.rect(screen, pygame.Color('red'),
                         (self.pazzle[0].rect.center[0] - 25, self.pazzle[0].y - 10, 50, 5))
        pygame.draw.rect(screen, pygame.Color('green'),
                         (self.pazzle[0].rect.center[0] - 25, self.pazzle[0].y - 10, int(50 * self.hp / self.maxhp), 5))
        self.move()
        MAP[int(self.yp)][int(self.xp)] = 1
        self.pazzle[0].update()
        self.pazzle[-1].update()
        self.yp = (self.y - 290) // 50
        self.xp = (self.x - self.yp * 50) // 100

    def move(self):
        if int(self.y) != self.ytarg * 50 + 290:
            if int(self.y) > self.ytarg * 50 + 290:
                for i in self.pazzle + [self]:
                    i.y -= self.speed / FPS
                    if i != self:
                        i.rect.y = int(i.y)
            if int(self.y) < self.ytarg * 50 + 290:
                for i in self.pazzle + [self]:
                    i.y += self.speed / FPS
                    if i != self:
                        i.rect.y = int(i.y)
        if int(self.x) != self.xtarg * 100 + self.ytarg * 50:
            if int(self.x) > self.xtarg * 100 + self.ytarg * 50:
                for i in self.pazzle + [self]:
                    i.x -= self.speed / FPS
                    if i != self:
                        i.rect.x = int(i.x)
                if int(self.pazzle[-1].cur_frame) == 0:
                    self.pazzle[-1].k = -0.85 * self.revers
            elif int(self.x) < self.xtarg * 100 + self.ytarg * 50:
                for i in self.pazzle + [self]:
                    i.x += self.speed / FPS
                    if i != self:
                        i.rect.x = int(i.x)
                if int(self.pazzle[-1].cur_frame) == 0:
                    self.pazzle[-1].k = 0.9 * self.revers
        if int(self.pazzle[0].cur_frame) == 0:
            self.pazzle[0].k = 1
        if self.targ != '':
            if self.targ[0].hp <= 0:
                self.targ = ''

    def rev(self, image):
        if self.revers == 1:
            return image
        else:
            return pygame.transform.flip(image, True, False)


class Enemy(Pers):
    def __init__(self, stats, pazzle, t, x, y):
        super().__init__(stats, pazzle, t, x, y)

    def update(self):
        super().update()
        stop = False
        if self.targ == '':
            for i in range(0, -5, -1):
                for j in range(3):
                    if MAP[j][int(self.xp) + i] != 0:
                        if j == int(self.yp) and i == 0:
                            continue
                        self.targ = [PERSES[[[i.xp, i.yp] for i in PERSES].index([int(self.xp) + i, j])], 1]
                        stop = True
                        break
                if stop:
                    break


class Friend(Pers):
    def __init__(self, stats, pazzle, t, x, y):
        super().__init__(stats, pazzle, t, x, y)
        self.miniPers()

    def miniPers(self):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.pazzle[0].image
        self.sprite.rect = self.sprite.image.get_rect()
        Heads.add(self.sprite)
        self.sprite.rect.x = 5
        self.sprite.rect.y = 20


class FriendSniper(Friend):
    def __init__(self, stats, pazzle, t, x, y, gun, ammo):
        super().__init__(stats, pazzle, t, x, y)
        self.gun = gun
        self.ammonow = ammo
        self.ammo = ammo
        self.gun.x = self.pazzle[-1].x + self.gun.sx
        self.gun.rect.x = int(self.gun.x)
        self.gun.y = self.pazzle[-1].y - self.gun.image.get_height() + self.gun.sy
        self.gun.rect.y = int(self.gun.y)

    def update(self):
        super().update()
        if self.targ != '':
            self.attack()
        self.gun.update()
        self.pazzle[1].update()
        self.moveG()
        for i in self.pazzle + [self.gun]:
            i.rect.x = int(i.x) - ZX

    def moveG(self):
        if int(self.y) != self.ytarg * 50 + 290:
            if int(self.y) > self.ytarg * 50 + 290:
                self.gun.y -= self.speed / FPS
                self.gun.rect.y = int(self.gun.y)
            if int(self.y) < self.ytarg * 50 + 290:
                self.gun.y += self.speed / FPS
                self.gun.rect.y = int(self.gun.y)
        if int(self.x) != self.xtarg * 100 + self.ytarg * 50:
            if int(self.x) > self.xtarg * 100 + self.ytarg * 50:
                self.gun.x -= self.speed / FPS
                self.gun.rect.x = int(self.gun.y)
            elif int(self.x) < self.xtarg * 100 + self.ytarg * 50:
                self.gun.x += self.speed / FPS
                self.gun.rect.x = int(self.gun.y)

    def attack(self):
        a = self.pazzle + [self.gun]
        if self.x > self.targ[0].x:
            if self.revers == 1:
                for i in range(len(a) - 1, -1, -1):
                    a[i].frames = [pygame.transform.flip(j, True, False) for j in a[i].frames]
                    if i != len(a) - 1 and i != len(a) - 2:
                        a[i].x = a[i + 1].x - 2 * a[i].sx
                        a[i].rect.x = int(a[i].x)
                    elif i == len(a) - 1:
                        a[i].x = a[-2].rect.center[0] - (a[i].rect.center[0] - a[-2].rect.center[0]) - a[i].image.get_width() // 2
                        a[i].rect.x = int(a[i].x)
                        a[i].y = a[-2].y - a[i].image.get_height() + a[i].sy
                        a[i].rect.y = int(a[i].y)
                self.revers = -1
        if self.x < self.targ[0].x:
            if self.revers == -1:
                for i in range(len(a) - 1, -1, -1):
                    a[i].frames = [pygame.transform.flip(j, True, False) for j in a[i].frames]
                    if i != len(a) - 1 and i != len(a) - 2:
                        a[i].x = a[i + 1].x + a[i].sx
                        a[i].rect.x = int(a[i].x)
                    elif i == len(a) - 1:
                        a[i].x = a[-2].x + a[i].sx
                        a[i].rect.x = int(a[i].x)
                        a[i].y = a[-2].y - a[i].image.get_height() + a[i].sy
                        a[i].rect.y = int(a[i].y)
                self.revers = 1
        if int(self.gun.cur_frame) == 0:
            snipeFire.play()
            self.pazzle[1].k = 1
            self.gun.k = 1
        if int(self.gun.cur_frame) == 1:
            rdmg = self.dmg
            if self.targ[1] == '0':
                rdmg *= 5
            self.targ[0].hp -= rdmg / 8.4999
            self.targ[0].pazzle[int(self.targ[1])].hp -= rdmg / 8.4999
        if self.targ[0].targ == '':
            self.targ[0].targ = self, 1

    def dead(self):
        self.tipe = ''
        MAP[int(self.yp)][int(self.xp)] = 0
        #DEAD.append(Death(load_image('')))
        del PERSES[PERSES.index(self)]
        for i in self.pazzle:
            persF.remove(i)
            gun.remove(self.gun)


class EnemyShild(Enemy):
    def __init__(self, stats, pazzle, t, x, y, shild):
        super().__init__(stats, pazzle, t, x, y)
        self.shild = shild
        self.shild.x = self.pazzle[-1].x + self.shild.sx
        self.shild.rect.x = int(self.shild.x)
        self.shild.y = self.pazzle[-1].y - self.shild.image.get_height() + self.shild.sy
        self.shild.rect.y = int(self.shild.y)

    def update(self):
        super().update()
        for i in self.pazzle + [self.shild]:
            i.rect.x = int(i.x) - ZX
        if self.targ != '':
            a = self.pazzle + [self.shild]
            if self.x > self.targ[0].x:
                if self.revers == 1:
                    for i in range(len(a) - 1, -1, -1):
                        a[i].frames = [pygame.transform.flip(j, True, False) for j in a[i].frames]
                        if i != len(a) - 1 and i != len(a) - 2:
                            a[i].x = a[i + 1].x - 2 * a[i].sx
                            a[i].rect.x = int(a[i].x)
                        elif i == len(a) - 1:
                            a[i].x = a[-2].rect.center[0] - (a[i].rect.center[0] - a[-2].rect.center[0]) - a[
                                i].image.get_width() // 2
                            a[i].rect.x = int(a[i].x)
                            a[i].y = a[-2].y - a[i].image.get_height() + a[i].sy
                            a[i].rect.y = int(a[i].y)
                        a[i].image = a[i].frames[int(a[i].cur_frame)]#
                    self.revers = -1
            if self.x < self.targ[0].x:
                if self.revers == -1:
                    for i in range(len(a) - 1, -1, -1):
                        a[i].frames = [pygame.transform.flip(j, True, False) for j in a[i].frames]
                        if i != len(a) - 1 and i != len(a) - 2:
                            a[i].x = a[i + 1].x + a[i].sx
                            a[i].rect.x = int(a[i].x)
                        elif i == len(a) - 1:
                            a[i].x = a[-2].x + a[i].sx
                            a[i].rect.x = int(a[i].x)
                            a[i].y = a[-2].y - a[i].image.get_height() + a[i].sy
                            a[i].rect.y = int(a[i].y)
                        a[i].image = a[i].frames[int(a[i].cur_frame)]
                    self.revers = 1
            if self.revers == 1:
                if self.xp != self.targ[0].xp - 1:
                    self.xtarg = self.targ[0].xp - 1
                else:
                    if int(self.shild.cur_frame) == 0:
                        self.attack()
            if self.revers == -1:
                if self.xp != self.targ[0].xp + 1:
                    self.xtarg = self.targ[0].xp + 1
                else:
                    if int(self.shild.cur_frame) == 0:
                        self.attack()
            if self.yp != self.targ[0].yp:
                self.ytarg = self.targ[0].yp
            if int(self.shild.cur_frame) == 10:
                self.targ[0].hp -= 15 / FPS
                if self.targ[0].hp <= 0:
                    self.targ[0].dead()
        self.shild.update()
        self.pazzle[1].update()
        self.moveS()

    def moveS(self):
        if int(self.y) != self.ytarg * 50 + 290:
            if int(self.y) > self.ytarg * 50 + 290:
                self.shild.y -= self.speed / FPS
                self.shild.rect.y = int(self.shild.y)
            if int(self.y) < self.ytarg * 50 + 290:
                self.shild.y += self.speed / FPS
                self.shild.rect.y = int(self.shild.y)
        if int(self.x) != self.xtarg * 100 + self.ytarg * 50:
            if int(self.x) > self.xtarg * 100 + self.ytarg * 50:
                self.shild.x -= self.speed / FPS
                self.shild.rect.x = int(self.shild.y)
            elif int(self.x) < self.xtarg * 100 + self.ytarg * 50:
                self.shild.x += self.speed / FPS
                self.shild.rect.x = int(self.shild.y)

    def dead(self):
        self.tipe = ''
        print('*DEAD*', self.tipe)
        print(int(self.pazzle[1].x), int(self.y - load_image('shildDead.png', 2).get_height()))
        DEAD.append(Death(self.rev(load_image('shildDead.png', 2)), 5, 1, int(self.pazzle[1].x - ZX), int(self.y - load_image('shildDead.png', 2).get_height()), deads, self.revers))
        for i in self.pazzle:
            persE.remove(i)
        shild.remove(self.shild)
        del ENEMIS[ENEMIS.index(self)]

    def attack(self):
        self.shild.k = 1
        self.pazzle[1].k = 1


class PersHead(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy, hp):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.mommy = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.sx = sx
        self.sy = sy
        self.hp = hp


class PersBody(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy, hp):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.mommy = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.sx = sx
        self.sy = sy
        self.hp = hp


class PersLegs(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, hp):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.mommy = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.hp = hp


class PersGun(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.mommy = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.sx = sx
        self.sy = sy


class PersShild(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy, hp):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.mommy = ''
        self.mask = pygame.mask.from_surface(self.image)
        self.sx = sx
        self.sy = sy
        self.hp = hp


class Background(pygame.sprite.Sprite):
    def __init__(self, image, b):
        super().__init__(b)
        self.image = image
        self.rect = self.image.get_rect()
        self.moveLeft = False
        self.moveRight = False
        self.rect.x = 0
        self.x = 0
        self.rect.y = 0

    def update(self):
        global ZX
        if self.moveLeft and self.x - 100 / FPS > - 1480:
            self.x -= 200 / FPS
            ZX += 100 / FPS
        if self.moveRight and self.x + 100 / FPS < 0:
            self.x += 200 / FPS
            ZX -= 100 / FPS
        self.rect.x = int(self.x)

    def move(self, event):
        if event.key == pygame.K_LEFT:
            self.moveRight = True
        elif event.key == pygame.K_RIGHT:
            self.moveLeft = True

    def notmove(self, event):
        if event.key == pygame.K_LEFT:
            self.moveRight = False
        elif event.key == pygame.K_RIGHT:
            self.moveLeft = False


class Death(AnimatedSprite):
    def __init__(self, sheet, columns, rows, x, y, group, r):
        super().__init__(sheet, columns, rows, x, y, group)
        self.r = r
        self.cur_frame = r
        self.k = r
        self.x = x + ZX

    def update(self):
        super().update()
        print(self.cur_frame)
        if int(self.cur_frame) == 0:
            self.image = self.frames[self.a()]
        self.rect.x = self.x - ZX

    def a(self):
        if self.r == -1:
            return 0
        else:
            return -1


def mapDraw():
    z = -170
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            pygame.draw.polygon(screen, chColor(MAP[i][j]),
                                [(j * 100 + z - int(ZX), 260 + 50 * i - poz(MAP[i][j])),
                                 ((j + 1) * 100 + z - int(ZX), 260 + 50 * i - poz(MAP[i][j])),
                                 (int((j + 1.5) * 100) + z - int(ZX), 260 + 50 * (i + 1) - poz(MAP[i][j])),
                                 (int((j + 0.5) * 100) + z - int(ZX), 260 + 50 * (i + 1) - poz(MAP[i][j]))],
                                dlin(MAP[i][j]))
        z += 50


def chColor(i):
    if i == 0:
        return pygame.Color('white')
    elif i == 1:
        return pygame.Color('red')
    elif i == 2:
        return pygame.Color('green')


def poz(i):
    if i == 0:
        return 0
    elif i == 1:
        return 2
    elif i == 2:
        return 2


def dlin(i):
    if i == 0:
        return 1
    elif i == 1 or i == 2:
        return 3


MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
back1 = Background(pygame.transform.scale(load_image('poleu.png', 1), (2440, 520)), background1)
clock = pygame.time.Clock()
running = True
First = FriendSniper([10, 1, 0, 0, 0, 40], [PersHead(load_image('head.png', 2), 8, 1, persF, '10', 4, 4, 10),
                                PersBody(load_image('body.png', 2), 11, 1, persF, '11', -2, 4, 10),
                                PersLegs(load_image('go.png', 2), 8, 1, persF, '12', 10)], '1', 0, 0,
             PersGun(load_image('firet.png', 2), 11, 1, gun, '13', -14, -4), 1)
Two = EnemyShild([10, 0, 0, 0, 0, 30], [PersHead(load_image('enemyHead.png', 2), 1, 1, persE, '20', 18, 22, 10),
                                     PersBody(load_image('enemyBody.png', 2), 12, 1, persE, '21', -10, 6, 10),
                                     PersLegs(load_image('enemyLegs.png', 2), 7, 1, persE, '22', 10)], '2', 11, 1,
              PersShild(load_image('shild.png', 2), 12, 1, shild, '24', 22, 30, 10))
PERSES = [First]
ENEMIS = [Two]
DEAD = []
back2 = Background(pygame.transform.scale(load_image('poled.png', 1), (2440, 520)), background2)
aimn = Arrow()
font = pygame.font.Font(None, 100)
text = font.render("START", 30, (73, 66, 61))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2
text_w = text.get_width()
text_h = text.get_height()
start = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
            if event.button == 1:
                if text_x - 10 < event.pos[0] < text_x + text_w + 10 and text_y - 10 < event.pos[1] < text_y + text_h + 10:
                    start = True
                    for i in range(len(PERSES)):
                        PERSES[i].xtarg = i // 3 + 3
                        PERSES[i].ytarg = 0 + i % 3
    background1.draw(screen)
    for i in PERSES + ENEMIS:
        i.update()
    persF.draw(screen)
    shild.draw(screen)
    gun.draw(screen)
    background2.draw(screen)
    if not start:
        pygame.draw.rect(screen, (48, 213, 200), (text_x - 10, text_y - 10,
                                                         text_w + 20, text_h + 10))
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, pygame.Color('black'), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 10), 3)
    pygame.draw.rect(screen, pygame.Color('black'), (0, 0, width, 100))
    pygame.draw.rect(screen, pygame.Color('black'), (0, height - 100, width, 100))
    clock.tick(FPS)
    pygame.display.flip()
    if all([i.xp == i.xtarg for i in PERSES] + [i.yp == i.ytarg for i in PERSES]) and start:
        break

a = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background1.draw(screen)
    for i in PERSES + ENEMIS:
        i.update()
    persF.draw(screen)
    gun.draw(screen)
    shild.draw(screen)
    background2.draw(screen)
    pygame.draw.rect(screen, pygame.Color('black'), (0, 0, width, a))
    pygame.draw.rect(screen, pygame.Color('black'), (0, height - a, width, a))
    a -= 100 / FPS
    if int(a) == 0:
        break
    clock.tick(FPS)
    pygame.display.flip()

x, y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            back1.move(event)
            back2.move(event)
            if event.key == pygame.K_a:
                aimn.f = True
        if event.type == pygame.KEYUP:
            back1.notmove(event)
            back2.notmove(event)
            if event.key == pygame.K_a:
                aimn.f = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                aimn.action()
    if pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
        aimn.rect.x = x
        aimn.rect.y = y
    back1.update()
    back2.update()
    aimn.opr()
    background1.draw(screen)
    aimn.update()
    mapDraw()
    persF.draw(screen)
    persE.draw(screen)
    MAP = [[0 for i in range(20)] for i in range(3)]
    for i in PERSES + ENEMIS:
        i.update()
    deads.draw(screen)
    for i in DEAD:
        i.update()
    shild.draw(screen)
    gun.draw(screen)
    background2.draw(screen)
    Heads.draw(screen)
    aim.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
