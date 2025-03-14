def print_file_info(file_name):
    try:
        f = open(file_name, 'r', encoding = 'utf-8')
        print(f.read())
    except Exception as e:
        print(f"出现异常，异常信息为：{e}")
    else:
        f.close()

if __name__ == '__main__':
    print_file_info('C:/code/python_code/python_study/test.txt')

def append_to_file(file_name, data):
    try:
        f = open(file_name, 'a', encoding = 'utf-8')
        f.write(data)
    except Exception as e:
        print(f"出现异常，异常信息为：{e}")
    else:
        f.close()