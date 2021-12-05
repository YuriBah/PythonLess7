import os

root_path = os.path.dirname(__file__)
pro_name = 'my_project1'
paths = [os.path.join(pro_name, 'settings'),
         os.path.join(pro_name, 'mainapp'),
         os.path.join(pro_name, 'adminapp'),
         os.path.join(pro_name, 'authapp')]
for _path in paths:
    os.makedirs(os.path.join(root_path, _path), exist_ok=True)

def create_one(name):
    try:
        os.mkdir(name)
    except FileExistsError as a:
        print(f'dir exist: {a.filename}')
    return 0

def create_two(one, *dirs):
    for el in dirs:
        try:
            dir_path = os.path.join(one, el)
            os.mkdir(dir_path)
        except FileExistsError as a:
            print(f'dir exits: {a.filename}')
    return 0

def create_finish(main_dir):
    create_one(main_dir)
    create_two(main_dir, 'settings', 'mainapp','adminapp', 'authapp')
