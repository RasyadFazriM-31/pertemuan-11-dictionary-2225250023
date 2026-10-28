"""Test case wajib Latihan 2 (jalankan: python3 praktik/test_data_mahasiswa.py)."""
import copy
from data_mahasiswa import (cari_mahasiswa, tambah_mahasiswa, ubah_nilai,
                            rata_rata_nilai)

DATA = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88},
}


def jalankan(id_tc, deskripsi, kondisi):
    status = "PASS" if kondisi else "FAIL"
    print(f"{id_tc} | {deskripsi:<45} | {status}")
    return kondisi


data = copy.deepcopy(DATA)
hasil = [
    jalankan("TC1", "Pencarian A003 menampilkan Citra",
             cari_mahasiswa(data, "A003")["nama"] == "Citra"),
    jalankan("TC2", "Pencarian A999 -> None (tanpa KeyError)",
             cari_mahasiswa(data, "A999") is None),
]
ubah_nilai(data, "A002", 82)
hasil.append(jalankan("TC3", "Nilai A002 berubah menjadi 82",
                      data["A002"]["nilai"] == 82))
tambah_mahasiswa(data, "A006", "Fajar", "B", 80)
hasil.append(jalankan("TC4", "Key A006 tersedia setelah ditambah",
                      "A006" in data))
hasil.append(jalankan("TC5", "Rekap items() memuat semua NIM",
                      [n for n, _ in data.items()] ==
                      ["A001", "A002", "A003", "A004", "A005", "A006"]))
hasil.append(jalankan("TC6", "Rata-rata data awal = 83.4",
                      abs(rata_rata_nilai(DATA) - 83.4) < 1e-9))
hasil.append(jalankan("TC7", "Rata-rata dictionary kosong = 0",
                      rata_rata_nilai({}) == 0))
hasil.append(jalankan("TC8", "Ubah nilai NIM tidak ada -> False",
                      ubah_nilai(data, "A999", 50) is False))

print(f"\nLulus {sum(hasil)}/{len(hasil)}")
raise SystemExit(0 if all(hasil) else 1)
