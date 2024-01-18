##Please install ffmpeg on windows
##https://www.gyan.dev/ffmpeg/builds/
from datetime import datetime
import pyaudio
import wave
import time
import threading
import keyboard
import os
from whisper2basic import speech2
# Initialize PyAudio
p = pyaudio.PyAudio()

# Define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Start the stream for recording
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

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
    wf = wave.open(f'{output_filename}', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("File saved")
    recog_text= speech2(output_filename)['text']
    print(recog_text)
    
    keyboard.write(recog_text)
    exit()  # Close the script after recording

def record_audio():
    while recording and stream.is_active():
        frames.append(stream.read(CHUNK))

# Start recording thread
recording_thread = threading.Thread(target=record_audio)

# Wait for the 'shift' key to start recording
print("Waiting for 'shift' key to be pressed...")
keyboard.wait('shift')
start_recording()

# Start recording thread
recording_thread.start()

# Record for 10 seconds
#time.sleep(10)

# Stop recording
keyboard.wait('esc')
stop_recording()
#time.sleep(3)
