
# Files utility class - Tutorial #1
# by Robo Pi

class filesClass:

    # __init__ defines the file to be used.
    def __init__(self, filename):
        self.filename = filename

    def readFile(self, print_line_numbers = False):
        # Open the file for reading.
        with open(self.filename, "r", encoding='utf8') as voice:
            # Read the lines into a list called lines.
            lines = voice.readlines()
            # Set a line counter to zero.
            if print_line_numbers == True:
                lineNumber = 0
                # Print out the lines with line numbers
                for line in lines:    
                    print (lineNumber, end="") # end="" prevents an extra line return
                    print(" ", end="")
                    print (line, end="")
                    lineNumber += 1 # increment the line number
        print("\n") # add an extra line return when finished.
        return lines # return the list of lines from the file.

    def writeFile(self, lines):
        # Open the file for writing.
        with open(self.filename, 'w', encoding='utf8') as outfile:
            # Write the lines to the file.
            for line in lines:
                outfile.write(line)        
        