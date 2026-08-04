# Sudoku Final Group Projecthttps://github.com/JuanDL2806/Sudoku-Final-Project/tree/main
import pygame
#import Board
import random

def main():
    global res, rest, ex, ext, board #my buttons on game screen
    global val
    try:
        height = 560
        width = 504
        pygame.init()
        pygame.font.init() #I think the doc said this is done auto in ln 12
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Sudoku")
        my_font = pygame.font.SysFont(None, 48)
        subtitle = pygame.font.SysFont(None, 30)
        result = pygame.font.SysFont(None, 58)
        mini = pygame.font.SysFont(None, 18)

        running = True
        game_start = False #THIS IS USED FOR determining what pane to show
        end_scrn = False

        startscrn(screen,subtitle, my_font, mini)
        pygame.display.flip()
        while running:
            #width=0, border_radius=0, border_top_left_radius=-1,
            # border_top_right_radius=-1, border_bottom_left_radius=-1,
            # border_bottom_right_radius=-1)

            for event in pygame.event.get():

               if event.type == pygame.QUIT:
                    running = False
               elif not game_start and not end_scrn and event.type == pygame.MOUSEBUTTONDOWN:
                   easy, medium, hard = startscrn(screen,subtitle, my_font, mini)
                   x, y = event.pos[0], event.pos[1]
                   if easy.collidepoint(x, y):
                       game_start = True
                       board = Board(width, height, screen, "easy")
                       screen.fill("light blue")
                       board.draw()
                       res, rest, ex = draw_options(screen)
                   elif medium.collidepoint(x, y):
                       game_start = True
                       board = Board(width, height, screen, "medium")
                       screen.fill("light blue")
                       board.draw()
                       res, rest, ex = draw_options(screen)
                   elif hard.collidepoint(x, y):
                       game_start = True
                       board = Board(width, height, screen, "hard")
                       screen.fill("light blue")
                       board.draw()
                       res, rest, ex = draw_options(screen)
               elif game_start and event.type == pygame.MOUSEBUTTONDOWN:
                   x, y = event.pos[0], event.pos[1]
                   if board.is_full():
                       game_start, end_scrn = False, True
                       if board.check_board():
                           screen.fill("gold")
                           screen.blit(result.render("YOU WIN!!!", True, "black"), (200, 200))
                           ext = makeButton(screen, "Exit", mini,(260, 400, 100, 40))
                       else:
                           screen.fill("tomato1")
                           screen.blit(result.render("Game Over :(", True, "black"), (200, 200))
                           rest = makeButton(screen, "Restart", mini,(260, 400, 100, 40))
                   elif board.click(x,y)!=None:
                       board.select(board.click(x,y)[0], board.click(x,y)[1])
                       board.draw()
                   else:
                       x, y = event.pos[0], event.pos[1]
                       if res.collidepoint(x,y):
                           board.clear()
                       elif rest.collidepoint(x,y):
                           game_start=False
                           startscrn(screen, subtitle, my_font, mini)
                       elif ex.collidepoint(x,y):
                           pygame.quit()
                #THIS MAY BE UNNECESSARY
                   if game_start:
                        screen.fill("light blue")
                        board.draw()
                        draw_options(screen)
               elif game_start and event.type == pygame.KEYDOWN and board.current()!=(None,None):
                   #print(pygame.key.name(event.key))
                   if event.key==pygame.K_UP and board.current()[0]>0:
                       board.select(board.current()[0]-1,board.current()[1])
                   elif event.key == pygame.K_DOWN and board.current()[0]<8:
                       board.select(board.current()[0]+1,board.current()[1])
                   elif event.key == pygame.K_LEFT and board.current()[1]>0:
                       board.select(board.current()[0],board.current()[1]-1)
                   elif event.key==pygame.K_RIGHT and board.current()[1]<8:
                       board.select(board.current()[0],board.current()[1]+1)
                   elif pygame.K_0 < event.key <= pygame.K_9:
                       val = event.key - pygame.K_0
                       board.sketch(val)
                       #board.draw()
                       #next we would need to handle number and enter keys, else no nothing
                   elif event.key == pygame.K_RETURN:
                       board.select(board.current()[0], board.current()[1])
                       board.place_number(board.curVal())
                   elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                       board.select(board.current()[0], board.current()[1])
                       board.place_number(0)
                       board.sketch(0)
                   else:
                       pass
                   screen.fill("light blue")
                   board.draw()
                   draw_options(screen)
               elif end_scrn:
                   x, y = event.pos[0], event.pos[1]
                   if board.check_board():
                       if ext.collidepoint(x, y):
                           pygame.quit()
                   else:
                       if rest.collidepoint(x,y):
                           game_start, end_scrn = False, False
                           startscrn(screen, subtitle, my_font, mini)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

