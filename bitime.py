from time import localtime, strftime, sleep

c = '●'
print('\n' * 5)

while True:
    print(strftime('%H:%M:%S', localtime()), end='')
    print('\033[1A', end='')
    print('\033[1A' + '\b' * 10 + f'{c}\u001b[31m {c}\u001b[0m  {c} {c}  {c} {c}', end='')
    print('\n')
    print('\033[3A' + '\b' * 10 + f'{c}\u001b[31m {c}\u001b[0m  {c} {c}  {c} {c}', end='')
    print('\n' * 2)
    print('\033[4A' + '\b' * 10 + f' \u001b[31m {c}\u001b[0m  {c} {c}  {c} {c}', end='')
    print('\n' * 3)
    print('\033[5A' + '\b' * 10 + f' \u001b[31m {c}\u001b[0m    {c}    {c}', end='')
    print('\n' * 4)
    sleep(1)