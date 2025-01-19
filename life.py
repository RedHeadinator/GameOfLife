import pygame
import helper as hp

def main():
    res = (700, 700)
    SCREEN = pygame.display.set_mode(res)
    running = True
    clock = pygame.time.Clock()
    size = res[0] / 70
    
    # Load initial state
    table = hp.read('starts/pulsar')
    length = len(table[0])
    old = table
    
    while running:
        SCREEN.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Game logic
        new = hp.zeros(length)

        for i in range(length):
            for j in range(length):
                neighs = hp.neighbors(old, (j, i), length)

                if neighs <= 1:
                    new[i][j] = 0
                elif neighs >= 4:
                    new[i][j] = 0
                elif old[i][j] == 1:
                    new[i][j] = 1
                else:
                    if neighs == 3:
                        new[i][j] = 1
        # Display start
        for i in range(length):
            for j in range(length):
                if new[i][j] == 1:
                    pygame.draw.rect(SCREEN, 'white', (j * size, i * size, size, size))
        
        old = new
        pygame.display.flip()
        clock.tick(10)


main()