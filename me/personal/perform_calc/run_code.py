
import os

def __main__():
    print("## from main method")
    #print(os.listdir("~/"))
    print("files in / dir")
    print(os.listdir("/"))
    print()
    print()
    print("files in /home dir")
    print(os.listdir("/home"))
    print()
    print()
    print("files in /home/runner dir")
    print(os.listdir("/home/runner"))
    print()
    print()
    print("files in /home/runner/work dir")
    print(os.listdir("/home/runner/work"))
    print()
    print()
    print("files in /home/runner/work/2_python_prj_with_setupfile dir")
    print(os.listdir("/home/runner/work/2_python_prj_with_setupfile"))
    print()
    print()
    print("files in /home/runner/work/2_python_prj_with_setupfile/2_python_prj_with_setupfile dir")
    print(os.listdir("/home/runner/work/2_python_prj_with_setupfile/2_python_prj_with_setupfile"))
    print()
    print()

if __name__ == "__main__" :
    __main__()