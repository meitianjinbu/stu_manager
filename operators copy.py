_info = {'姓名':'name','年龄':'age','成绩':'score'}
ops_dict = {'1':'add_stu',
             '2':'query',
             '3':'del_stu',
             '4':'modify_stu',
             '5':'query',
             '6':'query',
             '7':'query',
             '8':'query',
             '9':'write_data',
             '10':'read_data',
             'q':'quit'
             }
_DATA_PATH = 'si.txt'
L = []

def input_student():
    stu_data = []
    while True:
        student = {}
        for k,v in _info.items():
            input_info = input('请输入学生%s(输入空结束输入)：' % k)
            if not input_info:
                if student:
                    stu_data.append(student)
                return stu_data
            student[v] = input_info
        else:
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
        print(line2 % tuple(map(lambda x:stu[x].center(12) if x in stu else ' ' * 12, _info.values())))
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
    name = input('请输入您想删除学生的姓名：')
    # L = read_data()
    for lst in L:
        if lst['name'] == name:
            L.remove(lst)
            # write_data(L)
            print(name, '的信息删除成功!')
            return
    print(name,'的信息未找到，删除操作失败！')

def modify_stu(op):
    name = input('请输入需要修改成绩的学生姓名：')
    # L = read_data()
    for i in range(len(L)):
        if L[i]['name'] == name:
            score = input('请输入成绩')
            L[i]['score'] = score
            print(name,'的成绩已修改为：', score)
            # write_data(L)
            return
    print(name,'的信息未找到，修改操作失败！')

def query(op):
    lst = []
    if op == '2':   #所有信息
        lst = L
    elif op == '5': #成绩高到低
        lst = sorted(L, key=lambda x:int(x['score']),reverse=True)
    elif op == '6': #成绩低到高
        lst = sorted(L, key=lambda x:int(x['score']))
    elif op == '7': #年龄高到低
        lst = sorted(L, key=lambda x:int(x['age']),reverse=True)
    elif op == '8': #年龄低到高
        lst = sorted(L, key=lambda x:int(x['age']))
    output_student(lst)
def write_data(op):
    try:
        f = open(_DATA_PATH, 'w')
        for x in L:
            f.write(','.join(x.values()) + '\n')
        f.flush()
        f.close()
    except IOError:
        print('添加失败，请重新添加！！！')
def read_data(op):
    L.clear()
    try:
        f = open(_DATA_PATH)
        while True:
            s = f.readline()
            if not s:
                f.close()
                return
            lst = s.rstrip('\n').split(',')
            L.append(dict(zip(_info.values(), lst)))
    except IOError:
        print('数据读取失败！！！')