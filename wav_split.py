from pydub import AudioSegment
import math
import os

def split_audio(file, length_millis, overlap_millis, output_dir):
    audio = AudioSegment.from_wav(file)
    chunks = make_chunks(audio, length_millis, overlap_millis)

    # Make directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(os.path.join(output_dir, chunk_name), format="wav")

def make_chunks(audio, length_millis, overlap_millis):
    chunks = []
    num_chunks = math.ceil(len(audio) / (length_millis - overlap_millis))
    for i in range(num_chunks):
        start_time = i * (length_millis - overlap_millis)
        end_time = min((i * (length_millis - overlap_millis)) + length_millis, len(audio))
        chunk = audio[start_time:end_time]
        chunks.append(chunk)
    return chunks

#split_audio("dnd-2.wav", 10 * 60 * 1000, 2 * 1000, "chunks")  # 10 minutes and 2 seconds in milliseconds

