def tinh_bmi(chieu_cao, can_nang):
 
  return can_nang / (chieu_cao * chieu_cao)

def phan_loai_bmi(bmi):
 
  if bmi < 18.5:
    return "Thiếu cân lắm á nha ăn nhiều zô á nè"
  elif bmi < 25:
    return "chuẩn rồi đó nha"
  elif bmi < 30:
    return "Thừa cân"
  else:
    return "body bạn như Lê Thành Nhật"

chieu_cao = float(input("Nhập số đo chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = tinh_bmi(chieu_cao, can_nang)

print(f"Chỉ số BMI của bạn là: {bmi}")
print(f"Phân loại BMI: {phan_loai_bmi(bmi)}")
