import nkf
import os

def get_file_paths():
    dir_root = '.'
    file_dir_paths = os.listdir(dir_root)
    return [f for f in file_dir_paths if os.path.isfile(os.path.join(dir_root, f))]

def write_to_utf8(path):
    f = open(path, 'r')
    str = f.read()
    f.close()

    str_utf8 = nkf.nkf('w', str)
    fout = open(path, 'w')
    fout.write(str_utf8)
    fout.close()

if __name__ == '__main__':
    paths = get_file_paths()
    for path in paths:
        write_to_utf8(path)
    print(paths)
