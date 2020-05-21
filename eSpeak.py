
# eSpeak utility class - Tutorial #4
# by Robo Pi

# Import subprocess to execute the espeak terminal commands
import subprocess as cmdLine

# Name the class:
class eSpeak:

    # __init__ defines the voices to be used.
    def __init__(self, voice='mb-us1'):
        self.voice = voice

    # Speak the text
    def say(self, speech):
        # Define the command line
        command = 'espeak -v ' + self.voice + " " + chr(34) + speech + chr(34)
        # Execute the command in term terminal
        cmdLine.run(command, shell=True, capture_output=True, text=True)        

    # Prints phonemes using -X or -x  (the -q means quiet no speaking)
    # You still need to assign -v here for the dictionary reference
    def phonemes(self, speech, phone):
        command = 'espeak -' + phone + ' -q -v ' + self.voice + " " + chr(34) + speech + chr(34)
        result = cmdLine.run(command, shell=True, capture_output=True, text=True)
        # Return the result.
        return result.stdout

    # Sends the speech out to a wav file named by filename
    def wavFile(self, speech, filename):
        command = 'espeak -w ' + filename + ' -v ' + self.voice + " " + chr(34) + speech + chr(34)
        cmdLine.run(command, shell=True, capture_output=True, text=True)

    # Read a text file
    def textFile(self, filename):
        command = 'espeak -f ' + filename + ' -v ' + self.voice
        cmdLine.run(command, shell=True, capture_output=True, text=True)

    def compile(self):
        command = 'espeak --compile=' + self.voice
        cmdLine.run(command, shell=True, capture_output=True, text=True)