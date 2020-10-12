# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:13:33 2020

@author: jaqua
"""



from tkinter import *  
import tkinter as tk
import math

#Initilize the TKInter    
root = Tk()


root.title('Mouse based graphics program')             # This is the title of the window

# **********************************************************************************************
# Define the Window sizes and draw 2 frames (plot and control windows) inside a large window
# **********************************************************************************************
#  Window size
window_width=int(800)
window_height=int(600)

#   Window - setup and draw
canvas = Canvas(root, width =window_width, height=window_height)         

# ***************************************************************************
#   Window 1 - Large external frame 
x_and_y_offsets=float(0.05)        # Space between window and external frame

x_left_top_large_frame=window_width * x_and_y_offsets
y_left_top_large_frame=window_height * x_and_y_offsets
x_right_bottom_large_frame=window_width - (window_width * x_and_y_offsets)
y_right_bottom_large_frame=window_height  -  (window_height * x_and_y_offsets)

#Draw the frame with a rectangle
canvas.create_rectangle(x_left_top_large_frame, y_left_top_large_frame,
                        x_right_bottom_large_frame, y_right_bottom_large_frame,
                        outline="blue", fill="grey", width='2')

# ***************************************************************************
#   Window 2 - Plot frame in the large window - A function is used to redraw this window to clean the area

#  Plot the "PLOT WINDOW" - Use this function to clean the picture in it - We will erase the curve and both Axes with labels
def draw_plot_window(x_left_offset, x_right_offset, y_top_bottom_offsets):


    global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
    x_left_top_plot_frame=window_width * x_left_offset
    y_left_top_plot_frame=window_height * y_top_bottom_offsets
    x_right_bottom_plot_frame=window_width - (window_width * x_right_offset)
    y_right_bottom_plot_frame=window_height  -  (window_height * y_top_bottom_offsets)

    #Draw the frame with a rectangle
    canvas.create_rectangle(x_left_top_plot_frame, y_left_top_plot_frame,
                        x_right_bottom_plot_frame, y_right_bottom_plot_frame,
                        outline="red", fill="white", width='2')

#  Define boundaries and call the plot window drawing function
x_left_plot_frame_offset=float(0.1)        # Space between window and plot frame
x_right_plot_frame_offset=float(0.3)        # Space between window and plot frame
y_top_bottom_plot_frame_offsets=float(0.1)        # Space between window and plot frame

# Draw the window with above boundaries by using the above function
draw_plot_window(x_left_plot_frame_offset, x_right_plot_frame_offset, y_top_bottom_plot_frame_offsets)


# ***************************************************************************
#   Window 3 - Control button frame in the window
x_left_control_offset=float(0.72)        # Space between window and plot frame
x_right_control_offset=float(0.08)        # Space between window and plot frame
y_top_bottom_control_offsets=float(0.1)        # Space between window and plot frame

x_left_top_control_frame=window_width * x_left_control_offset
y_left_top_control_frame=window_height * y_top_bottom_control_offsets
x_right_bottom_control_frame=window_width - (window_width * x_right_control_offset)
y_right_bottom_control_frame=window_height  -  (window_height * y_top_bottom_control_offsets)

#Draw the frame with a rectangle
canvas.create_rectangle(x_left_top_control_frame, y_left_top_control_frame,
                        x_right_bottom_control_frame, y_right_bottom_control_frame,
                        outline="red", fill="white", width='2')



# ***************************************************************************
#   Set the default values to draw the geometric functions
#   Put the range of the x axis in radian

#   Define the boundaries of the x variable and display them on the screen
global x_start, x_end
x_start=int(0)
x_end=float(4*3.14)

x_button_offset=  x_left_control_offset + 0.02   # Percentage of the width of the window
y_button_offset=  y_top_bottom_control_offsets + 0.02   # Percentage of the height of the window

y_button_space= 30          # Exact distance between the buttons and input boxes in the control frame

x_button_location=window_width*x_button_offset
y_button_location=window_height*(y_button_offset+0.02)

canvas.create_text(x_button_location, y_button_location,
                        anchor=W, font=('verdana', 12),fill='blue',
                           text="Select color")
canvas.create_text(x_button_location, y_button_location+y_button_space,
                        anchor=W, font=('verdana', 12),fill='blue',
                           text="then option")

#Initialize a List That Will Store the End Points of the Lines the User Creates
line_end_points = [ ]

#Function That Determines When The Color Red Was Pressed 
def color_red_activated():
    global color 
    color = "red"
    print("The user has clicked on the red color button")

#Function That Determines When The Color Green Was Pressed 
def color_green_activated():
    global color 
    color = "green"
    print("The user has clicked on the green color button")

#Function That Determines When The Color Blue Was Pressed   
def color_blue_activated():
    global color 
    color = "blue"
    print("The user has clicked on the blue color button")
    
#Function That Determines When The Color purple Was Pressed 
def color_purple_activated():
    global color
    color = "#b366ff"
    print("The user has clicked on the purple color button")

#Function That Determines When The Color Orange Was Pressed 
def color_orange_activated():
    global color
    color = "#ffa31a"
    print("The user has clicked on the orange color button")
   
#Function that determines when the color brown was pressed
def color_brown_activated():
    global color
    color = "#996633"
    print("The user has clicked on the brown color button")

# Function to clear the plotting area - Redraw that frame
def clear():
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        # Draw the window with above boundaries by using the above function
        draw_plot_window(x_left_plot_frame_offset, x_right_plot_frame_offset, y_top_bottom_plot_frame_offsets)

# Function to draw a line on the canvas, Step 1 & 4    
def draw_line ():
        canvas.bind('<Button-1>', draw_line_1)
        print("The left mouse button has been clicked")

     

# Function to draw a line on the canvas, Step 2        
def draw_line_1 (event):
        global control
        control=1
        global x,y    
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = 'blue', width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = 'blue', width = 1)
            canvas.bind('<Button-1>', draw_line_2)

# Function to draw a line on the canvas, Step 3
def draw_line_2(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1
        global color
        global i,j,k,l
        
        x1 = event.x
        y1 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x,y,x1,y1, fill=color, width = 3)
                control=0
                #Empties the color variable so that the program doesn't run into any bugs
                color=""
                #Displays in terminal window that the user has drawn as line
                print("The user has drawn a line")
                
                #Declare a list called coordinates to then append to line_end_points
                coordinates = [ ] 
                coordinates.extend((x ,y, x1, y1))
                line_end_points.append(coordinates)
                print("The line_end_points are: ", line_end_points)


# Function to draw a circle on the canvas, Step 1 & 4    
def draw_circle ():
        canvas.bind('<Button-1>', draw_circle_1)
     

# Function to draw a circle on the canvas, Step 2        
def draw_circle_1 (event):
        global control
        control=1
        global x,y    
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = 'red', width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = 'red', width = 1)
            canvas.bind('<Button-1>', draw_circle_2)

# Function to draw a circle on the canvas, Step 3
def draw_circle_2(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1
        global color
        x1 = event.x
        y1 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                d = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                canvas.create_oval(x-d,y+d,x+d,y-d, outline=color,  width = 3)
                control=0
                #Empties the color variable so that the program doesn't run into any bugs
                color=""
                print("The user has drawn a circle")




# Function to draw an ellipse on the canvas, Step 1 & 4    
def draw_ellipse ():
        canvas.bind('<Button-1>', draw_ellipse_1)
     

# Function to draw a line on the canvas, Step 2        
def draw_ellipse_1 (event):
        global control
        control=1
        global x,y
        global color
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = color, width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = color, width = 1)
            canvas.bind('<Button-1>', draw_ellipse_2)

# Function to draw a line on the canvas, Step 3
def draw_ellipse_2(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1
        global color
        x1 = event.x
        y1 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_oval(x,y,x1,y1, outline=color, width = 3)
                control=0
                #Empties the color variable so that the program doesn't run into any bugs
                color=""
                print("The user has drawn an ellipse")


# Function to draw a rectangle on the canvas, Step 1 & 4    
def draw_rectangle ():
        canvas.bind('<Button-1>', draw_rectangle_1)
     

# Function to draw a line on the canvas, Step 2        
def draw_rectangle_1 (event):
        global control
        control=1
        global x,y  
        global color
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = color, width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = color, width = 1)
            canvas.bind('<Button-1>', draw_rectangle_2)
            

# Function to draw a line on the canvas, Step 3
def draw_rectangle_2(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1
        global color
        x1 = event.x
        y1 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_rectangle(x,y,x1,y1, outline=color,  width = 3)
                control=0
            #Empties the color variable so that the program doesn't run into any bugs
            color=""

# Function to draw a triangle on the canvas, Step 1 & 4    
def draw_triangle ():
        canvas.bind('<Button-1>', draw_triangle_1)
     

# Function to draw a triangle on the canvas, Step 2        
def draw_triangle_1 (event):
        global control
        control=1
        global x,y 
        global color
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = color, width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = color, width = 1)
            canvas.bind('<Button-1>', draw_triangle_2)

# Function to draw a triangle on the canvas, Step 3
def draw_triangle_2(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1
        global color
        x1 = event.x
        y1 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x,y,x1,y1, fill=color,  width = 3)
#               control=0
                canvas.bind('<Button-1>', draw_triangle_3)

# Function to draw a triangle on the canvas, Step 4
def draw_triangle_3(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1,x2,y2
        global color
        x2 = event.x
        y2 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x2>x_left_top_plot_frame and x2<x_right_bottom_plot_frame and y2>y_left_top_plot_frame and y2<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x1,y1,x2,y2, fill=color,  width = 3)
                canvas.create_line(x2,y2,x,y, fill=color,  width = 3)
                control=0
                #Empties the color variable so that the program doesn't run into any bugs
                color=""

# Function to draw a triangle on the canvas, Step 1 & 4    
def draw_polygon ():
        canvas.bind('<Button-1>', draw_polygon_1)
     

# Function to draw a triangle on the canvas, Step 2        
def draw_polygon_1 (event):
        global control
        control=1
        global x,y 
        global color
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = color, width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = color, width = 1)
            canvas.bind('<Button-1>', draw_polygon_2)

# Function to draw a triangle on the canvas, Step 3
def draw_polygon_2(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1
        global color
        x1 = event.x
        y1 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x,y,x1,y1, fill=color,  width = 3)
#               control=0
                canvas.bind('<Button-1>', draw_polygon_3)

# Function to draw a triangle on the canvas, Step 4
def draw_polygon_3(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1,x2,y2
        global color
        x2 = event.x
        y2 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x2>x_left_top_plot_frame and x2<x_right_bottom_plot_frame and y2>y_left_top_plot_frame and y2<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click
            
            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x1,y1,x2,y2, fill=color,  width = 3)
#               control=0
                canvas.bind('<Button-1>', draw_polygon_4)

# Function to draw a triangle on the canvas, Step 5
def draw_polygon_4(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1,x2,y2,x3,y3
        global color
        x3 = event.x
        y3 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x3>x_left_top_plot_frame and x3<x_right_bottom_plot_frame and y3>y_left_top_plot_frame and y3<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click
            
            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x2,y2,x3,y3, fill=color,  width = 3)
#               control=0
                canvas.bind('<Button-1>', draw_polygon_5)   
                
# Function to draw a triangle on the canvas, Step 6
def draw_polygon_5(event):
        global control
        global cursor1, cursor2
        global x,y,x1,y1,x2,y2,x3,y3,x4,y4
        global color
        x4 = event.x
        y4 = event.y
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x4>x_left_top_plot_frame and x4<x_right_bottom_plot_frame and y4>y_left_top_plot_frame and y4<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click
            
            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x3,y3,x4,y4, fill=color,  width = 3)
#               control=0
                canvas.bind('<Button-1>', draw_polygon_4) 
                #Empties the color variable so that the program doesn't run into any bugs
                color=""
                
def motion_line_live_1(event):
    global cursor1, cursor2
    global control_cursor
    if control_cursor>0:
        canvas.delete(cursor1, cursor2)
        
    x, y = event.x, event.y
    cursor1=canvas.create_line(x-5,y,x+5,y, fill = 'green', width = 1)
    cursor2=canvas.create_line(x,y-5,x,y+5, fill = 'green', width = 1)

    control_cursor=1

def motion_line_live_2(event):
    global x,y
    global cursor1, cursor2,cursor3,cursor4
    global control_cursor
    global control_live_line_option
#    global control_live_line
    global control_cursor_live_line,line_mouse

    if control_live_line_option>0:
        if control_cursor_live_line>0:
#           canvas.delete(cursor1, cursor2)
            canvas.delete(cursor3, cursor4)

        if control_cursor_live_line>0:
            canvas.delete(line_mouse)
        
        xm, ym = event.x, event.y


        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if xm>x_left_top_plot_frame and xm<x_right_bottom_plot_frame and ym>y_left_top_plot_frame and ym<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click
            cursor3=canvas.create_line(xm-5,ym,xm+5,ym, fill = 'green', width = 1)
            cursor4=canvas.create_line(xm,ym-5,xm,ym+5, fill = 'green', width = 1)
        
            line_mouse=canvas.create_line(x,y,xm,ym, fill="green", width = 1)
            control_cursor_live_line=1
    else:
        return
    
            

  
def draw_line_live ():
        canvas.bind('<Button-1>', draw_line_live_1)
        canvas.bind('<Motion>', motion_line_live_1)
     

# Function to draw a line on the canvas, Step 2        
def draw_line_live_1 (event):
        global control,control_live_line_option
        control=1
        global x,y    
        x = event.x
        y = event.y

        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x>x_left_top_plot_frame and x<x_right_bottom_plot_frame and y>y_left_top_plot_frame and y<y_right_bottom_plot_frame:
            global cursor1, cursor2
            cursor1=canvas.create_line(x-5,y,x+5,y, fill = 'red', width = 1)
            cursor2=canvas.create_line(x,y-5,x,y+5, fill = 'red', width = 1)
            canvas.bind('<Button-1>', draw_line_2)
            control_live_line_option=1
            canvas.bind('<Motion>', motion_line_live_2)

# Function to draw a line on the canvas, Step 3
def draw_line_live_2(event):
        global control,control_live_line_option
        global cursor1, cursor2
        global x,y,x1,y1
        x1 = event.x
        y1 = event.y
        #  Stop drawing rubber lines
        control_live_line_option=0
        # Evaluate if the point is at the plot window
        global x_left_top_plot_frame, x_right_bottom_plot_frame, y_left_top_plot_frame, y_right_bottom_plot_frame
        if x1>x_left_top_plot_frame and x1<x_right_bottom_plot_frame and y1>y_left_top_plot_frame and y1<y_right_bottom_plot_frame:

        #Erase the cursor which marks the location of first click

            canvas.delete(cursor1, cursor2)
            if control== 1:
                canvas.create_line(x,y,x1,y1, fill="black", width = 3)
                control=0

def erase_line(event): 
    global i,j,k,l
    
    if 80 < event.x < 120 and 80 < event.y < 120:
        w.delete(i,j,k,l) 
        canvas.bind("<Button-1>", click)
    
    

            

# *******************************************************************************************************
# *******************************************************************************************************
# ********************************  MAIN ACTION *********************************************************
# *******************************************************************************************************
# *******************************************************************************************************

# To avoid problems at the first run - It will be 1 after the first point in the functions
global cursor_control
global control_live_line
global control_cursor_live_line
global control_live_line_option
control_cursor=0
control_live_line=0
control_cursor_live_line=0
control_live_line_option=0
# Draw the sine wave with defined boundaries first time


# ***************************************************************************
# Button to clear the drawing area
clear_button= Button(canvas,text="Clear", command=clear, height=1, width=8, bg="yellow",compound=LEFT)
clear_button.place(x = x_button_location, y = y_button_location+y_button_space*3)

# ***************************************************************************
# Button to draw line
line_button= Button(canvas,text="Line", command=draw_line, height=1, width=8, bg="yellow",compound=LEFT)
line_button.place(x = x_button_location, y = y_button_location+y_button_space*4)
# ***************************************************************************
# Button to draw circle
ellipse_button= Button(canvas,text="Circle", command=draw_circle, height=1, width=8, bg="yellow",compound=LEFT)
ellipse_button.place(x = x_button_location, y = y_button_location+y_button_space*5)

# ***************************************************************************
# Button to draw ellipse
ellipse_button= Button(canvas,text="Ellipse", command=draw_ellipse, height=1, width=8, bg="yellow",compound=LEFT)
ellipse_button.place(x = x_button_location, y = y_button_location+y_button_space*6)

# ***************************************************************************
# Button to draw rectangle
rectangle_button= Button(canvas,text="Rectangle", command=draw_rectangle, height=1, width=8, bg="yellow",compound=LEFT)
rectangle_button.place(x = x_button_location, y = y_button_location+y_button_space*7)

# ***************************************************************************
# Button to draw a triangle
triangle_button= Button(canvas,text="Triangle", command=draw_triangle, height=1, width=8, bg="yellow",compound=LEFT)
triangle_button.place(x = x_button_location, y = y_button_location+y_button_space*8)

# ***************************************************************************
#Button to draw a line - line shape is displayed
live_line_button= Button(canvas,text="Line - live", command=draw_line_live, height=1, width=8, bg="yellow",compound=LEFT)
live_line_button.place(x = x_button_location, y = y_button_location+y_button_space*9)

#Button to Add Red Color
red_button= Button(canvas,text="Red", command=color_red_activated, height=1, width=8, bg="#ff4d4d",compound=LEFT)
red_button.place(x = x_button_location + 70, y = y_button_location+y_button_space*5)

#Button to Add Blue Color
blue_button= Button(canvas,text="Blue", command=color_blue_activated, height=1, width=8, bg="#4d88ff",compound=LEFT)
blue_button.place(x = x_button_location + 70, y = y_button_location+y_button_space*4) 

#Button to Add Green Color
green_button= Button(canvas,text="Green", command=color_green_activated, height=1, width=8, bg="#00cc00",compound=LEFT)
green_button.place(x = x_button_location + 70, y = y_button_location+y_button_space*3) 

#Button to Add Purple Color
purple_button= Button(canvas,text="Purple", command=color_purple_activated, height=1, width=8, bg="#b366ff",compound=LEFT)
purple_button.place(x = x_button_location + 70, y = y_button_location+y_button_space*6) 

#Button to Add Orange Color
orange_button= Button(canvas,text="Orange", command=color_orange_activated, height=1, width=8, bg="#ffa31a",compound=LEFT)
orange_button.place(x = x_button_location + 70, y = y_button_location+y_button_space*7) 

#Button to Add Brown Color
brown_button= Button(canvas,text="Brown", command=color_brown_activated, height=1, width=8, bg="#996633",compound=LEFT)
brown_button.place(x = x_button_location + 70, y = y_button_location+y_button_space*8) 

# Button to draw a Polygon
polygon_button= Button(canvas,text="Polygon", command=draw_polygon, height=1, width=8, bg="yellow",compound=LEFT)
polygon_button.place(x = x_button_location, y = y_button_location+y_button_space*10)

#Erase Button
erase_button= Button(canvas,text="Erase \nLine", command=erase_line, height=2, width=8, bg="yellow",compound=LEFT)
erase_button.place(x = x_button_location, y = y_button_location+y_button_space*11)

canvas.pack()
root.mainloop()
