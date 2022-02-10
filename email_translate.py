import csv


#input name of the personel 
l_name = input('Введите фамилию сотрудника: ')
last_name_upper = l_name.upper()

f_name = input('Введите имя сотрудника: ')
first_name_upper = f_name.upper()

#change the file path for your file location
with open('F:/teaching/python/email_generation/translit.csv', newline ='', encoding='utf-8') as f:
    freader = csv.reader(f, delimiter= ' ', quotechar='|')
    
    translit_dict = {}
    last_name_transl = ''
    

    for row in freader:
       x = [s.replace('"', "").split(',') for s in row] #get rid of quotes and split list by comma
       translit_dict.update(dict(x))

    
    # find letter in dictionary and make new translit string
    for let in last_name_upper:
        let = str(translit_dict.get(let))
        last_name_transl = last_name_transl + let.lower()

    #get first letter of first name
    first_symbol = str(translit_dict.get(first_name_upper[0]))

    #concatenate first letter and translit string
    output = first_symbol.lower() + '.' + last_name_transl
    print(output)
    
    
