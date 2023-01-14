import pygame
import board.box as boxclass
import pieces.pawn as pawnclass
import pieces.knight as knightclass
import pieces.bishop as bishopclass
import pieces.rook as rookclass
import pieces.queen as queenclass
import pieces.king as kingclass

pygame.init() # now use display and fonts

# Setting the background color
background_colour = (234, 212, 252)

# Defining the screen dimensions
screen = pygame.display.set_mode((400,400))

# Setting the captions of the screen
pygame.display.set_caption("Ouhami Chess")

screen.fill(background_colour)

# Drawing the board
color1 = (233,196,106)
color2 = (42,157,143)
#pygame.draw.rect(screen,color1,pygame.Rect(0,0,100,100))
#pygame.draw.rect(screen,color2,pygame.Rect(100,0,100,100))

# Initilizaing the height position j = 0
j = 1
box_list = []

# Black pieces
black_pawn_list = []
black_knight_list = []
black_bishop_list = []
black_rook_list = []
black_queen_list = []
black_king_list = []

# White pieces
white_pawn_list = []
white_knight_list = []
white_bishop_list = []
white_rook_list = []




box_id = 1 # The box_id
while(j != 9):
    if j % 2 == 0: # Even row
        for i in range(1,9):
            if i % 2 == 0: # Even column
                rect = pygame.Rect(50*(i-1),50*(j-1),50,50)
                coloredbox = boxclass.Box(box_id,(233,196,106),50*(i-1)+25,50*(j-1) + 25,drawrect=rect)
                pygame.draw.rect(screen,color1,rect) # Color 1
                box_list.append(coloredbox)
                box_id += 1

                
            else : # Odd column

                rect = pygame.Rect(50*(i-1),50*(j-1),50,50)
                coloredbox = boxclass.Box(box_id,(42,157,143),50*(i-1) + 25,50*(j-1) + 25,drawrect=rect)
                pygame.draw.rect(screen,color2,rect) # Color 2
                box_list.append(coloredbox)
                box_id += 1

                
    else : # Odd row
        for i in range(1,9):
            if i % 2 == 0: # Even column
                rect = pygame.Rect(50*(i-1),50*(j-1),50,50)
                coloredbox = boxclass.Box(box_id,(42,157,143),50*(i-1) + 25,50*(j-1) + 25,drawrect=rect)
                pygame.draw.rect(screen,color2,rect) # Color 2
                box_list.append(coloredbox)
                box_id += 1
    
            else : # Odd column
                rect = pygame.Rect(50*(i-1),50*(j-1),50,50)
                coloredbox = boxclass.Box(box_id,(233,196,106),50*(i-1) + 25,50*(j-1) + 25,drawrect=rect)
                pygame.draw.rect(screen,color1,rect) # Color 1
                box_list.append(coloredbox)
                box_id += 1
                
    j += 1

font = pygame.font.Font('freesansbold.ttf', 32)

def setting_black_pieces():
    # Adding Pawn to the board
    for box in box_list:
        if box.id in range(9,17):
            pawnObject = pawnclass.pawn(color = "Black",x = box.x,y = box.y,value = 10)
            screen.blit(pawnObject.sprite, (pawnObject.x-30,pawnObject.y - 30))
            pawnObject.spriterect.update((box.x-20,box.y-20),(50,50))
            black_pawn_list.append(pawnObject)
            
            
    # Adding Knights to the board
    for box in box_list:
        if box.id == 2 or box.id == 7:
            knightObject = knightclass.knight(color = "Black",x = box.x,y = box.y,value = 10)
            screen.blit(knightObject.sprite, (knightObject.x - 30,knightObject.y - 30))
            knightObject.spriterect.update((box.x-20,box.y-20),(50,50))
            black_knight_list.append(knightObject)


    # Adding Bishops to the board
    for box in box_list:
        if box.id == 3 or box.id == 6:
            bishopObject = bishopclass.bishop(color = "Black",x = box.x,y = box.y,value = 10)
            bishopObject.spriterect.update((box.x-20,box.y-20),(50,50))
            black_bishop_list.append(bishopObject)
            screen.blit(bishopObject.sprite, (bishopObject.x-30,bishopObject.y - 30))

    # Adding Rooks to the board
    for box in box_list:
        if box.id == 1 or box.id == 8:
            rookObject = rookclass.rook(color = "Black",x = box.x,y = box.y,value = 10)
            rookObject.spriterect.update((box.x-20,box.y-20),(50,50))
            black_rook_list.append(rookObject)
            screen.blit(rookObject.sprite, (rookObject.x-30,rookObject.y - 30))

    # Adding Queen to the board
    for box in box_list:
        if box.id == 4:
            queenObject = queenclass.queen(color = "Black",x = box.x,y = box.y,value = 10)
            queenObject.spriterect.update((box.x-20,box.y-20),(50,50))
            black_queen_list.append(queenObject)
            screen.blit(queenObject.sprite, (queenObject.x-30,queenObject.y - 30))

    # Adding King to the board
    for box in box_list:
        if box.id == 5:
            kingObject = kingclass.king(color = "Black",x = box.x,y = box.y,value = 10)
            kingObject.spriterect.update((box.x-20,box.y-20),(50,50))
            black_king_list.append(kingObject)
            screen.blit(kingObject.sprite, (kingObject.x-30,kingObject.y - 30))

