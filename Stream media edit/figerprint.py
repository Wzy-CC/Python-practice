# --------------- 导入模块 ---------------
import pyaudio
import wave
import numpy as np
import matplotlib.pylab as plt

file_wav = wave.open(r"test.wav","rb")                  # 打开一个wav文件（wave对象）
file_params = file_wav.getparams()                       # 参数传递：声道数, 量化位数（byte单位），采样频率，采样点数, 压缩类型,压缩类型的描述
print(file_params)
_channels,_sampwidth,_framerate,_nframes = file_params[:4]
str_data = file_wav.readframes(_nframes)                 # 返回一堆二进制字符串
file_wav.close()

narray_data = np.fromstring(str_data,np.short)
narray_data.shape = -1,2
narray_data = narray_data.T                              # narry_data：[[左声道],[右声道]]
time = np.arange(0,_nframes)*(1.0/_framerate)

L_fft = abs(np.fft.fft(narray_data[0]))                  # 左声道向量abs
L_fft_half = L_fft[:int(len(narray_data[0])/2)]               # 取半

R_fft = abs(np.fft.fft(narray_data[1]))                  # 右声道向量
R_fft_half = R_fft[:int(len(narray_data[1])/2)]               # 取半

FRE_FP = [L_fft_half,R_fft_half]

# narray_data[0] narray_data[1] 为时域指纹
# L_fft_half R_fft_half 为频域指纹

# --------------- 绘制波形 ---------------

# plt.subplot(221)
# plt.plot(time, narray_data[0])
# plt.xlabel("time(L)")
#
# plt.subplot(222)
# plt.plot(time, narray_data[1], c="g")
# plt.xlabel("time(R)")
#
# plt.subplot(223)
# plt.plot(L_fft_half)
# plt.xlabel("FFT(L)")
#
# plt.subplot(224)
# plt.plot(R_fft_half , c="g")
# plt.xlabel("FFT(R)")
#
# plt.show()

# --------------- 音乐数据库 --------------

music = "《出埃及记》"

# --------------- 音频检索 ---------------

file_x_wav = wave.open(r"x.wav","rb")                       # 打开一个未知wav文件（wave对象）
file_x_params = file_x_wav.getparams()                       # 参数传递：声道数, 量化位数（byte单位），采样频率，采样点数, 压缩类型,压缩类型的描述
x_channels,x_sampwidth,x_framerate,x_nframes = file_x_params[:4]
str_x_data = file_x_wav.readframes(x_nframes)                # 返回一堆二进制字符串
file_x_wav.close()

# 时域匹配：

narray_x_data = np.fromstring(str_x_data,np.short)
narray_x_data.shape = -1,2
narray_x_data = narray_x_data.T                              # narry_data：[[左声道],[右声道]]
time_x = np.arange(0,x_nframes)*(1.0/x_framerate)

eflag = 0                                                    # 阈值eflag

for i in range(len(narray_x_data[0])):
    if narray_x_data[0][i] != narray_data[0][i]:
        eflag =+ 1

if eflag >= len(narray_data[0])/2:
    print("未识别到此歌曲，请重试：")
else:
    print("时域分析：这首歌是%s"%music)

# 频域匹配：

L_x_fft = abs(np.fft.fft(narray_x_data[0]))                  # 左声道向量abs
L_x_fft_half = L_x_fft[:int(len(narray_x_data[0])/2)]               # 取半

R_x_fft = abs(np.fft.fft(narray_x_data[1]))                  # 右声道向量
R_x_fft_half = R_fft[:int(len(narray_x_data[1])/2)]               # 取半

FRE_X_FP = [L_x_fft_half,R_x_fft_half]

fflag = 0                                                    # 阈值eflag

for i in range(len(R_x_fft_half)):
    if R_x_fft_half[i] != R_fft_half[i]:
        eflag =+ 1

if fflag >= len(R_x_fft_half)/2:
    print("未识别到此歌曲，请重试：")
else:
    print("频域分析：这首歌是%s"%music)
