import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

# warna
white = pygame.Color('#ffffff')
red_01 = pygame.Color('#FF1226')
red_02 = pygame.Color('#D20E1E')

# Assets
icon = pygame.image.load('Assets/Icon.png')
Background = pygame.image.load('Assets/Background.png')
red_car = pygame.image.load('Assets/RedCar.png')
white_car = pygame.image.load('Assets/WhiteCar.png')
play = pygame.image.load('Assets/play.png')
play_hover = pygame.image.load('Assets/play2.png')
stop = pygame.image.load('Assets/Stop.png')
stop_hover = pygame.image.load('Assets/Stop2.png')

#Layar
width, height = 1120, 630
pygame.init()
pygame.display.set_caption("Gerak Lurus Beraturan & Gerak Lurus Berubah Beraturan")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


# function
def draw_text(text,color,x,y,size):
    font = pygame.font.Font('Assets/Font/Poppins-Regular.ttf',size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface,(x,y))

# Widget 
# Mobil 1
    #Slider Kecepatan
slider = Slider(screen, 160, 497, 140, 13, min=0, max=50, step=1, handleColour = red_01)
    #Slider Jarak
slider2 = Slider(screen, 185, 550, 115, 13, min=-10, max=10, step=1, handleColour = red_01)
# Mobil 2
    # Slider Kecepatan
slider3 = Slider(screen, 570, 497, 140, 13, min=0, max=50, step=1, handleColour = red_01)
    # Slider Jarak
slider4 = Slider(screen, 595, 550, 115, 13, min=-10, max=10, step=1, handleColour = red_01)
   
#Variabel inisial
showResult,showResult2 = False,False
percepatan,percepatan2 = 0,0
kecepatan,kecepatan2 = 0, 0
move,move2 = 0,0
xcar,xcar2 = 28,28
jarak = 940
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 880 <= mouse[0] <= 918 and 395 <= mouse[1] <= 433: 
                print("play")
                move,move2 = 1,1
                count = True
                showResult, showResult2 = False,False
            if 930 <= mouse[0] <= 968 and 395 <= mouse[1] <= 433:  
                print("stop")
                move,move2 = 0,0
                xcar,xcar2 = 28,28
                waktu = 0
                showResult, showResult2 = False,False
    
    # Latar dan gambar              
    screen.blit(Background,(0,0))
    screen.blit(red_car,(xcar,285))
    screen.blit(white_car,(xcar2,175))  
    
    #slider
    draw_text(str(slider.getValue()),white,323,490,20)
    draw_text(str(slider2.getValue()),white,323,540,20)
    draw_text(str(slider3.getValue()),white,733,490,20)
    draw_text(str(slider4.getValue()),white,733,540,20)

    #Button
    mouse = pygame.mouse.get_pos() 
    if 880 <= mouse[0] <= 918 and 395 <= mouse[1] <= 433: 
        screen.blit(play_hover,(880,395))
    else: 
        screen.blit(play,(880,395))
    mouse = pygame.mouse.get_pos() 
    if 930 <= mouse[0] <= 968 and 395 <= mouse[1] <= 433:  
        screen.blit(stop_hover,(930,395))
    else: 
        screen.blit(stop,(930,395))

    #Percepatan
    percepatan = int(slider2.getValue())
    percepatan2 = int(slider4.getValue())
    
    #Kecepatan
    kecepatan = int(slider.getValue())+percepatan
    kecepatan2 = int(slider3.getValue())+percepatan2

    #Pergerakan Mobil
    if move == 1 and xcar <= jarak :
        xcar += kecepatan/10
    if move2 == 1 and xcar2 <= jarak :
        xcar2 += kecepatan2/10
    #Antisipasi jarak
    if jarak - xcar < kecepatan/10:
        xcar += jarak - xcar
        showResult = True
    if jarak - xcar2 < kecepatan2/10:
        xcar2 += jarak - xcar2
        showResult2 = True
    
    #Mobil 1
    if showResult == True:
        if kecepatan != 0:
            t = int(jarak//kecepatan)
            minute = t // 60
            second = t % 60
            output = "{0:02}:{1:02}".format(minute, second)
        else :
            output = "00:00"
        draw_text(str(output), red_02, 995, 500, 20)
    else :
        output = "00:00"
        draw_text(str(output), red_02, 995, 500, 20)
    
    #Mobil 2
    if showResult2 == True:
        if kecepatan2 != 0:
            t = int(jarak//kecepatan2)
            minute2 = t // 60
            second2 = t % 60
            output2 = "{0:02}:{1:02}".format(minute2, second2)
        else :
            output2 = "00:00"
        draw_text(str(output2), red_02, 995, 530, 20)
    else :
        output = "00:00"
        draw_text(str(output), red_02, 995, 530, 20)
        
    pygame_widgets.update(events)
    pygame.display.update()
    clock.tick(60)

pygame.quit()