def rata_rata(data):
    if len(data) == 0:
        return 0
    # Pembagi dinamis menggunakan len(data) bukan angka statis 5
    return sum(data) / len(data)

# Pengujian sesuai modul dengan argumen data list yang valid
print("Rata-rata:", rata_rata([70, 80, 90, 60, 75]))
print("Rata-rata list kosong:", rata_rata([]))