
def baca_nilai(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            isi = file.read().strip()

        if isi == "":
            print("File kosong.")
            return []

        nilai = []
        for baris in isi.splitlines():
            nilai.append(float(baris))

        return nilai

    except FileNotFoundError:
        print("File tidak ditemukan.")
        return []

    except ValueError:
        print("Data nilai tidak valid.")
        return []


data = baca_nilai("Kasus/nilai.txt")
print("Data nilai:", data)