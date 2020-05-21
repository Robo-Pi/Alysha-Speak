# Alysha-Speak
A repository for the design of how Alysha will speak

This is the beginning of creating a voice for Alysha.  I'm using a program called eSpeak not eSpeak-ng.

I've created a series of videos explaining how I got to this point:

<a href="https://www.youtube.com/watch?v=stMPWkRvTSA&list=PLB1qG5ujfHrVv4ZkesiNN8jBPwi1Udpit">eSpeak Video Series</a>

ai_list and ai_rules are the current dictionary source files I'm using thus far in this project.

The following is the very beginning of a GUI program to interface Alsha with eSpeak. 

Note: This program may not work with the standard espeak_list files that normally come with eSpeak.  I'll be making my own dictionary lists so I don't need the espeak dictionaries.   Compiling this list and rules file will create an ai_dict file which the alysha voice must point to.  See the video series.

New_Dict_Main.py - The main dictionary program.

New_alysha.py - is a class named alysha

GUI_FUNCS.py - is a class I made to position Tkinter windows on the scrreen.

eSpeak.py - is a class that accesses eSpeak via the Python subprocess module.

filesClass.py - is a class that reads and write files. 

I'm not the world's best programmer, so this is all just tossed together.   This is a seed for growing a more complex voice system as time progresses.   I'll most likely change this up dramatically as I move forward.   As an example I'm already going to move the alysha.get_dict() method into a class of its own.  So what I've done thus far is to just get my feet wet with creating a voice for Alsha. 

Why use eSpeak?

I'm aware that there are better sounding voices available, as well as TTS systems that already incorporate AI systems.  But my goal is to create my own Linquistic AI system from scratch.  And eSpeak offers everything I need to do this, including independence from the Internet and other people's cloud servers, as well as being designed to run on lightweight SBCs.  So these were the criteria for my choice of using eSpeak. 



