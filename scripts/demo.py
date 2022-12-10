#!/usr/bin/python3
import pyaudio
import wave
import time
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "/home/peter/code/recording/files/output.mp3"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))

time.sleep(0.5)   #停2秒后进入下一个函数

r = sr.Recognizer()    #调用识别器
test = sr.AudioFile("/home/peter/code/recording/files/output.mp3")   #导入语音文件
with test as source:       
    audio = r.record(source)
type(audio)
c=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
print(c)

time.sleep(0.5)

chunk=1024  #2014kb
wf1=wave.open(r"/home/peter/code/recording/files/school.mp3",'rb')
p1=pyaudio.PyAudio() 
stream1=p.open(format=p.get_format_from_width(wf1.getsampwidth()),
               channels=wf1.getnchannels(),
               rate=wf1.getframerate(),
               output=True)
data1 = wf1.readframes(chunk)  # 读取数据
    
wf2=wave.open(r"/home/peter/code/recording/files/team.mp3",'rb')
p2=pyaudio.PyAudio()
stream2=p.open(format=p.get_format_from_width(wf2.getsampwidth()),
               channels=wf2.getnchannels(),
               rate=wf2.getframerate(),
               output=True)
 
data2 = wf2.readframes(chunk)  # 读取数据

if '学校' in c:
    while True:
        data1=wf1.readframes(chunk)
        if data1=="":
            break
        stream1.write(data1)
    stream1.stop_stream()   # 停止数据流
    stream1.close()
    p1.terminate()  # 关闭 PyAudio
    print('play函数结束！')
    if __name__ == '__main__':
        audio_file='/home/peter/code/recording/files/school.mp3'  #指定录音文件
              #播放录音文件

if '队' or '对' in c:
    while True:
        data2=wf2.readframes(chunk)
        if data2=="":
            break
        stream2.write(data2)
    stream2.stop_stream()   # 停止数据流
    stream2.close()
    p2.terminate()  # 关闭 PyAudio
    print('play函数结束！')
    if __name__ == '__main__':
        audio_file='/home/peter/code/recording/files/team.mp3'  #指定录音文件
                  #播放录音文件
       
    
