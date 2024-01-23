#ffmpeg needs to be installed separately . Follow the instructions from here https://phoenixnap.com/kb/ffmpeg-windows

import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
# you can change model id here. Some examples "openai/whisper-tiny.en" , "openai/whisper-medium.en"
# More models here https://huggingface.co/collections/openai/whisper-release-6501bba2cf999715fd953013
model_id = "openai/whisper-small.en"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)


def speech2text(audiofile):
    audiotext=pipe(audiofile)
    return audiotext

