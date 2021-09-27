# LATIHAN KOMPARASI DAN LOGIKA

# LATIHAN NOMOR 1 (------ 0 ++++++++++ 5 ------------- 8 +++++++++ 11 ---------)
inputUser = float(input("Masukkan angka yang bernilai \nlebih dari 0 dan kurang dari 5 atau \nlebih dari 8 dan kurang dari 11\n:"))

# ------ 0 +++++++++ 5 ---------
# LEBIH DARI 0 atau KURANG DARI 5
y = (inputUser > 0) and (inputUser < 5)
print("Lebih dari 0 atau Kurang dari 5 = ", y)

# -------- 8 ++++++++++ 11 ----------
# LEBIH DARI 8 atau KURANG DARI 11
x = (inputUser > 8) and (inputUser < 11)
print("Lebih dari 8 atau Kurang dari 11 = ", x)

# (------ 0 ++++++++++ 5 ------------- 8 +++++++++ 11 ---------)
isCorrect = y or x
print("Angka yang anda masukkan : ", isCorrect)

print("\n", 10*"=", "\n")

# LATIHAN NOMOR 2 (+++++++ 0 ------- 5 +++++++++++ 8 --------- 11 ++++++++)
inputUser = float(input("Masukkan angka yang bernilai \nkurang dari 0 \nlebih dari 5 atau kurang dari 8 \nlebih dari 11\n:"))

# +++++++ 0
# KURANG DARI 0 atau LEBIH DARI 5
y = (inputUser < 0)
print("Kurang dari 0 = ", y)

# -------- 5 +++++++++ 8 -----------
z = (inputUser > 5) and (inputUser < 8)
print("Lebih dari 5 atau Kurang dari 8 = ", z)

# 11 ++++++
# KURANG DARI 8 atau LEBIH DARI 11
x = (inputUser > 11)
print("Lebih dari 11 = ", x)

# (+++++++ 0 ------- 5 +++++++++++ 8 --------- 11 ++++++++)
isCorrect = y or z or x
print("Angka yang anda masukkan : ", isCorrect)