from wav_split        import split_audio
from whisper_convert  import transcribe_and_save
from transcribe_merge import concatenate_files

wavfile = 'dnd2.wav'
length_of_chunk = 1000 * 60 * 10 # Length of individual chunk in ms
chunks_dir = './chunks/'
overlap_millis = 2 # Length of chunk overlap in ms
transcribe_dir = './transcribe/'
transcribe_model = "medium" # Openai whisper transcribe model. Possible values: tiny, base, small, medium, large
final_filename = './transcribed_output.txt'

split_audio(wavfile, length_of_chunk, overlap_millis, chunks_dir)
transcribe_and_save(chunks_dir, transcribe_dir, model_name=transcribe_model)
concentrate_files(transcribe_dir, final_filename)
