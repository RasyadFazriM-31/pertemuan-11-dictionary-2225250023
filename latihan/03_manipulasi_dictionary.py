data = {"nama": "Ayu", "nilai": 85}

data["kelas"] = "A"      # menambah pasangan baru
data["nilai"] = 90       # mengubah value
print(data)

kelas = data.pop("kelas")  # menghapus dan mengembalikan value
print(kelas)
print(data)

data.update({"nilai": 92})
print(data)
