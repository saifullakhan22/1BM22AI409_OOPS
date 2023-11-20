class student:
  pass

class marks:
  pass

student1 = student()
marks1 = marks()

is_student_instance = isinstance(student1,student)
is_marks_instance = isinstance(marks1 , marks)

is_student_subclass = issubclass(student,object)
is_marks_subclass = issubclass(marks,object)

print(f'student1 instance is an instance of class student? --> {is_student_instance}')
print(f'marks1 instance is an instance if class marks? --> {is_marks_instance}')
print(f'student subclass of object class? --> {is_student_subclass}')
print(f'marks subclass is an class?  --> {is_marks_subclass}')
