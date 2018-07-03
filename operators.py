from student import StuAddr

_info = {'序号':'sn','姓名':'name','年龄':'age','成绩':'score', '地址':'address'}
ops_dict = {'1':'add_stu',
             '2':'query',
             '3':'del_stu',
             '4':'modify_score',
             '5':'query',
             '6':'query',
             '7':'query',
             '8':'query',
             '9':'write_data',
             '10':'read_data',
             '11':'modify_addr',
             'q':'quit'
             }
_DATA_PATH = 'si.txt'
L = []

def input_student():
    stu_data = []
    while True:
        tmp = []
        for k in _info:
            if k == '序号':
                continue
            input_info = input('请输入学生%s(输入空结束输入)：' % k)
            if not input_info and k == '姓名':
                return stu_data
            tmp.append(input_info)
        else:
            n, a, s, addr = tmp
            student = StuAddr(len(L) + len(stu_data) + 1, n, a, s, addr)
            stu_data.append(student)
    return stu_data

def output_student(lst):
    line1 = ' ' * 8 + '+' + ('-' * 12 + '+') * len(_info)
    line2 = ' ' * 8 + '|' + '%s|' * len(_info)
    print(line1)
    info_values = [x.center(12) for x in _info.values()]
    print(line2 % tuple(info_values))
    print(line1)
    for stu in lst:
        print(line2 % tuple(map(lambda x:str(x).center(12) if isinstance(x, int) else x.center(12), stu.get_stu_data())))
        print(line1)

def add_stu(op):
    lst = input_student()
    if not lst:
        print('输入空，无任何信息添加')
    else:
        L.extend(lst)
        print('添加成功')
    return
def del_stu(op):
    index = get_student('删除')
    if index != None:
        L.pop(index)
        print('删除成功!')

def modify_score(op):
    index = get_student('修改成绩')
    if index != None:
        print(L[index].get_stu_name(), '的旧成绩为：', L[index].get_stu_score())
        score = input('请输入新成绩：')
        L[index].set_stu_score(score)
        print('序号为',L[index].get_stu_sn() , '的', L[index].get_stu_name(),'的成绩已修改为：', score)
    return

def modify_addr(op):
    index = get_student('修改地址')
    if index != None:
        print(L[index].get_stu_name(), '的旧地址为：', L[index].get_stu_addr())
        addr = input('请输入新地址：')
        L[index].set_stu_addr(addr)
        print('序号为',L[index].get_stu_sn() , '的', L[index].get_stu_name(),'的地址已修改为：', addr)
    return

def get_student(op_str):
    name = input('请输入您想' + op_str + '学生的姓名：')
    indexs = []
    for i in range(len(L)):
        if L[i].get_stu_name() == name:
            indexs.append(i)
    if not indexs:
        print(name,'的信息未找到，', op_str, '操作失败！')
        return
    if len(indexs) == 1:
        return indexs[0]
    else:
        try:
            sn = int(input('有重名，请输入学生对应的序号：'))
            j = indexs.index(sn - 1)
            return indexs[j]
        except ValueError:
            print(op_str, '操作失败！')
            print('与姓名信息不相符或输入序号格式错误，请核对并重新操作！！！')
            return

def query(op):
    lst = []
    if op == '2':   #所有信息
        lst = L
    elif op == '5': #成绩高到低
        lst = sorted(L, key=lambda x:int(x.score),reverse=True)
    elif op == '6': #成绩低到高
        lst = sorted(L, key=lambda x:int(x.score))
    elif op == '7': #年龄高到低
        lst = sorted(L, key=lambda x:int(x.age),reverse=True)
    elif op == '8': #年龄低到高
        lst = sorted(L, key=lambda x:int(x.age))
    output_student(lst)
def write_data(op):
    try:
        f = open(_DATA_PATH, 'w')
        for x in L:
            x.save_to_file(f)
        f.flush()
        f.close()
    except IOError:
        print('添加失败，请重新添加！！！')
def read_data(op):
    L.clear()
    try:
        f = open(_DATA_PATH)
        i = 1
        while True:
            s = f.readline()
            if not s:
                f.close()
                return
            lst = s.rstrip('\n').split(',')
            if len(lst) == 4:
                lst.append(i)
                i += 1
                n, a, s, addr, sn = lst
            else:
                sn, n, a, s, addr = lst
            L.append(StuAddr(sn, n, a, s, addr))
    except IOError:
        print('数据读取失败！！！')