"""Latihan 2 - Sistem Data Mahasiswa (dictionary, NIM sebagai key)."""


def cari_mahasiswa(data, nim):
    """Mengembalikan data mahasiswa berdasarkan NIM, atau None jika tidak ada."""
    return data.get(nim)


def tambah_mahasiswa(data, nim, nama, kelas, nilai):
    """Menambah mahasiswa baru. Mengembalikan False jika NIM sudah ada."""
    if nim in data:
        return False
    data[nim] = {"nama": nama, "kelas": kelas, "nilai": nilai}
    return True


def ubah_nilai(data, nim, nilai_baru):
    """Mengubah nilai mahasiswa. Mengembalikan False jika NIM tidak ditemukan."""
    if nim in data:
        data[nim]["nilai"] = nilai_baru
        return True
    return False


def rata_rata_nilai(data):
    """Rata-rata nilai seluruh mahasiswa; 0 jika data kosong."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)


def tampilkan_mahasiswa(data, nim):
    hasil = cari_mahasiswa(data, nim)
    if hasil is not None:
        print(f"{nim}: {hasil}")
    else:
        print("Data tidak ditemukan")


def main():
    data_mahasiswa = {
        "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
        "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
        "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
        "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
        "A005": {"nama": "Eka", "kelas": "A", "nilai": 88},
    }

    print("== Pencarian ==")
    tampilkan_mahasiswa(data_mahasiswa, "A003")   # ada
    tampilkan_mahasiswa(data_mahasiswa, "A999")   # tidak ada

    print("\n== Pembaruan nilai A002 menjadi 82 ==")
    ubah_nilai(data_mahasiswa, "A002", 82)
    print(data_mahasiswa["A002"])

    print("\n== Penambahan A006 ==")
    tambah_mahasiswa(data_mahasiswa, "A006", "Fajar", "B", 80)
    print("A006 tersedia:", "A006" in data_mahasiswa)

    print("\n== Rekap seluruh data ==")
    for nim, info in data_mahasiswa.items():
        print(nim, info)

    print(f"\nRata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")


if __name__ == "__main__":
    main()
