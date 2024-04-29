import pygame
import sys
import os

WIDTH, HEIGHT = 300, 300
ROWS, COLS = 3, 3
TILE_SIZE = WIDTH // COLS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Taquin 3x3")

pieces = []
for i in range(1, ROWS * COLS):
    img = pygame.image.load(os.path.join(f'{i}.png')).convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    pieces.append(img)
pieces.append(pygame.Surface((TILE_SIZE, TILE_SIZE)))

piece_coords = [(x * TILE_SIZE, y * TILE_SIZE) for y in range(ROWS) for x in range(COLS)]

def swap_pieces(empty_pos, piece_pos):
    piece_coords[empty_pos], piece_coords[piece_pos] = piece_coords[piece_pos], piece_coords[empty_pos]

def main():
    empty_index = ROWS * COLS - 1

    running = True
    while running:
        screen.fill((255, 255, 255))

        for i, (x, y) in enumerate(piece_coords):
            screen.blit(pieces[i], (x, y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and empty_index + COLS < ROWS * COLS:
                    swap_pieces(empty_index, empty_index + COLS)
                    empty_index += COLS
                elif event.key == pygame.K_DOWN and empty_index - COLS >= 0:
                    swap_pieces(empty_index, empty_index - COLS)
                    empty_index -= COLS
                elif event.key == pygame.K_LEFT and (empty_index + 1) % COLS != 0:
                    swap_pieces(empty_index, empty_index + 1)
                    empty_index += 1
                elif event.key == pygame.K_RIGHT and (empty_index % COLS) != 0:
                    swap_pieces(empty_index, empty_index - 1)
                    empty_index -= 1

if __name__ == "__main__":
    main()

