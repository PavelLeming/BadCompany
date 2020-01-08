import math, pygame, os

TG = {0.0: 0, 0.1: 6, 0.2: 11, 0.3: 17, 0.4: 22, 0.5: 27, 0.6: 31, 0.7: 35, 0.8: 39, 0.9: 42,
      1.0: 45, 1.1: 48, 1.2: 50, 1.4: 55, 1.5: 56, 1.6: 58, 1.7: 60, 1.8: 61, 1.9: 63, 2.0: 64,
      2.1: 65, 2.2: 66, 2.3: 67, 2.4: 68, 2.6: 69, 2.7: 70, 2.9: 71, 3.0: 72, 3.2: 73, 3.4: 74,
      3.7: 75, 4.0: 76, 4.3: 77, 4.7: 78, 5.1: 79, 5.6: 60, 6.3: 81, 7.1: 82, 8.1: 83, 9.5: 84,
      11.4: 85, 14.3: 86, 19.0: 87, 28.6: 88, 57.2: 89}
TGMX = {-57.2: 91, -28.6: 92, -19.0: 93, -14.3: 94, -11.4: 95, -9.5: 96, -8.1: 97, -7.1: 98,
        -6.3: 99, -5.6: 100, -5.1: 101, -4.7: 102, -4.3: 103, -4.0: 104, -3.7: 105, -3.4: 106,
        -3.2: 107, -3.0: 108,-2.9: 109, -2.7: 110, -2.6: 111,-2.4: 112, -2.3: 113, -2.2: 114,
        -2.1: 115, -2.0: 116, -1.9: 117, -1.8: 119, -1.7: 120, -1.6: 122, -1.5: 123, -1.4: 125,
        -1.3: 127, -1.2: 130, -1.1: 132, -1.0: 135, -0.9: 138, -0.8: 141, -0.7: 145, -0.6: 150,
        -0.5: 155, -0.4: 160, -0.3: 165, -0.2: 170, -0.1: 175}
TGMM = {0.0: 180, 0.1: 185, 0.2: 190, 0.3: 195, 0.4: 200, 0.5: 205, 0.6: 210, 0.7: 215, 0.8: 220,
        0.9: 222, 1.0: 225, 1.1: 228, 1.2: 230, 1.3: 232, 1.4: 235, 1.5: 236, 1.6: 238, 1.7: 240,
        1.8: 241, 1.9: 242, 2.0: 244, 2.1: 245, 2.2: 246, 2.3: 247, 2.4: 248, 2.6: 249, 2.7: 250,
        2.9: 251, 3.0: 253, 3.2: 253, 3.4: 254, 3.7: 255, 4.0: 256, 4.3: 257, 4.7: 258, 5.1: 257,
        5.6: 260, 6.3: 261, 7.1: 262, 8.1: 263, 9.5: 264, 11.4: 265, 14.3: 266, 19.0: 267,
        28.6: 268, 57.2: 269}
TGMY = {-57.2: 271, -28.6: 272, -19.0: 273, -14.3: 274, -11.4: 275, -9.5: 276, -8.1: 277, -7.1: 278,
        -6.3: 279, -5.6: 280, -5.1: 281, -4.7: 282, -4.3: 283, -4.0: 284, -3.7: 285, -3.4: 286,
        -3.2: 287, -3.0: 288, -2.9: 289, -2.7: 290, -2.6: 291, -2.4: 292, -2.3: 293, -2.2: 294,
        -2.1: 295, -2.0: 296, -1.9: 297, -1.8: 299, -1.7: 300, -1.6: 302, -1.5: 303, -1.4: 305,
        -1.3: 307, -1.2: 310, -1.1: 312, -1.0: 315, -0.9: 318, -0.8: 321, -0.7: 325, -0.6: 330,
        -0.5: 335, -0.4: 340, -0.3: 345, -0.2: 350, -0.1: 355, -0.0: 360}

