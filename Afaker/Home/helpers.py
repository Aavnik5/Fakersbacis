from faker import Faker
fake = Faker()

name = fake.name()
print(name)

from .models import *
import random
import datetime

def generate_fake_data():
    for i in range(0 , 20):
        departments = Department.objects.all()
        rand_index = random.randint(1 ,len(departments))

        student_obj = Student.objects.create(
            student_name = fake.name(),
            student_age = random.randint(18 , 54),
            student_dob = datetime.date.today(),
            student_email = fake.email(),
            department = departments[rand_index-1]
        )
        print('Student created')
        skills = list(Skills.objects.all())
        random.shuffle(skills)
        print(skills)
        
        random_list_count =  random.randint(0 , len(skills)-1)
        print(random_list_count)
        for skill in skills[0:random_list_count] :
            skill_obj = Skills.objects.get(id = skill.id)
            student_obj.skills.add(skill_obj)

            print('Student skill added ')
            print(student_obj)
