import pygame
import time
import random
import os
import threading
import urllib.request
import cv2

pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLOCK_SIZE = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
SNAKE_SPEED = 15

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

class AdManager(threading.Thread):
    def __init__(self, url, extension):
        super().__init__()
        self.url = url
        self.extension = extension
        self.new_file_name = ""

    def download_ad(self):
        file_name, _ = urllib.request.urlretrieve(self.url)
        base = os.path.splitext(file_name)[0]
        self.new_file_name = base + self.extension
        os.rename(file_name, self.new_file_name)

    def display_ad(self):
        image_ad = cv2.imread(self.new_file_name)
        if image_ad is None:
            print("Error: Could not load image.")
            return
        image_ad = cv2.resize(image_ad, (300, 300))
        cv2.namedWindow("Advertisement", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Advertisement", cv2.WND_PROP_TOPMOST, 1)
        cv2.resizeWindow("Advertisement", 300, 300)
        while True:
            cv2.imshow("Advertisement", image_ad)
            key = cv2.waitKey(1000)
            if key == 27:
                break
        cv2.destroyAllWindows()

    def run(self):
        self.download_ad()
        self.display_ad()

def game_loop():
    game_over = False
    game_close = False
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            font = pygame.font.SysFont(None, 35)
            message = font.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(message, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        draw_snake(BLOCK_SIZE, snake_list)
        pygame.display.update()
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1
        clock.tick(SNAKE_SPEED)
    pygame.quit()
    quit()

ad_manager = AdManager("http://d.wpimg.pl/1098145671--204938399/movies.jpg", ".jpg")
ad_manager.start()

game_loop()

ad_manager.join()

