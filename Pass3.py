import os

root_path = os.path.dirname(__file__)
data = os.path.join(root, 'date')

res = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
key = [ 0, 10, 100, 1000, 10000, 100000, 1000000]
for root, dirs, files, in os.walk(data):
    for _file in files:
        z = os.star(os.path.join(root, _file)).st_size
        if z == 0:
            result[0] += 1
            continue
        for i, keys in enumerate(key):
            if i == len(key) - 1:
                print(f'Очень большой файл {_file}')
                break
            if keys < z <= key[i + 1]:
                res[key[i + 1]] += 1
                break
print(res)