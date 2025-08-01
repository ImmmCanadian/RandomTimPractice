import pygame, random, math, sys, time
pygame.init()

WIDTH,HEIGHT=800,600
win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT= 500
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 50

label_font = pygame.font.SysFont("comicsans", 24)

class Target():
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR="RED"
    COLOR2="WHITE"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow=False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    
    def draw(self, window):
        pygame.draw.circle(window, self.COLOR2, (self.x, self.y), self.size)
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.size*0.8)
        pygame.draw.circle(window, self.COLOR2, (self.x, self.y), self.size*0.6)
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.size*0.4)
    
    def collide(self, mouse_x, mouse_y):
        distance = math.sqrt(((self.x - mouse_x)**2)+((self.y-mouse_y)**2))
        return distance < self.size
    
def draw(window,targets):
    window.fill("black")

    for target in targets:
        target.draw(window)

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top_bar(window, elasped_time, hits, misses, LIVES):
    pygame.draw.rect(window, "gray", (0,0, WIDTH, 50))
    time_label = label_font.render(f"{format_time(elasped_time)}",1,"black")

    speed = round(hits / elasped_time, 1)
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "black")

    hits_label = label_font.render(f"Hits: {hits}", 1, "black")

    lives_label = label_font.render(f"Lives: {LIVES - misses}", 1, "black")

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))

def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill("black")
    time_label = label_font.render(
        f"Time: {format_time(elapsed_time)}", 1, "white")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "white")

    hits_label = label_font.render(f"Hits: {targets_pressed}", 1, "white")

    accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = label_font.render(f"Accuracy: {accuracy}%", 1, "white")

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()


def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2


def main():
    run = True
    targets=[]
    clock= pygame.time.Clock()
    start_time = time.time()
    misses=0
    LIVES=10
    clicks=0
    hits=0
    

    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT)

    while run:
        clock.tick(60)
        click=False
        
        mouse_pos = pygame.mouse.get_pos()
        elasped_time=time.time()-start_time

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False 
                break
            if event.type==TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y= random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicks += 1
                click=True

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
                LIVES -= 1

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                hits += 1
        
        if LIVES <= 0:
            end_screen(win, elasped_time, hits, clicks)

        draw(win,targets)
        draw_top_bar(win,elasped_time, hits, misses, LIVES)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()






