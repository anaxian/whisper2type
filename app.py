# ffmpeg needs to be installed separately . Follow the instructions from here https://phoenixnap.com/kb/ffmpeg-windows

from datetime import datetime
import pyaudio
import wave
import keyboard
import os
from whisper2text import speech2text

# Check if the 'audio' directory exists
if not os.path.isdir('audio'):
    # If not, create it
    os.makedirs('audio')

# Initialize PyAudio
p = pyaudio.PyAudio()

# Define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Start the stream for recording
try:
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
except Exception as e:
    print(f"Error opening stream: {e}")
    p.terminate()
    exit(1)

frames = []
recording = False

def start_recording():
    global recording
    global frames
    frames = []
    recording = True
    print("Recording started")

def stop_recording():
    global recording
    global frames
    print("Recording stopped")
    recording = False
    # Save frames to file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = os.path.join('audio', f'recording_{timestamp}.wav')
    try:
        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        print("File saved")
        try:
            recog_text = speech2text(output_filename)['text']
            print(recog_text)
            keyboard.write(recog_text)
        except Exception as e:
            print(f"Error transcribing audio: {e}")
    except Exception as e:
        print(f"Error saving recording: {e}")

while True:
    # Wait for the 'shift' key to start recording
    print("Waiting for 'shift' key to be pressed to start recording...")
    keyboard.wait('shift')
    start_recording()
    print("Press Esc to stop recording and type the text at your current cursor position")

    # Record while the 'esc' key is not pressed
    while not keyboard.is_pressed('esc'):
        frames.append(stream.read(CHUNK))

    # Stop recording when 'esc' key is pressed
    stop_recording()

    # Check if F12 is pressed to exit the loop
    if keyboard.is_pressed('F12'):
        break

# Close the stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()