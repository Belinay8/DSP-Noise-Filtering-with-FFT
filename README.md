# DSP Noise Filtering with FFT

This project demonstrates a simple Digital Signal Processing (DSP) pipeline implemented in Python.

Bu proje Python kullanarak basit bir **Sayısal Sinyal İşleme (DSP)** akışını göstermektedir.

The program generates a synthetic signal, adds Gaussian noise, analyzes the frequency spectrum using FFT, and applies a Butterworth low-pass filter to remove high-frequency noise.

Program sentetik bir sinyal üretir, bu sinyale Gaussian gürültü ekler, FFT kullanarak frekans spektrumunu analiz eder ve yüksek frekanslı gürültüyü azaltmak için Butterworth düşük geçiren filtre uygular.

---

# Features / Özellikler

- Signal generation with multiple frequencies  
  Çoklu frekanslardan oluşan sinyal üretimi

- Gaussian noise addition  
  Gaussian (rastgele) gürültü ekleme

- Frequency spectrum analysis using FFT  
  FFT kullanarak frekans spektrumu analizi

- Low-pass Butterworth filtering  
  Butterworth düşük geçiren filtre uygulaması

- Signal-to-Noise Ratio (SNR) evaluation  
  Sinyal-Gürültü Oranı (SNR) hesaplama

- Time-domain and frequency-domain visualization  
  Zaman domeni ve frekans domeni görselleştirmesi

---

# Technologies Used / Kullanılan Teknolojiler

- Python  
- NumPy  
- SciPy  
- Matplotlib  

---

# Signal Processing Pipeline / Sinyal İşleme Akışı

1. Generate a clean signal (5 Hz + 20 Hz)  
   Temiz bir sinyal oluşturulur (5 Hz + 20 Hz)

2. Add Gaussian noise  
   Sinyale Gaussian gürültü eklenir

3. Compute FFT to analyze frequency components  
   Frekans bileşenlerini analiz etmek için FFT uygulanır

4. Apply a Butterworth low-pass filter  
   Butterworth düşük geçiren filtre uygulanır

5. Compare FFT before and after filtering  
   Filtre öncesi ve sonrası frekans spektrumları karşılaştırılır

6. Calculate SNR improvement  
   Filtreleme sonrası SNR iyileşmesi hesaplanır

---

# Example Output / Örnek Çıktı

The program visualizes the following:

Program aşağıdaki grafikleri görselleştirir:

- Clean Signal (Temiz Sinyal)
- Noisy Signal (Gürültülü Sinyal)
- FFT Before Filtering (Filtre Öncesi FFT)
- FFT After Filtering (Filtre Sonrası FFT)
- SNR Before and After Filtering (Filtreleme Öncesi ve Sonrası SNR)


