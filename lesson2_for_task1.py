stock = [1,5,2,4,16,789,33,56,943,20]
for a in stock:
    print(a+1)

c = input('Введите строку: ')
for b in list(c):
    #print(f'{b.split()}' )
    print(b)

oc_school = 0
school =   [{'school_class': '4a', 'scores': [3,4,4,5,2]},
            {'school_class': '5a', 'scores': [5,3,1,2,2]},
            {'school_class': '9b', 'scores': [4,3,1,1,5]}
            ]
for oc in school:
    oc_avg_class=sum(oc['scores'])/len(oc['scores'])
    cl=oc['school_class']
    print(f'Средний балл по классу {cl} : {oc_avg_class}')
    oc_school += oc_avg_class


bb = oc_school/len(school)

print(f'Средний балл по школе = {bb}')