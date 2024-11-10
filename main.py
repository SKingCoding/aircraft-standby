import tkinter as tk
import random
import pyttsx3
import speech_recognition as sr

# Set up the main Tkinter window
window = tk.Tk()
window.title("Dubai Airport Ground Simulation")
window.geometry("1000x700")

canvas = tk.Canvas(window, bg="black", width=1000, height=700)
canvas.pack()

# Basic Dubai Airport ground layout (simplified version, full layout needs more taxiways and gates)
# Drawing gates, taxiways, and runways here
canvas.create_line(200, 650, 800, 650, fill="white", width=2)  # Main runway
canvas.create_line(250, 600, 750, 600, fill="white", width=2)  # Parallel taxiway
canvas.create_rectangle(150, 500, 850, 700, outline="white", width=1)  # Airport boundary

# Define gates
gates = [(random.randint(150, 850), random.randint(500, 650)) for _ in range(5)]
for x, y in gates:
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="cyan")  # Gate marker

# Initialize text-to-speech
engine = pyttsx3.init()

# Plane class for grounded aircraft
class Plane:
    def __init__(self, canvas, x, y, callsign):
        self.canvas = canvas
        self.callsign = callsign
        self.id = canvas.create_oval(x, y, x + 10, y + 10, fill="green")
        self.x, self.y = x, y

    def request_permission(self):
        # Simulates the plane calling up for taxi clearance
        engine.say(f"{self.callsign} requesting taxi clearance.")
        engine.runAndWait()
    
    def receive_instruction(self, instruction):
        # Plane reads back instruction
        engine.say(f"{self.callsign}, roger. {instruction}")
        engine.runAndWait()

# Create planes at gates
planes = [Plane(canvas, x, y, f"Flight {1000+i}") for i, (x, y) in enumerate(gates)]

# Recognize user instruction using speech recognition
def get_user_instruction():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for instruction...")
        audio = recognizer.listen(source)
        try:
            instruction = recognizer.recognize_google(audio)
            print(f"Instruction received: {instruction}")
            return instruction
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError:
            print("Error with the speech recognition service")
            return None

# Simulate plane requesting instructions
def start_communications():
    for plane in planes:
        plane.request_permission()
        instruction = get_user_instruction()
        if instruction:
            plane.receive_instruction(instruction)
        else:
            engine.say("Please repeat the instruction.")
            engine.runAndWait()

# Start communication sequence
start_communications()

# Run the Tkinter main loop
window.mainloop()
