# README for Python Speech Recognition Script

## Description
Works with Python <=3.11 (Some how doesnot work with Python 3.12)
This Python script is designed to perform real-time speech recognition. It records audio when the 'shift' key is pressed and stops recording when the 'esc' key is pressed. The recorded audio is then converted into text using the `whisper2basic` module's `speech2` function. The recognized text is then typed out using the `keyboard` module. The script continues to listen for the 'shift' key to start a new recording unless the script is terminated

## Dependencies

The script requires the following Python packages:

- `datetime`
- `pyaudio`
- `wave`
- `time`
- `keyboard`
- `os`
- `whisper2basic`

Please ensure these packages are installed before running the script. You can install them using pip:

```python
pip install -r requirements.txt 

```
ffmpeg needs to be installed separately . Follow the instructions from here https://phoenixnap.com/kb/ffmpeg-windows
## Usage

To use the script, simply run it in a Python environment. The script will then wait for the 'shift' key to be pressed to start recording. Press the 'esc' key to stop recording. The recorded audio will be saved as a .wav file in the 'audio' directory with a timestamp in the filename. The script will then convert the audio to text and print the recognized text. The recognized text will also be typed out using the `keyboard` module. The script will continue to listen for the 'shift' key to start a new recording unless closed 

## Notes

- The script uses the `pyaudio` module to record audio in real-time[2].
- The `wave` module is used to save the recorded audio as a .wav file[1].
- The `whisper2basic` module's `speech2` function is used to convert the recorded audio to text. This module needs to be provided or installed separately.
- The `keyboard` module is used to wait for key presses and to type out the recognized text
- The script runs in an infinite loop, constantly listening for the 'shift' key to start a new recording.

## Contributing

Contributions to improve the script are welcome. Please ensure that any changes maintain the original functionality of the script.

  
  
