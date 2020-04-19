import random
secret = random.randint(1,10)

print('------------我爱甲鱼c工作室---------------')
temp = input('猜猜小鲫鱼心里想的是那个数字：')
guess = int(temp)
if guess==secret:
    print('我草，你是小甲鱼心里的蛔虫吗')
    print('哼，猜中了也没有奖励')
else:
    while guess!=secret:
        temp = input('重新猜猜小鲫鱼心里想的是那个数字：')
        guess = int(temp)
        if guess==secret:
            print('猜对了也没奖励！！！')
        else:
            if guess > secret:
                print('哥，大了大了~~')
            else:
                print('哥，小了小了~~')
print('不玩啦，游戏结束！')
