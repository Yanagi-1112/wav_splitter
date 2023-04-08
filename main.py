import os
from pydub import AudioSegment

def split_wav_file(input_file, output_dir, output_prefix, split_duration):
    # ファイルが存在することを確認
    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    # 出力ディレクトリが存在することを確認（存在しない場合は作成）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力ファイルを読み込む
    audio = AudioSegment.from_wav(input_file)
    total_duration = len(audio)
    split_duration = split_duration * 1000  # milliseconds

    # 分割
    for i in range(0, total_duration, split_duration):
        start = i
        end = i + split_duration
        split_audio = audio[start:end]
        split_file_name = f"{output_prefix}_{i//1000}s_to_{(i+split_duration)//1000}s.wav"
        split_file_path = os.path.join(output_dir, split_file_name)
        split_audio.export(split_file_path, format="wav")
        print(f"Exported '{split_file_path}'")

if __name__ == "__main__":
    input_file = "uedarena.wav"  # 入力ファイル名
    output_dir = "output"  # 分割ファイルを保存するディレクトリ
    output_prefix = "split"  # 分割ファイルのプレフィックス
    split_duration = 3  # 分割する秒数

    split_wav_file(input_file, output_dir, output_prefix, split_duration)
