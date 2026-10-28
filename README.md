# Pertemuan 13 - Debugging dan Testing

Nama: Alya Mutiara Marine
NIM: 2225250224
Kelas: 3A

## Kasus
Jelaskan program yang diuji.
- Program yang diuji adalah aplikasi pengolah data nilai siswa/mahasiswa yang memuat beberapa fungsi utilitas utama, yaitu menghitung nilai rata-rata dari sebuah list, menentukan status kelulusan berdasarkan standar nilai batas bawah (threshold), serta mencari nilai tertinggi di dalam kumpulan data numerik.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
| :--- | :--- | :--- | :--- | :--- |
| T1 | `[70, 80]` | 75.0 | 30.0 (Salah pembagi) | Gagal (Awal) / Sukses (Fix) |
| T2 | `[85, 95, 90]` | 90.0 | 90.0 | Sukses |
| T3 | 60 | "Lulus" | "Tidak lulus" (Batas tidak masuk) | Gagal (Awal) / Sukses (Fix) |
| T4 | 59 | "Tidak lulus" | "Tidak lulus" | Sukses |
| T5 | `[75, 90, 80]` | 90 | 0 (Salah logika cari) | Gagal (Awal) / Sukses (Fix) |

## Bug Report
Jelaskan gejala, lokasi, akar penyebab, dan perbaikan.
1. **Bug 1: Pembagi Rata-rata Statis**
   - **Gejala:** Hasil perhitungan rata-rata menjadi salah saat jumlah elemen dalam list diubah.
   - **Lokasi:** Fungsi `hitung_rata_rata(nilai)`
   - **Akar Penyebab:** Pembagi nilai total menggunakan angka statis `5` (hardcoded).
   - **Perbaikan:** Mengubah nilai pembagi menjadi dinamis menggunakan fungsi `len(nilai)`.
2. **Bug 2: Batas Kelulusan Tidak Inklusif**
   - **Gejala:** Siswa yang mendapatkan nilai tepat `60` dilaporkan "Tidak lulus".
   - **Lokasi:** Fungsi `status(nilai)`
   - **Akar Penyebab:** Operator perbandingan yang digunakan hanya `>` (lebih besar dari).
   - **Perbaikan:** Mengubah operator perbandingan menjadi `>=` (lebih besar dari atau sama dengan).
3. **Bug 3: Logika Nilai Tertinggi Salah**
   - **Gejala:** Nilai tertinggi yang dikembalikan salah atau selalu bernilai awal `0`.
   - **Lokasi:** Fungsi `nilai_tertinggi(nilai)`
   - **Akar Penyebab:** Inisialisasi awal variabel `tertinggi` diset ke `0` (salah jika ada nilai negatif) dan penggunaan operator perbandingan `<` untuk mencari nilai maksimum.
   - **Perbaikan:** Inisialisasi variabel menggunakan elemen pertama list (`nilai[0]`) dan mengubah kondisi pembanding menjadi `x > tertinggi`.

## Retest
Catat hasil pengujian setelah perbaikan.
Hasil eksekusi final pada berkas `praktik_4_debugging.py` menunjukkan seluruh pengujian berhasil memenuhi ekspektasi:
- `[T1] Rata-rata: 75.0 (Expected: 75.0)` -> **Sukses**
- `[T2] Rata-rata: 90.0 (Expected: 90.0)` -> **Sukses**
- `[T3] Status nilai 60: Lulus (Expected: Lulus)` -> **Sukses**
- `[T4] Status nilai 59: Tidak lulus (Expected: Tidak lulus)` -> **Sukses**
- `[T5] Nilai tertinggi: 90 (Expected: 90)` -> **Sukses**

## Cara Menjalankan
python3 praktik/praktik_4_debugging.py

## Refleksi
Apa teknik debugging yang paling membantu dan mengapa?
- Teknik debugging yang paling membantu adalah **Tracing dengan Print Statement** dan **Penerapan Unit Testing/Test Cases**. Melalui penelusuran manual nilai variabel secara terstruktur dan membandingkan *Expected Output* dengan *Actual Output* pada terminal, lokasi ketidaksesuaian logika program (seperti salah pembagi ataupun salah operator perbandingan) dapat diidentifikasi secara cepat dan akurat tanpa merusak alur program utama.