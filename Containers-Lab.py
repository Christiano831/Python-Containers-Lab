# Excercise 1:

students = ['CJ', 'Billy', 'Bob', 'Jack']
print(students[1])
print(students[-1])

# Excercise 2:

food = ('chicken', 'rice', 'beans', 'brocoli')
for f in food:
    print(f'{f} is a good food')

# Excercise 3:

for f in food[-2:]:
    print(f)

# Excercise 4:

home_town = {
    'city': 'Monterey',
    'state': 'California',
    'population': 3
}
print(f'I was born in {home_town['city']},{home_town['state']} - population of {home_town['population']})

# Excercise 5:

for key,val in home_town.items():
    print(f'{key} = {val}')

# Excercise 6:

cohort = []
for idx,student in enumerate(students): 
    cohort.append({'student': student, 'fav_food': food[idx]})
for student in cohort:
    print(student)

# Excercise 7:

awesome_students = [student for student in students]

for student in awesome_students:
    print(f'{student} is awesome!')

# Excercise 8:

a_foods = [f for f in food if 'a' in f]
for f in a_foods:
    print(f)