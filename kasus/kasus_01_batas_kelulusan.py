def status_lulus(nilai):
    # Menggunakan >= 60 agar nilai 60 dinyatakan Lulus
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Pengujian awal sesuai modul
print("Uji nilai 75:", status_lulus(75))
print("Uji nilai 60:", status_lulus(60))
print("Uji nilai 59:", status_lulus(59))