# Setting the white pieces
def setting_white_pieces():
    # Adding Pawn to the board
    text_pawn = font.render('P', True, (0,0,0))
    for box in box_list:
        if box.id in range(49,57):
            pawnObject = pawnclass.pawn("White",box.x,box.y,10)
            white_pawn_list.append(pawnObject)
            textRect = text_pawn.get_rect()
            screen.blit(text_pawn, (pawnObject.x-textRect.centerx,pawnObject.y - textRect.centery))
            
    # Adding Knights to the board
    text_knight = font.render('Kn', True, (0,0,0))
    for box in box_list:
        if box.id == 58 or box.id == 63:
            knightObject = knightclass.knight("White",box.x,box.y,10)
            white_knight_list.append(knightObject)
            textRect = text_knight.get_rect()
            screen.blit(text_knight, (knightObject.x-textRect.centerx,knightObject.y - textRect.centery))

    # Adding Bishops to the board
    text_bishop = font.render('B', True, (0,0,0))
    for box in box_list:
        if box.id == 59 or box.id == 62:
            bishopObject = bishopclass.bishop("White",box.x,box.y,10)
            white_bishop_list.append(bishopObject)
            textRect = text_bishop.get_rect()
            screen.blit(text_bishop, (bishopObject.x-textRect.centerx,bishopObject.y - textRect.centery))

    # Adding Rooks to the board
    text_rook = font.render('R', True, (0,0,0))
    for box in box_list:
        if box.id == 57 or box.id == 64:
            rookObject = rookclass.rook("White",box.x,box.y,10)
            white_rook_list.append(rookObject)
            textRect = text_rook.get_rect()
            screen.blit(text_rook, (rookObject.x-textRect.centerx,rookObject.y - textRect.centery))

    # Adding Queen to the board
    text_queen = font.render('Q', True, (0,0,0))
    for box in box_list:
        if box.id == 60:
            white_queenObject = queenclass.queen("White",box.x,box.y,10)
            textRect = text_queen.get_rect()
            screen.blit(text_queen, (white_queenObject.x-textRect.centerx,white_queenObject.y - textRect.centery))

    # Adding King to the board
    text_king = font.render('K', True, (0,0,0))
    for box in box_list:
        if box.id == 61:
            white_kingObject = kingclass.king("White",box.x,box.y,10)
            textRect = text_king.get_rect()
            screen.blit(text_king, (white_kingObject.x-textRect.centerx,white_kingObject.y - textRect.centery))


setting_black_pieces() # Setting the black pieces
setting_white_pieces() # Setting the white pieces

# Updating the display
pygame.display.flip()


# Variable to keep our game running
running = True
chosen_piece = None
while running:
    # For loop through our game events
    for event in pygame.event.get():

        # Check for the quit event
        if event.type == pygame.QUIT:
            running = False

        # Moving pieces
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousepos = pygame.mouse.get_pos()

            # Checking pawns position
            for pawn in black_pawn_list:
                if pawn.spriterect.collidepoint(mousepos):
                    chosen_piece = pawn
                    for box in box_list:
                        if box.drawrect.collidepoint(mousepos):
                            previous_block = box
                            
            
            # Checking knights position
            for knight in black_knight_list:
                if knight.spriterect.collidepoint(mousepos):
                    chosen_piece = knight
                    for box in box_list:
                        if box.drawrect.collidepoint(mousepos):
                            previous_block = box
                            can_change = False

            # Checking bishops position
            for bishop in black_bishop_list:
                if bishop.spriterect.collidepoint(mousepos):
                    chosen_piece = bishop
                    for box in box_list:
                        if box.drawrect.collidepoint(mousepos):
                            previous_block = box
                            can_change = False

            # Checking rooks position
            for rook in black_rook_list:
                if rook.spriterect.collidepoint(mousepos):
                    chosen_piece = rook
                    for box in box_list:
                        if box.drawrect.collidepoint(mousepos):
                            previous_block = box
                            can_change = False
            
           # Checking queen position
            for queen in black_queen_list:
                if queen.spriterect.collidepoint(mousepos):
                    chosen_piece = queen
                    for box in box_list:
                        if box.drawrect.collidepoint(mousepos):
                            previous_block = box
                            can_change = False

            # Checking king position
            for king in black_king_list:
                if king.spriterect.collidepoint(mousepos):
                    chosen_piece = king
                    for box in box_list:
                        if box.drawrect.collidepoint(mousepos):
                            previous_block = box
                            can_change = False


            for box in box_list:
                if box.drawrect.collidepoint(mousepos):
                    canchange = True
                    if canchange and chosen_piece is not None:
                        chosen_piece.spriterect.update(box.drawrect.topleft,(50,50))
                        screen.blit(chosen_piece.sprite, (box.x-30,box.y - 30))
                        pygame.draw.rect(screen,previous_block.color,previous_block.drawrect) # Color 1
                        # Updating the display
                        pygame.display.update()
                        pygame.time.delay(1000)
                        chosen_piece = None