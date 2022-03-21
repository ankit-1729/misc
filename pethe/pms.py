class Property:
  p_reg_num = -1
  p_type = ''
  p_price = -1

  def __init__(self, p_reg_num, p_type, p_price):
    self.p_reg_num = p_reg_num
    self.p_type = p_type
    self.p_price = p_price

class PMS:
  p_list = []
  tax_payment_record = dict()

  def __init__(self, p_list, tax_payment_record):
    self.p_list = p_list
    self.tax_payment_record = tax_payment_record

  def compute_total_tax(self, p_reg_num, tax_year):
    p = None

    for _p in self.p_list:
      if _p.p_reg_num == p_reg_num:
        p = _p
        break
    
    if p == None:
      return 0

    t_year = self.tax_payment_record[p_reg_num]

    if t_year >= tax_year:
      return -1
    
    p_tax = 0.05 * p.p_price
    late_fine = 0

    if t_year < tax_year - 2:
      late_fine = 1000 * (tax_year - (t_year + 2))
    
    if t_year < tax_year - 10:
      self.p_list = [p for p in self.p_list if p.p_reg_num != p_reg_num]
    
    total_tax = p_tax + late_fine
    return int(total_tax)

def main():
  n = int(input())
  _p_list = []
  _tax_payment_record = dict()

  for _ in range(n):
    _p_reg_num = int(input())
    _p_type = input()
    _p_price = int(input())

    _p_list.append(Property(_p_reg_num, _p_type, _p_price))

  for _ in range(n):
    _p_reg_num = int(input())
    _tax_year = int(input())

    _tax_payment_record[_p_reg_num] = _tax_year

  pms = PMS(_p_list, _tax_payment_record)

  _p_reg_num = int(input())
  _tax_year = int(input())

  output = pms.compute_total_tax(_p_reg_num, _tax_year)

  if output == 0:
    print("Property not available.")
  elif output == -1:
    print("Tax already paid.")
  else:
    print(output)

  for p in pms.p_list:
    print(p.p_reg_num)

if __name__ == "__main__":
    main()