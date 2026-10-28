def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Eksekusi Test Case untuk pembuktian
test_cases = [75, 60, 59]
for tc in test_cases:
    print(f"Input: {tc} -> Hasil Aktual: {status_lulus(tc)}")