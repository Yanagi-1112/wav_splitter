from pydub import AudioSegment

def convert_to_mono(input_file, output_file):
    # ステレオ音声ファイルを読み込む
    stereo_audio = AudioSegment.from_wav(input_file)

    # ステレオ音声をモノラルに変換
    mono_audio = stereo_audio.set_channels(1)

    # モノラル音声ファイルを出力
    mono_audio.export(output_file, format="wav")

# 入力ファイル名と出力ファイル名を指定して、モノラルに変換
input_file = "input_stereo.wav"
output_file = "output_mono.wav"
convert_to_mono(input_file, output_file)
