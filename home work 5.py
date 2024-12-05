
Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del Geeks['bag']
Geeks['address'] = 'Ибраимова 103'
Geeks['phone'] = '+996507052018'
Geeks['instagram'] = '@geeks_edu'
new_courses = ['Bacend', 'UX/UI-дизайнер', 'Mobile-разработчик', 'Fullstack-разработчик']
Geeks['courses'].extend(new_courses)
Geeks['courses'] = set(Geeks['courses'])
Geeks['foundation_date'] = '2018'
print(f"Количество курсов: {len(Geeks['courses'])}")
for key, value in Geeks.items():
    print(f"{key}: {value}")
