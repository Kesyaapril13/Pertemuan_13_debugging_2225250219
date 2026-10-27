# Pertemuan 13 - Debugging, Tracing, dan Testing

## Identitas
- Nama: Kesya Nur Aprilliani
- NIM: 2225250219
- Mata Kuliah: Algoritma dan Pemrograman

## Deskripsi
Praktikum ini membahas proses debugging, tracing, dan testing pada program Python. Kegiatan dilakukan dengan mengidentifikasi kesalahan program, memperbaiki kode, menjalankan pengujian, serta memeriksa hasil program menggunakan Visual Studio Code dan GitHub.

## Struktur Folder
```text
Pertemuan_13_debugging_2225250219/
├── Kasus/
│   ├── 01_batas_kelulusan.py
│   ├── 02_rata_rata.py
│   ├── 03_file_nilai.py
│   └── nilai.txt
├── Latihan/
├── Praktik/
└── README.md
```

## Tujuan
1. Memahami proses debugging pada program Python.
2. Melakukan tracing untuk memeriksa jalannya program.
3. Menguji program menggunakan beberapa test case.
4. Menangani kesalahan yang terjadi saat program dijalankan.
5. Mendokumentasikan hasil pengujian program.

## Cara Menjalankan
Pastikan terminal berada di folder utama proyek.

Jalankan Kasus 1:
```bash
python Kasus/01_batas_kelulusan.py
```

Jalankan Kasus 2:
```bash
python Kasus/02_rata_rata.py
```

Jalankan Kasus 3:
```bash
python Kasus/03_file_nilai.py
```

## Kasus 1 - Batas Kelulusan
Program digunakan untuk memeriksa status kelulusan berdasarkan nilai. Pengujian dilakukan pada nilai di bawah, tepat pada, dan di atas batas kelulusan untuk menemukan kesalahan kondisi.

## Kasus 2 - Rata-rata
Program digunakan untuk menghitung nilai rata-rata. Pengujian dilakukan untuk memastikan perhitungan sesuai dengan data masukan.

## Kasus 3 - File Nilai
Program digunakan untuk membaca data nilai dari file teks. Program menangani kondisi file kosong, file tidak ditemukan, dan data yang tidak valid.


### Test Case Kasus 3 - File Nilai

| No. | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | File `nilai.txt` berisi angka 80, 75, 90, dan 85 | Data nilai ditampilkan | Data nilai: [80.0, 75.0, 90.0, 85.0] | Berhasil |
| 2 | File `nilai.txt` kosong | Pesan "File kosong." ditampilkan | File kosong. Data nilai: [] | Berhasil |
| 3 | File `nilai.txt` berisi teks `abc` | Pesan "Data nilai tidak valid." ditampilkan | Data nilai tidak valid. Data nilai: [] | Berhasil |
| 4 | File tidak ditemukan | Pesan "File tidak ditemukan." ditampilkan | File tidak ditemukan. Data nilai: [] | Berhasil |

### Kesimpulan Kasus 3

Program berhasil membaca data nilai dari file teks dan menangani beberapa kondisi kesalahan, yaitu file kosong, data yang tidak valid, serta file yang tidak ditemukan. Pengujian dilakukan menggunakan beberapa test case untuk memastikan program memberikan keluaran sesuai dengan kondisi file.

## Kesimpulan
Debugging membantu menemukan dan memperbaiki kesalahan program. Tracing membantu memeriksa jalannya instruksi, sedangkan testing digunakan untuk memastikan program menghasilkan keluaran yang sesuai pada berbagai kondisi masukan.

## Teknologi
- Python
- Visual Studio Code
- Git
- GitHub
