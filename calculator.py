action = input('Выберите операцию: ')
while action != '+' and action != '-' and action != '*' and action != '/':
  print('Ошибка: такой операции не существует. Попробуйте еще раз.')
  action = input('Выберите операцию: ')
oper = int(input('Сколько операндов? '))
num_print = ''
for i in range(1, oper + 1):
  num = int(input(f"Введите операнд {i}: "))
  if i == 1:
    num_res = num
    num_print += str(num)
  else:
    if action == '+':
      num_res += num
      num_print += action + str(num)
    elif action == '-':
      num_res -= num
      num_print += action + str(num)
    elif action == '*':
      num_res *= num
      num_print += action + str(num)
    else:
      num_res /= num
      num_print += action + str(num)
print(num_print, '=', num_res)
print('Жыве Беларусь! Круто!')

