
import pygame
import time
import random

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inicialización de la ventana y el reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Función para dibujar la serpiente
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Función para generar una nueva posición para la comida
def generate_food():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Función principal del juego
def game():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = (1, 0)
    food = generate_food()
    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)
                elif event.key == pygame.K_SPACE:  # Pausar y reanudar el juego con la tecla de espacio
                    paused = not paused

        if paused:
            continue  # Si el juego está en pausa, no actualizamos la serpiente ni el juego

        snake_head = (snake[-1][0] + snake_direction[0], snake[-1][1] + snake_direction[1])

        if snake_head == food:
            food = generate_food()
        else:
            snake.pop(0)

        if snake_head in snake[:-1]:
            return

        snake.append(snake_head)

        screen.fill(WHITE)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    game()


