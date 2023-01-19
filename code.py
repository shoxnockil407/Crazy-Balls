import sys as s
import pygame
import os
from random import randint
import time
'''импорт библиотек'''


'''cпециальный класс для таймера'''


class Timer:

    def __init__(self):
        self._start_time = None
        self.pause_time = 0
        self.directory = 0
        self.timer_bonus = randint(20, 35)

    def start(self):
        """Запуск нового таймера"""

        self._start_time = time.perf_counter()

    def return_time(self):
        """Возврат времени"""

        return str(int(300 - time.perf_counter() + self.timer_bonus))


t = Timer()

'''инициализация игры и создания нужных переменных для игры'''
pygame.init()
pygame.display.set_caption('Поймай меня, если сможешь')
size = w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
r = 70
count_p = 0
rr = r
running = True
clock = pygame.time.Clock()
fps = 1
score = 0
level = 1
x = randint(0, 800)
y = randint(0, 600)
a = 1000
flag_game_over = False
start_green = 0
flag = False
count_tick = 0
mines = 1
fl = False
flag_red = False
fl1 = False
fl2 = False
fr = 1
xx = yy = 0
flag_time = 0
yellow_score = 2
sc = screen

'''фунция для завершающего интро'''


def tablet_game(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render(f'Your final score: {score} .'
                       f'Your final level: {level}.', True, (255, 240, 110))

    text_x = w // 2 - text.get_width() // 2
    text_y = h // 2 - text.get_height() // 2

    screen.blit(text, (text_x, text_y))



'''функция для загрузок нужных изображений'''


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        s.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
img = sprite.image = load_image('arrow.png')
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)

sprite.rect.x = 5
sprite.rect.y = 20


'''функция для отображения данных игры во время игрового процесса'''


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render(f'Score: {score}', True, (198, 105, 50))

    text_x = w // 7 - text.get_width() // 2
    text_y = h // 7 - text.get_height() // 2

    screen.blit(text, (text_x, text_y))

    text1 = font.render(f'Level: {level}', True, (1, 251, 160, 109))

    text_x1 = w // 7 - text.get_width() // 2
    text_y1 = (h // 10 - text.get_height() // 2) - 2

    screen.blit(text1, (text_x1, text_y1))

    if count_p % 2 == 0:
        sms = 'OFF'
        times = t.return_time()
    else:
        sms = 'ON'
        times = t.return_time()

    text2 = font.render(f'Pause: {sms}', True, (pygame.Color('Pink')))

    text_x2 = w // 7 - text.get_width() // 2
    text_y2 = (h // 2 - text.get_height() // 2) - h // 3 - w // 15

    screen.blit(text2, (text_x2, text_y2))

    text3 = font.render(f'Time: {times}', True, ((140, 10, 99, 255)))

    text_x3 = w // 7 - text.get_width() // 2
    text_y3 = (h // 2 - text.get_height() // 2) - h // 9 - w // 9

    screen.blit(text3, (text_x3, text_y3))


FPS = 50


'''фунция для завершения игры'''


def terminate():
    pygame.quit()
    s.exit()


'''фунцкия для создания приветствующего интро'''


def start_screen():
    intro_text = ["Добро пожаловать!", "",
                  "Правила игры:",
                  "Правило одно - поймать шарики, пока есть время!",
                  "",
                  "Управление:",
                  "Колесо мыши - пауза",
                  'Зажать Escape - exit',
                  "Клик мышкой - попытка попасть в шарик",
                  "",
                  "Вам нужно ловить постоянно бегающие шарики!",
                  "Будьте внимательны, когда кликаете по шарикам",
                  "Речь идет жёлтом шарике!",
                  "Удачи, салага;)"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (w, h))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            global flag_time
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                flag_time = 1
                return
        pygame.display.flip()
        clock.tick(FPS)


'''запуск игрового цикла'''

start_screen()
pygame.mixer.music.load('data/fon_music.mp3')
pygame.mixer.music.play(-1)
total = pygame.mixer.Sound('data/total.ogg')
if flag_time == 1:
    t.start()
while running:
    sc.fill((0, 0, 0))
    time_of_game = int(t.return_time())
    if time_of_game <= 0:
        flag_game_over = True
        running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        terminate()

    flag_tick = False
    count_tick += 1
    if level != 1 and count_tick % 2 == 0:
        flag_tick = True
        xx, yy = randint(0, 800), randint(0, 600)
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if score == 10:
                r -= 10
                rr += 2
                level = 2
                flag = True
                mines = 2
                x1 = randint(0, 800)
                y1 = randint(0, 600)
            if score >= 25 and fl1 is False:
                yellow_score += 2
                level = 3
                mines = 3
                r -= 10
                rr += 1
                start_green = 1
                x3, y3 = randint(0, 800), randint(0, 600)
                fl1 = True
            if score >= 50 and fl2 is False:
                level = 4
                yellow_score += 3
                mines = 5
                fl2 = True
                r -= 5
                a = score
            if score >= a * 2:
                rr += 1
                mines = 5 + level * 2
                level += 1
                yellow_score += 5
                if level >= 8:
                    fps = 2
                a = score
                if r != 25:
                    r -= 5
                else:
                    r = 24
            vx, vy = event.pos[0], event.pos[1]
            if count_p % 2 == 0:
                if fr == 1:
                    if vx in range(x - r, x + r) and vy in range(y - r, y + r):
                        score += 1
                        total.play()
                if flag is True:
                    if vx in range(x1 - r, x1 + r) and vy in range(y1 - r, y1 + r):
                        score += 3
                        total.play()
                if start_green != 0:
                    if vx in range(x3 - r, x3 + r) and vy in range(y3 - r, y3 + r):
                        score += 5
                        total.play()
                if vx in range(xx - r, xx + r) and vy in range(yy - r, yy + r):
                    score -= yellow_score
                    total.play()
        if event.type == pygame.MOUSEWHEEL:
            count_p += 1
    draw(screen)
    x = randint(0, 800)
    y = randint(0, 600)
    if fr == 1:
        pygame.draw.circle(screen, pygame.Color('Red'), (x, y), radius=r)
    if flag is True and count_p % 2 == 0:
        x1 = randint(0, 800)
        y1 = randint(0, 600)
    if flag is True:
        pygame.draw.circle(screen, pygame.Color('Blue'), (x1, y1), radius=r - 3)
    if start_green != 0 and count_p % 2 == 0:
        x3 = randint(0, 800)
        y3 = randint(0, 600)
    if start_green != 0:
        pygame.draw.circle(screen, pygame.Color('Green'), (x3, y3), radius=r - 5)
    if flag_tick is True:
        xx = randint(0, 800)
        yy = randint(0, 600)
    if flag_tick is True and count_p % 2 == 0:
        pygame.draw.circle(screen, pygame.Color('Yellow'), (xx, yy), radius=rr)
    pygame.display.flip()
    clock.tick(fps)

pygame.mixer.music.stop()
game_over_sound = pygame.mixer.Sound('data/game_is_over.ogg')
game_over_sound.play(-1)
while True:
    if int(t.return_time()) < -8:
        terminate()
        break
    tablet_game(screen=screen)
    pygame.display.flip()
    clock.tick(fps)
