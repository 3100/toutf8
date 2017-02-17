import nkf
import os

input_dir= './input'
output_dir= './output'

def get_file_names():
    file_dir_paths = os.listdir(input_dir)
    return [f for f in file_dir_paths if os.path.isfile(os.path.join(input_dir, f))]

def make_output_dir():
    if os.path.isdir(output_dir):
        return
    os.mkdir(output_dir)
    os.chmod(output_dir, 0777)

def write_to_utf8(file_name):
    input_path = os.path.join(input_dir, file_name)
    f = open(input_path, 'r')
    str = f.read()
    f.close()

    str_utf8 = nkf.nkf('w', str)
    save_path = os.path.join(output_dir, file_name)
    fout = open(save_path, 'w')
    fout.write(str_utf8)
    fout.close()

if __name__ == '__main__':
    make_output_dir()
    file_names = get_file_names()
    for file_name in file_names:
        write_to_utf8(file_name)