pygame.init()
size = width, height = 960, 520
screen = pygame.display.set_mode(size)
background1 = pygame.sprite.Group()
background2 = pygame.sprite.Group()
choose = pygame.sprite.Group()
friend = pygame.sprite.Group()
pers = pygame.sprite.Group()
aim = pygame.sprite.Group()
all_sprites = [pers, choose]
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


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


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
        if int(self.cur_frame) != 0:
            self.cur_frame = (self.cur_frame + 7 / FPS * self.k) % len(self.frames)
            self.image = self.frames[int(self.cur_frame)]
        else:
            self.k = 0


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(aim)
        self.image = load_image('aim.png', 1 / 24)
        self.rect = pygame.Rect(0, 0, self.image.get_width() * 0.3, self.image.get_height() * 0.3)
        self.y = (self.rect.x - 260) // 50
        self.x = 0
        self.tipe = 0
        self.f = False

    def opr(self):
        if pygame.sprite.spritecollideany(self, pers) and not self.f:
            self.image = load_image('aimFriend.png', 1 / 16)
        elif self.f and any(i.activ == 1 for i in PERSES):
            self.image = load_image('aimTarg.png', 1 / 32)
            self.rect.x -= self.image.get_width() // 2
            self.rect.y -= self.image.get_height() // 2
        else:
            self.image = load_image('aim.png', 1 / 24)

    def update(self):
        self.y = (self.rect.y - 260) // 50
        self.x = (self.rect.x - (self.rect.y - 260) + 70) // 100
        if 0 <= self.y <= 2 and 0 <= self.x < len(MAP[0]):
            MAP[self.y][self.x] = 2

    def action(self):
        if pygame.sprite.spritecollideany(self, pers) and not self.f:
            PERSES[
                [str(i) for i in PERSES].index(pygame.sprite.spritecollide(self, pers, False)[0].tipe[0])].activ *= -1
        if not self.f and any(i.activ == 1 for i in PERSES) \
                and not self.f and any(i.activ == 1 for i in PERSES):
            if 0 <= self.y <= 2 and 0 <= self.x <= len(MAP[0]):
                for i in PERSES:
                    if i.activ == 1:
                        i.ytarg = (self.rect.y - 260) // 50
                        i.xtarg = (self.rect.x - (self.rect.y - 260) + 70) // 100
        elif self.f and any(i.activ == 1 for i in PERSES):
            if pygame.sprite.spritecollideany(self, pers):
                PERSES[[i.activ for i in PERSES].index(True)].targ \
                    = pygame.sprite.spritecollideany(self, pers).tipe


class Pers:
    def __init__(self, stats, pazzle, t, x, y, gun=None):
        self.hp = stats[0]
        self.dmg = stats[1]
        self.armor = stats[2]
        self.dodge = stats[3]
        self.aim = stats[4]
        self.speed = stats[5]
        self.pazzle = pazzle
        self.dk = 1
        self.tipe = t
        self.targ = '0'
        self.gun = gun
        self.activ = -1
        self.y = y * 50 + 290
        self.x = x * 100 + y * 50
        self.pazzle[-1].x = self.x - self.pazzle[-1].image.get_width() // 2
        self.pazzle[-1].y = self.y - self.pazzle[-1].image.get_height()
        self.pazzle[-1].rect.x = int(self.pazzle[-1].x)
        self.pazzle[-1].rect.y = int(self.pazzle[-1].y)
        self.xp = x
        self.yp = y
        self.xtarg = x
        self.ytarg = y
        self.spx = 0
        self.sp = 0
        self.a = 1 / 180
        self.r = 0
        for i in range(len(self.pazzle[:-1]) - 1, -1, -1):
            self.pazzle[i].x = self.pazzle[i + 1].x + self.pazzle[i].sx
            self.pazzle[i].rect.x = int(self.pazzle[i].x)
            self.pazzle[i].y = self.pazzle[i + 1].y - self.pazzle[i].image.get_width() + self.pazzle[i].sy
            self.pazzle[i].rect.y = int(self.pazzle[i].y)
        if self.gun is not None:
            self.gun.x = self.pazzle[-1].x + self.gun.sx
            self.gun.rect.x = int(self.gun.x)
            self.gun.y = self.pazzle[-1].y - self.gun.image.get_width() + self.gun.sy
            self.gun.rect.y = int(self.gun.y)

    def __str__(self):
        return self.tipe

    def update(self):
        MAP[int(self.yp)][int(self.xp)] = int(self.tipe)
        if int(self.x) != self.xtarg * 100 + self.ytarg * 50:
            if int(self.x) > self.xtarg * 100 + self.ytarg * 50:
                for i in self.pazzle + [self]:
                    i.x -= self.speed / FPS
                    if int(self.pazzle[-1].cur_frame) == 0:
                        self.pazzle[-1].cur_frame = -1
                        self.pazzle[-1].k = -0.85
                    if i != self:
                        i.rect.x = int(i.x)
            elif int(self.x) < self.xtarg * 100 + self.ytarg * 50:
                for i in self.pazzle + [self]:
                    i.x += self.speed / FPS
                    if int(self.pazzle[-1].cur_frame) == 0:
                        self.pazzle[-1].cur_frame = 1
                        self.pazzle[-1].k = 0.9
                    if i != self:
                        i.rect.x = int(i.x)
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
        if int(self.pazzle[0].cur_frame) == 0:
            self.pazzle[0].cur_frame = 1
            self.pazzle[0].k = 1
        self.pazzle[0].update()
        self.pazzle[-1].update()
        for i in range(len(self.pazzle[:-1]) - 1, -1, -1):
            self.pazzle[i].x = self.pazzle[i + 1].x + self.pazzle[i].sx
            if i == 0:
                self.pazzle[i].x -= self.spx
            self.pazzle[i].rect.x = int(self.pazzle[i].x)
            self.pazzle[i].rect.y = self.pazzle[i + 1].rect.y - self.pazzle[i].image.get_width() + self.pazzle[i].sy
        if self.gun is not None:
            self.gun.x = self.pazzle[-1].x + self.gun.sx
            self.gun.rect.x = int(self.gun.x)
            self.gun.y = self.pazzle[-1].y - self.gun.image.get_width() + self.gun.sy
            self.gun.rect.y = int(self.gun.y)
        self.yp = (self.y - 290) // 50
        self.xp = (self.x - self.yp * 50) // 100
        if self.targ != '0':
            if int(self.gun.cur_frame) == 0:
                self.pazzle[1].k = 1
                self.pazzle[1].cur_frame = 1
                self.gun.k = 1
                self.gun.cur_frame = 1
                self.sp = 12 / 60
                self.spx = 0
                rdmg = self.dmg
                if self.targ[1] == '0':
                    rdmg *= 5
                PERSES[[str(i) for i in PERSES].index(self.targ[0])].hp -= rdmg
            self.gun.update()
            self.sp -= self.a
            self.spx += self.sp
            self.pazzle[1].update()
            self.r += 2
            oldc = self.gun.rect.center
            if self.gun.rect.center[0] < PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[0]:
                if self.gun.rect.center[1] < PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1]:
                    self.gun.image = pygame.transform.rotate(self.gun.image,
                                                             -TG[round((PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1] - self.gun.rect.center[1])
                                                                       / (PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[0] - self.gun.rect.center[0]), 1)])
                if self.gun.rect.center[1] > PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1]:
                    self.gun.image = pygame.transform.rotate(self.gun.image,
                                                             -TGMY[round((PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1] - self.gun.rect.center[1])
                                                                       / (PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[0] - self.gun.rect.center[0]), 1)])
            self.gun.rect = self.gun.image.get_rect()
            self.gun.rect.center = oldc


