import pygame
import math

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Inicialización de la ventana y el reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Holographic Window')
clock = pygame.time.Clock()

# Función para dibujar una línea con efecto holográfico y mostrar un mensaje en pantalla
def draw_hologram_line(screen, color, start_pos, end_pos, message):
    distance = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
    angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
    for i in range(int(distance)):
        x = int(start_pos[0] + i * math.cos(angle))
        y = int(start_pos[1] + i * math.sin(angle))
        pygame.draw.circle(screen, color, (x, y), 1)

    # Mostrar el mensaje en pantalla
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(text, text_rect)

# Función principal del juego
def hologram():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()
        draw_hologram_line(screen, BLUE, (WIDTH // 2, HEIGHT // 2), mouse_pos, "Hola, soy un holograma")
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    hologram()
