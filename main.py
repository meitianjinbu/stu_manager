from operators import *
import menu
def main():
    flag = True
    while True:
        menu.show_menu()
        if flag:
            s = input('请按照提示选择操作：')
        if s not in ops_dict:
            flag = False
            s = input('输入有误，请按照提示重新选择操作：')
        elif s == 'q':
            print('程序结束，欢迎下次使用！')
            return
        else:
            flag = True
            eval(ops_dict[s])(s)


if __name__ == '__main__': #判断当前模块是否是主模块
    main()