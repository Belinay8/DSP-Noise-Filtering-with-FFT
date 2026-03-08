import numpy as np        # matematik işlemleri ve sinyal üretmek için
import matplotlib.pyplot as plt        # grafik çizme
from scipy.signal import butter, filtfilt    # dijital filtre oluşturmak için
def generate_signal(t, f1,f2):                 #Sinyal Üret
    #iki frekanslı sinyal üret
    signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)
    return signal

def add_noise(signal, noise_level):            #Gürültü Ekle
    #rastgele gürültü
    noise = np.random.normal(0, noise_level, len(signal))
    
    #sinyale gürültü ekle
    noisy_signal = signal + noise
    return noisy_signal, noise

def compute_fft(signal, fs):
    # frekans bileşenlerin genliği
    fft_vals = np.fft.fft(signal)

    #frekans ekseni
    freq = np.fft.fftfreq(len(signal), 1/fs) #(örnek sayısı, örnekleme aralığı)
    #sonuç frekans spekturumu
    return freq, fft_vals

def apply_lowpass_filter(signal, fs):
    #filtre oluştur
    b, a =butter(4, 10/(fs/2), 'low')

    #filtre uygula
    filtered_signal = filtfilt(b, a, signal)

    return filtered_signal

def calculate_snr(signal, noise):   # SNR hesaplayan bir fonk
    signal_power = np.mean(signal**2) # sinyal gücü sinyaldeki değerlerin karesinin ortalamasını azaltır
    noise_power = np.mean(noise**2)
    snr = 10*np.log10(signal_power / noise_power)  #SNR hesapla (dB)

    return snr


def plot_results(t, signal, noisy_signal, freq,
    fft_vals, fft_filtered, snr_before, snr_after):

    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.plot(t, signal)
    plt.title("Clean Signal")

    plt.subplot(2,2,2)
    plt.plot(t, noisy_signal)
    plt.title("Noisy Signal")

    plt.subplot(2,2,3)
    plt.plot(freq, np.abs(fft_vals))
    #plt.plot(freq[:len(freq)//2], np.abs(fft_vals[:len(freq)//2])) 
    #negatif frekasları çizmez
    plt.title("FFT Before Filtering")

    plt.subplot(2,2,4)
    plt.plot(freq, np.abs(fft_filtered))
    plt.title("FFT After Filtering")

    plt.figtext(0.5, 0.01,
            f"SNR Before Filtering: {snr_before:.2f} dB | SNR After Filtering: {snr_after:.2f} dB",
            ha="center", fontsize=12)
    
    plt.tight_layout()
    plt.show()



def main():

    fs = 500
    t = np.linspace(0,1,fs, endpoint=False)

    signal = generate_signal(t,5,20)

    noisy_signal,_ = add_noise(signal,0.5)

    freq,fft_vals = compute_fft(noisy_signal,fs)

    filtered_signal = apply_lowpass_filter(noisy_signal,fs)

    _,fft_filtered = compute_fft(filtered_signal,fs)

    # SNR hesapla
    # filtre öncesi gürültü
    noise_before = noisy_signal - signal
    snr_before = calculate_snr(signal, noise_before)

    # filtre sonrası gürültü
    noise_after = noisy_signal - filtered_signal
    snr_after = calculate_snr(filtered_signal, noise_after)

    plot_results(t, signal, noisy_signal, freq, fft_vals, fft_filtered, snr_before, snr_after)

if __name__ == "__main__":
    main()
