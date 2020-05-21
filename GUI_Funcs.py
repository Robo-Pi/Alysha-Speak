
# GUI functions Utility Class
# by Robo Pi

class GUI_Funcs:

    def __init__(self, window, title):
        self.window = window
        self.title = title

    def WinCenter(self, width, height):
        # define window title
        self.window.title(self.title)
        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        # calculate the x and y coordinates to center the window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        # set the dimensions of the screen and place it.
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def WinCenterOffset(self, width, height, vert_Offset, Horz_Offset):
        # define window title
        self.window.title(self.title)
        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        # calculate the x and y coordinates to center the window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        x = x + Horz_Offset
        y = y + vert_Offset
        # set the dimensions of the screen and place it.
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def WinCoords(self, width, height, x, y):
        # define window title
        self.window.title(self.title)
        # set the dimensions of the screen and place it.
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))
