def conversion(number,system_num):
    integer_part_of_number=int(number)
    checking_for_an_integer=number-integer_part_of_number
    fractional_part_of_a_number=float('0.'+str(number)[str(number).index('.')+1:])
    line_2=''
    if integer_part_of_number==0:
        line_1='0'
    else:
        line_1=''
        while integer_part_of_number>0:
            line_1=str(integer_part_of_number%system_num)+line_1
            integer_part_of_number//=system_num
    frac_part=fractional_part_of_a_number
    part_of_the_result=fractional_part_of_a_number
    decimal_places=0
    while frac_part!=0 and decimal_places!=20:
        part_of_the_result=part_of_the_result*system_num
        residues_from_division=int(part_of_the_result)%system_num
        frac_part=part_of_the_result-int(part_of_the_result)
        line_2+=str(residues_from_division)
        decimal_places+=1
    if checking_for_an_integer==0:
        return print("Результат перевода числа",int(number),"в систему счисления с основанием",system_num,"равен: ",line_1)
    else:
        return print("Результат перевода числа",number,"в систему счисления с основанием",system_num,"равен:",line_1+'.'+line_2)


def number_input():
    while True:
        num=float(input("Введите число: "))
        if num<=0:
            print("Вы ввели отрицательное значение или 0! Повторите ввод!")
        if num>0:
            break
    return num

def number_system():
    while True:
        system=float(input("Введите целевую систему счисления(двоичная или восьмеричная): "))
        if int(system)!=8 and int(system)!=2:
            print("Вы ввели некорректную систему счисления! Повторите ввод!(двоичная или восьмеричная)")
        if int(system)==2 or int(system)==8:
            system=int(system)
            break
    return system

num_input=number_input()
num_system=number_system()

conversion(num_input,num_system)
        
