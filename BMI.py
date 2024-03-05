def tinh_bmi(chieu_cao, can_nang):
  """
  Hàm tính chỉ số BMI

  Args:
      chieu_cao (float): Chiều cao (m)
      can_nang (float): Cân nặng (kg)

  Returns:
      float: Chỉ số BMI
  """
  return can_nang / (chieu_cao * chieu_cao)

def phan_loai_bmi(bmi):
  """
  Hàm phân loại BMI

  Args:
      bmi (float): Chỉ số BMI

  Returns:
      str: Phân loại BMI
  """
  if bmi < 18.5:
    return "Thiếu cân"
  elif bmi < 25:
    return "Bình thường"
  elif bmi < 30:
    return "Thừa cân"
  else:
    return "Béo phì"

chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = tinh_bmi(chieu_cao, can_nang)

print(f"Chỉ số BMI của bạn là: {bmi}")
print(f"Phân loại BMI: {phan_loai_bmi(bmi)}")