def draw_options(screen):
    #draw vert lines
    mini = pygame.font.SysFont(None, 18)
    gameRes = makeButton(screen, "RESET", mini, (50, 500,100, 40))
    gameRestart = makeButton(screen, "RESTART", mini, (200, 500,100, 40))
    gameQuit = makeButton(screen, "EXIT", mini, (350, 500,100, 40))
    return gameRes, gameRestart, gameQuit

def startscrn(screen,subtitle, my_font, mini):
    screen.fill("light green")
    screen.blit(subtitle.render("Welcome to...", True, "black"), (200, 50))
    screen.blit(my_font.render("SUDOKU!!", True, "black"), (180, 100))
    screen.blit(subtitle.render("Select game mode", True, "black"), (170, 210))
    easy = makeButton(screen, "EASY", mini, (50, 275, 100, 40))
    medium = makeButton(screen, "MEDIUM", mini, (200, 275, 100, 40))
    hard = makeButton(screen, "HARD", mini, (350, 275, 100, 40))
    return easy, medium, hard

def makeButton(screen, text, font, tple):
    RestSrf = font.render(text, True, "black")
    restartGO = pygame.Rect(tple)
    RestRect = RestSrf.get_rect()
    RestRect.center = restartGO.center
    pygame.draw.rect(screen, "white", restartGO)
    screen.blit(RestSrf, RestRect)
    return restartGO

def generate_sudoku(size, removed):
    board = None
    #fill in above
    return board

class cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.skValue = 0
        self.font = pygame.font.SysFont(None, 40)
        self.sketchf = pygame.font.SysFont(None, 25)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.skValue = value
        #made by me
    def get_sketched_value(self):
        return self.skValue
    #above was not mentioned

    def draw(self):
        if self.value!=None and 9>=self.value>0:
            self.screen.blit(self.font.render(str(self.value), True, "black"),(56*self.col+20, 53*self.row+16))
        elif self.skValue!=None and 9>=self.skValue>0:
            self.screen.blit(self.sketchf.render(str(self.skValue), True, "dimgrey"),(56*self.col+4, 53*self.row+2))
    #add text formatting to make skVal pale and in corner
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height-80
        self.screen = screen
        self.difficulty = difficulty #I pass this as a string "easy", "medium", "hard"
        #past this, useful vars I made
        self.cellw = self.width//9
        self.cellh = self.height//9
        self.selCel = (None, None)
       #self.board = generate_sudoku(size, removed)
        self.board = [[cell(1,0,0,self.screen),cell(0, 0,1,self.screen),cell(0, 0,2,self.screen),cell(0, 0,3,self.screen),cell(0, 0,4,self.screen),cell(0, 0,5,self.screen),cell(0, 0,6,self.screen),cell(0, 0,7,self.screen),cell(0, 0,8,self.screen)], [cell(1,1,0,self.screen),cell(0, 1,1,self.screen),cell(0, 1,2,self.screen),cell(0, 1,3,self.screen),cell(0, 1,4,self.screen),cell(0, 1,5,self.screen),cell(0, 1,6,self.screen),cell(0, 1,7,self.screen),cell(0, 1,8,self.screen)],
                      [cell(2,2,0,self.screen),cell(0, 2,1,self.screen),cell(0, 2,2,self.screen),cell(0, 2,3,self.screen),cell(0, 2,4,self.screen),cell(0, 2,5,self.screen),cell(0, 2,6,self.screen),cell(0, 2,7,self.screen),cell(0, 2,8,self.screen)], [cell(3,3,0,self.screen),cell(0, 3,1,self.screen),cell(0, 3,2,self.screen),cell(0, 3,3,self.screen),cell(0, 3,4,self.screen),cell(0, 3,5,self.screen),cell(0, 3,6,self.screen),cell(0, 3,7,self.screen),cell(0, 3,8,self.screen)],
                      [cell(1,4,0,self.screen),cell(0, 4,1,self.screen),cell(0, 4,2,self.screen),cell(0, 4,3,self.screen),cell(0, 4,4,self.screen),cell(0, 4,5,self.screen),cell(0, 4,6,self.screen),cell(0, 4,7,self.screen),cell(0, 4,8,self.screen)], [cell(1,5,0,self.screen),cell(0, 5,1,self.screen),cell(0, 5,2,self.screen),cell(0, 5,3,self.screen),cell(0, 5,4,self.screen),cell(0, 5,5,self.screen),cell(0, 5,6,self.screen),cell(0, 5,7,self.screen),cell(0, 5,8,self.screen)],
                      [cell(1,6,0,self.screen),cell(0, 6,1,self.screen),cell(0, 6,2,self.screen),cell(0, 6,3,self.screen),cell(0, 6,4,self.screen),cell(0, 6,5,self.screen),cell(0, 6,6,self.screen),cell(0, 6,7,self.screen),cell(0, 6,8,self.screen)], [cell(1,7,0,self.screen),cell(0, 7,1,self.screen),cell(0, 7,2,self.screen),cell(0, 7,3,self.screen),cell(0, 7,4,self.screen),cell(9, 7,5,self.screen),cell(0, 7,6,self.screen),cell(0, 7,7,self.screen),cell(0, 7,8,self.screen)],[cell(1,8,0,self.screen),cell(0, 8,1,self.screen),cell(0, 8,2,self.screen),cell(0, 8,3,self.screen),cell(0, 8,4,self.screen),cell(0, 8,5,self.screen),cell(0, 8,6,self.screen),cell(0, 8,7,self.screen),cell(0, 8,8,self.screen)]]

    def draw(self):
        # draw grid
        #draw vert
        for i in range (self.width//self.cellw +1): #vert lines
            if i%3==0:
                pygame.draw.lines(self.screen, "dark green", True, ((i * self.cellw, 0), (i * self.cellw, self.height)), 3)
            pygame.draw.line(self.screen, "dark green", (i*self.cellw, 0), (i * self.cellw, self.height))

        for i in range (self.height//self.cellh +1): #horiz lines
            if i % 3 == 0:
                pygame.draw.lines(self.screen, "dark green", True,((0,i*self.cellh), (self.width, i*self.cellh)), 3)
            pygame.draw.line(self.screen, "dark green", (0,i*self.cellh), (self.width, i*self.cellh))
        #add cell values
        for row in range(9):
            for col in range(9):
                if (row, col) == self.selCel:
                    pygame.draw.rect(self.screen, "red", (self.cellw*col,self.cellh*row,self.cellw,self.cellh), width=3)
                self.board[row][col].draw()


    def select(self, row, col):
        self.selCel = (row, col)

    #method I chose to add
    def current(self):
        return self.selCel
    def curVal(self):
        return self.board[self.selCel[0]][self.selCel[1]].get_sketched_value()
    #done
    def click(self, x, y):
        if x<self.width and y<self.height:
            row, col = y//self.cellh,x//self.cellw
            return (row, col)
        else:
            return None

    def clear(self):
        pass

    def sketch(self, value):
        self.board[self.selCel[0]][self.selCel[1]].set_sketched_value(value)
        self.board[self.selCel[0]][self.selCel[1]].set_cell_value(None)
    def place_number(self, value):
        self.board[self.selCel[0]][self.selCel[1]].set_cell_value(value)

    def reset_to_original(self):
        pass

    def is_full(self):
        return False
        #for row in self
            #if None in self[row]:
            #return False
        #return True

    def update_board(self):
        pass

    def find_empty(self):
        pass
    def check_board(self):
        return True

if __name__ == "__main__":
    main()