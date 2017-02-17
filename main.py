import chardet
import glob
import os
import shutil
import sys

input_dir= './input'
output_dir= './output'

def get_file_names(dir):
    return glob.glob(dir + '/**/*.*', recursive=True)

# 強制コピー。output_dirが存在する場合は削除してからコピーする
def make_copy(input_dir, output_dir):
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    shutil.copytree(input_dir, output_dir)

# 上書き
def write_to_utf8(path):
    f = open(path, 'rb')
    binary = f.read()
    f.close()
    estimated = chardet.detect(binary)['encoding']
    if (estimated == None):
        sys.stderr.write('判定できず: ' + path + '\r\n')
        return
    str_utf8 = binary.decode(estimated)

    fout = open(path, 'w')
    fout.write(str_utf8)
    fout.close()

if __name__ == '__main__':
    make_copy(input_dir, output_dir)
    file_names = get_file_names(output_dir)
    for file_name in file_names:
        write_to_utf8(file_name)
