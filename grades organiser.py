#organising student grade
#create a list to store and calculate grade for student
grades=[45,67,23,19,89,76]
print(grades)
a=grades.append(98)
print(a)
avg=sum(grades)/len(grades)
print(avg)
highest_marks=max(grades)
lowest_marks=min(grades)
print(f"the highest mark is {highest_marks}")
print(f"the lowest mark is {lowest_marks}")