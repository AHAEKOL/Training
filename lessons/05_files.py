import os

# print current working directory
print("Current working directory is: " + os.getcwd())

# create directory files
os.mkdir('files')

# create files f1.txt, f2.txt ... f10.txt in directory files
for x in range(1, 11):
    fp = os.path.join('files', f'f{x}.txt')
    open(fp, 'w').close()

# print all in current directory
for root, dirs, files in os.walk(".", topdown=True):
   for name in sorted(files):
       print(os.path.abspath(os.path.join(root, name)))

# print file content
with open('05_files.py', 'r') as file:
    print(file.read())


#removing the directory with files
import shutil

shutil.rmtree('files')
