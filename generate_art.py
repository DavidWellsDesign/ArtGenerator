from PIL import Image, ImageDraw, ImageChops, ImageColor
import random
import colorsys

def randomColour():
    h = random.random()
    s = 1
    v = 1

    floatRGB = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in floatRGB]
    
    return tuple(rgb)
    #return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def randomHSL(h:int,l:int):
    
    s = 1

    floatRGB = colorsys.hls_to_rgb(h, l, s)
    rgb = [int(x * 255) for x in floatRGB]
    
    return tuple(rgb)


def interpolate(start_Colour,end_Colour,factor:float):
    recip = 1 - factor
    return(
        int(start_Colour[0] * recip + end_Colour[0] * factor),
        int(start_Colour[1] * recip + end_Colour[1] * factor),
        int(start_Colour[1] * recip + end_Colour[1] * factor)
    )

def generate_art(path: str):
    print(f'Generating {path}!')
    image_resolution_x = 256
    image_resolution_y = 256
    padding_px = 12
    image_bg_colour = (randomHSL(random.random(),0.7))
    thickness = 0
    arcSize = 12
    arcScale = 6
    ellipseStartPositionX = 0
    ellipseStartPositionY = 0
    ellipseMovePositionX = 1
    ellipseMovePositionY = 1
    ellipseMoveModifier = 2 #how much to multiply the ellipse movement for each iteration
    ellipseColour = random.random()
    ellipseColourSteps = 0.01 #how much to move the Hue value for each iteration
    startColour = randomColour()
    endColour = randomColour()
    image = Image.new("RGB", (image_resolution_x, image_resolution_y), (image_bg_colour))
    recordColour = random.random()

    icon = Image.open('Icons/Icon1.png')

    #Draw some lines
    draw = ImageDraw.Draw(image)
    points = []

    #Generate the points
    for _ in range (18):
        random_point = (
            random.randint(0+padding_px, image_resolution_x-padding_px),
            random.randint(0+padding_px, image_resolution_y-padding_px)
            )
        points.append(random_point)

    #draw the record
    draw.ellipse((6,6,image_resolution_x-6,image_resolution_y-6),fill=(randomHSL(recordColour,0.02)),outline=(255,255,255),width=2)
    #draw the reflection lines
    
    #draw the points
    for i, point in enumerate(points):

        #Overlay canvas
        overlayImage = Image.new("RGB", (image_resolution_x, image_resolution_y), (image_bg_colour))
        overlayDraw = ImageDraw.Draw(overlayImage)
        p1 = point

        thickness+=1

        #overlayDraw.line(line_xy,fill=(line_colour),width=thickness)

        if ellipseColour >= 1:
            ellipseColour=0

        #draw.ellipse((ellipseStartPositionX,ellipseStartPositionY,ellipseStartPositionX+20,ellipseStartPositionY+20),fill=randomHSL(ellipseColour))
        
        draw.arc((0+arcSize,0+arcSize,image_resolution_x-arcSize,image_resolution_y-arcSize), random.randrange(0,360), random.randrange(0,360),fill=randomHSL(ellipseColour,0.6),width=2)

        #move the next ellipse a set amount

        ellipseMovePositionX = random.random()
        ellipseMovePositionY = random.random()

        arcSize += arcScale

        ellipseStartPositionX += ellipseMovePositionX * ellipseMoveModifier
        ellipseStartPositionY += ellipseMovePositionY * ellipseMoveModifier
        
        ellipseColour += ellipseColourSteps

        #image = ImageChops.add(image, overlayImage)

    #draw the reflection
    draw.pieslice((6,6,image_resolution_x-6,image_resolution_y-6), 222, 228,fill=(250,250,250))
    draw.pieslice((6,6,image_resolution_x-6,image_resolution_y-6), 217, 218,fill=(250,250,250))
    draw.pieslice((6,6,image_resolution_x-6,image_resolution_y-6), 232, 233,fill=(250,250,250))
    draw.pieslice((6,6,image_resolution_x-6,image_resolution_y-6), 42, 48,fill=(250,250,250))
    draw.pieslice((6,6,image_resolution_x-6,image_resolution_y-6), 37, 38,fill=(250,250,250))
    draw.pieslice((6,6,image_resolution_x-6,image_resolution_y-6), 52, 53,fill=(250,250,250))

    #draw the sticker in the middle
    draw.ellipse((101,101,155,155),fill=(250,250,250))
    draw.ellipse((103,103,153,153),fill=(randomHSL(random.random(),0.7)))

    #image.paste(icon,box=(112,112),mask=icon)

    draw.ellipse((126,126,129,129),fill=(0,0,0))

    image.save(path)

if __name__ == "__main__":
    for i in range (10):
        generate_art(f"Art/test_image_{i}.png")
