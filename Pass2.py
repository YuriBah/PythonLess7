import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_project1')
pro_dir = os.path.join(os.path.dirname(__file__),'my_project1', 'templates')

if not os.path.exists(pro_dir):
    os.makedirs(pro_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir_ in dirs:
            if not os.path.exists(os.path.join(pro_dir, dir_)):
                os.makedirs(os.path.join(pro_dir, dir_))
        for file in files:
            first_file = os.path.join(root, file)
            second_file = os.path.join(pro_dir, os.path.basename(root))
            if not os.path.dirname(first_file) == second_file:
                shutil.copy(first_file, second_file)