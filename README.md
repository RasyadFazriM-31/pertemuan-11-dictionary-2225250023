# Pertemuan 11 - Dictionary/Map

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Dictionary bersarang dengan **NIM sebagai key** karena NIM unik dan langsung dipakai untuk mencari data. Value berupa dictionary berisi `nama`, `kelas`, dan `nilai`.
```python
{"A001": {"nama": "Ayu", "kelas": "A", "nilai": 85}, ...}
```

## Cara Menjalankan
Dari root folder proyek:
```
python3 praktik/data_mahasiswa.py
cd praktik && python3 test_data_mahasiswa.py
```
Latihan 1-6: `python3 latihan/01_dasar_dictionary.py` dst.

## Test Case (hasil aktual, dijalankan)
| Kasus | Input/aksi | Expected | Actual | Status |
|-------|-----------|----------|--------|--------|
| Pencarian tersedia | A003 | Data Citra ditampilkan | `{'nama': 'Citra', 'kelas': 'B', 'nilai': 92}` | PASS |
| Pencarian tidak tersedia | A999 | Pesan "Data tidak ditemukan" | Data tidak ditemukan | PASS |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 = 82 | 82 | PASS |
| Penambahan data | A006 | Key A006 tersedia | True | PASS |
| Rekap items() | semua | Semua NIM tampil | A001-A006 tampil | PASS |
| Rata-rata kelas | 6 mahasiswa setelah ubah dan tambah | 83.50 | 83.50 | PASS |
| Dictionary kosong | `{}` | 0 | 0 | PASS |

`test_data_mahasiswa.py`: 8/8 PASS.

## Refleksi
Kesalahan akses key yang perlu dihindari: `data["A999"]` menghasilkan `KeyError`. Perbaikannya memakai `data.get(nim)` yang mengembalikan `None`, lalu program menampilkan pesan yang jelas.

## Referensi/Bantuan
Bahan ajar Pertemuan 11, Python 3 Documentation (Dictionaries). Dibantu Claude untuk menyusun kode dan test; penulis wajib dapat menjelaskan isinya.
