import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("jfk.flac")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(fp16 = False)
result = whisper.decode(model, mel, options)
print("Text: {}".format(result.text))
print("Comparing resulting text with the existing one...")

# print the recognized text
with open("jfk.txt", "r") as text_file:
    my_text = text_file.read()

if(result.text == my_text):
    print("Test passed")
    print()
else:
    print("Test failed")