class PersShild(Pers):
    def __init__(self, stats, pazzle, t, x, y):
        super().__init__(stats, pazzle, t, x, y)


class PersHead(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.sx = sx
        self.sy = sy


class PersBody(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.sx = sx
        self.sy = sy


class PersLegs(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t


class PersGun(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.rect = self.image.get_rect()
        self.sx = sx
        self.sy = sy


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
            self.x -= 100 / FPS
            ZX += 50 / FPS
        if self.moveRight and self.x + 100 / FPS < 0:
            self.x += 100 / FPS
            ZX -= 50 / FPS
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


def mapDraw():
    z = -70
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
    elif i == 1:
        return 3
    elif i == 2:
        return 3


MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
back1 = Background(pygame.transform.scale(load_image('poleu.png', 1), (2440, 520)), background1)
clock = pygame.time.Clock()
camera = Camera()
running = True
ev = False
First = Pers([10, 1, 0, 0, 0, 50], [PersHead(load_image('head.png', 2), 8, 1, pers, '10', 4, 10),
                                PersBody(load_image('body.png', 2), 11, 1, pers, '11', -2, 4),
                                PersLegs(load_image('go.png', 2), 8, 1, pers, '12')], '1', 1, 0,
             PersGun(load_image('firet.png', 2), 11, 1, pers, '1', -12, 42))
Enemy = PersShild([10, 0, 0, 0, 0, 10], [PersHead(load_image('enemyHead.png', 2), 1, 1, pers, '20', 38, 16),
                                     PersBody(load_image('enemyBody.png', 2), 12, 1, pers, '21', -32, 26),
                                     PersLegs(load_image('enemyLegs.png', 2), 7, 1, pers, '22')], '2', 6, 1)
PERSES = [First, Enemy]
back2 = Background(pygame.transform.scale(load_image('poled.png', 1), (2440, 520)), background2)
aimn = Arrow()
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
    [i.update() for i in PERSES]
    aimn.opr()
    background1.draw(screen)
    aimn.update()
    mapDraw()
    pers.draw(screen)
    MAP = [[0 for i in range(30)] for i in range(3)]
    background2.draw(screen)
    aim.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
