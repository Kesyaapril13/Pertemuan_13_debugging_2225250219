def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


data = [80, 60, 90, 70]
print("Rata-rata:", hitung_rata_rata(data))