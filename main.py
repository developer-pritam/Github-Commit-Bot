import os
a = int(input("Enter Day : "))
w = int(input("Select Week : "))
a = w*7 + a
b = a + 1
c = int(input("No. of Commit require : "))
for i in range(c):
    for i in range(a, b):
        d = str(i) + ' days ago'
        with open('bot.txt', 'a') as file:
            file.write(d+'\n')
        os.system('git add bot.txt')
        os.system('git commit --date="'+d+'" -m "hack-commit"')

    os.system('git push -u origin main')

 