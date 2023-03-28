import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    turtle.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    
    # your code to animate Irma here
    with open("data/irma.csv") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        for row in reader:
            lat = float(row[2])
            lon = float(row[3])
            wind = int(row[4])
            category = hurricaneCategory(wind)
            turtle.goto(lon, lat)
            turtle.pensize(lineThickness(category))
            turtle.pencolor(lineColor(category))
            turtle.write(categoryText(category))
        turtle.done()

def hurricaneCategory(wind_speed):
    if wind_speed >= 157:
        return 5
    elif wind_speed >= 130:
        return 4
    elif wind_speed >= 111:
        return 3
    elif wind_speed >= 96:
        return 2
    elif wind_speed >= 74:
        return 1
    else:
        return 0

def lineThickness(category):
    if category == 5:
        return 15
    elif category == 4:
        return 10
    elif category == 3:
        return 8
    elif category == 2:
        return 5
    elif category == 1:
        return 3
    else:
        return 1

def lineColor(category):
    if category == 5:
        return "red"
    elif category == 4:
        return "orange"
    elif category == 3:
        return "yellow"
    elif category == 2:
        return "green"
    elif category == 1:
        return "blue"
    else:
        return "white"

def categoryText(category):
    if category > 0:
        return str(category)
    else:
        return ""
        
if __name__ == "__main__":
    irma()
