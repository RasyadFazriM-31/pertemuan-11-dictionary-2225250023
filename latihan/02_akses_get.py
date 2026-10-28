data = {"nama": "Ayu", "nilai": 85}

print(data.get("nama"))
print(data.get("kelas", "Belum ada"))

# Perbandingan: kurung siku pada key yang tidak ada menghasilkan KeyError
try:
    print(data["kelas"])
except KeyError:
    print("KeyError: key 'kelas' tidak tersedia")

# Memeriksa keberadaan key
if "nilai" in data:
    print("Nilai tersedia.")
