import os

def concatenate_files(input_dir, output_file):
    with open(output_file, 'w') as outfile:
        for filename in sorted(os.listdir(input_dir)):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_dir, filename)
                with open(file_path, 'r') as infile:
                    for line in infile:
                        outfile.write(line)
                outfile.write("\n")  # Add a newline character between files

#concatenate_files("./transcribed/", "combined_transcription.txt")

