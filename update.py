#USED FOR EASIER PUBLISH OF THIS MODULE, DONT RUN THIS BECAUSE IT WILL ERROR ON YOUR MACHINE
with open("some_student_le/really_not_good/__init__.py",'r') as f1, open("some_student_le_PyPI/some_student_le/really_not_good.py",'w') as f2:
  f2.write(''.join(f1.readlines()))
with open("some_student_le/pyproject.toml",'r') as f1, open("some_student_le_PyPI/pyproject.toml",'w') as f2:
  f2.write(''.join(f1.readlines()).replace("description = \"some student le ","description = \"").replace("really-not-good","some-student-le"))
  with open("some_student_le/README.md",'r') as f1, open("some_student_le_PyPI/README.md",'w') as f2:
    f2.write(''.join(f1.readlines()).replace("really_not_good","some_student_le.really_not_good"))