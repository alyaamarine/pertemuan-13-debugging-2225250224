def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    # FIX: Menggunakan len(nilai) agar pembagi dinamis sesuai jumlah data
    return sum(nilai) / len(nilai)

def status(nilai):
    # FIX: Menggunakan >= agar nilai tepat 60 dinyatakan Lulus
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    # FIX: Inisialisasi menggunakan elemen pertama dari list nilai
    tertinggi = nilai[0]
    for x in nilai[1:]:
        # FIX: Operator perbandingan harus '>' untuk mencari nilai tertinggi
        if x > tertinggi:
            tertinggi = x
    return tertinggi

# =====================================================================
# BLOK JALAN UTAMA PROGRAM DAN RETEST TEST CASE WAJIB DOSEN
# =====================================================================
if __name__ == "__main__":
    print("=== HASIL RETEST SETELAH PERBAIKAN BUG ===\n")
    
    # T1: Rata-rata list normal
    nilai_t1 = [70, 80, 75, 85, 65]
    print(f"[T1] Rata-rata: {hitung_rata_rata(nilai_t1)} (Expected: 75.0)")
    
    # T2: Rata-rata list dengan panjang berbeda
    nilai_t2 = [90, 85, 95]
    print(f"[T2] Rata-rata: {hitung_rata_rata(nilai_t2)} (Expected: 90.0)")
    
    # T3: Status kelulusan tepat di nilai batas (60)
    print(f"[T3] Status nilai 60: {status(60)} (Expected: Lulus)")
    
    # T4: Status kelulusan di bawah nilai batas (59)
    print(f"[T4] Status nilai 59: {status(59)} (Expected: Tidak lulus)")
    
    # T5: Mencari nilai tertinggi dalam kumpulan list data
    nilai_t5 = [70, 85, 90, 65, 80]
    print(f"[T5] Nilai tertinggi: {nilai_tertinggi(nilai_t5)} (Expected: 90)")