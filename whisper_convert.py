import os
import whisper

def transcribe_and_save(chunks_dir, output_dir, model_name="base"):
    model = whisper.load_model(model_name)

    # Make directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    chunk_files = [f for f in os.listdir(chunks_dir) if f.endswith('.wav')]

    for chunk_file in chunk_files:
        # load audio and pad/trim it to fit 30 seconds
        audio_path = os.path.join(chunks_dir, chunk_file)
        #audio = whisper.load_audio(audio_path)
        #audio = whisper.pad_or_trim(audio)
        model = whisper.load_model("medium")
        result = model.transcribe(audio_path)

        # write the recognized text to a file
        output_file = os.path.join(output_dir, chunk_file.replace('.wav', '.txt'))
        with open(output_file, 'w') as f:
            f.write(result["text"])

        print(f'Transcribed {chunk_file} and saved transcription to {output_file}')

# Use the function
#transcribe_and_save(chunks_dir="./chunks/", output_dir="./transcribed/")

