import subprocess


def run():
    p = subprocess.Popen("pytest -s test.py --alluredir=report", shell=True, stdout=subprocess.PIPE)
    res = str(p.stdout.read(), encoding='utf-8')
    print(res)


if __name__ == '__main__':
    run()
