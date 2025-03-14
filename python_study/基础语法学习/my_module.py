__all__ = ["test2"]
def test(a, b):
    print(a + b)

def test2(a, b):
    print(a - b)

# test(1, 2)  # 在导入时会自动执行
# 只在当前文件调用该函数，其他导入的文件不符合该执行条件
if __name__ == "__main__":
    test(1, 2)