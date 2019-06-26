# cho danh sách 5 sinh viên, in ra diem trung binh cua tung sinh vien, in sinh vien co diem toan cao nhat, nhap sdt va in ten sv neu co
students = []
A = {'name': 'A', 'age': 20, 'address': 'HANOI', 'Math': 8.0,
     'Physical': 7.0, 'Chemical': 7.8, 'phone': '0987654321'}
B = {'name': 'B', 'age': 20, 'address': 'HANOI', 'Math': 7.5,
     'Physical': 8.2, 'Chemical': 6.5, 'phone': '0381456981'}
C = {'name': 'C', 'age': 20, 'address': 'HANOI', 'Math': 8.9,
     'Physical': 8.0, 'Chemical': 8.6, 'phone': ['0916547892', '0937324672']}
students.append(A)
students.append(B)
students.append(C)
maxMath = 0
for i in students:
    average = (i['Math']+i['Physical']+i['Chemical'])/3
    print('The average score of student ', i['name'], ' is '+str(average))
    if maxMath < i['Math']:
        maxMath = i['Math']
        name = i['name']
print('The highest math score is ', maxMath, ' of student ', name)
phone = input('Enter phone number: ')
check = False
for i in students:
    if phone in i['phone']:
        print('This phone of ', i['name'])
        check = True
if not check:
    print('This phone no one')
