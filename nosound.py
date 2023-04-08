import os
import shutil
from pydub import AudioSegment

def is_silent(audio, silence_threshold=-50.0):
    return audio.dBFS < silence_threshold

def move_silent_files(input_dir, output_dir, silence_threshold=-50.0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            file_path = os.path.join(input_dir, file_name)
            audio = AudioSegment.from_wav(file_path)

            if is_silent(audio, silence_threshold):
                dest_path = os.path.join(output_dir, file_name)
                shutil.move(file_path, dest_path)
                print(f"Moved silent file '{file_name}' to 'nosound' folder")

if __name__ == "__main__":
    input_dir = "input"  # .wavファイルが格納されているディレクトリ
    output_dir = "nosound"  # 無音の.wavファイルを移動するディレクトリ
    silence_threshold = -50.0  # 音量がこの値（デシベル）未満の場合、ファイルを無音と判断

    move_silent_files(input_dir, output_dir, silence_threshold)
