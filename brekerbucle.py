def run ():
    for contador in range(1000):
        if contador %2 != 0: 
            continue
        print(contador)
    for i in range(4000):
        print(i)
        if i == 789:
            break
if __name__ == '__main__':
    run()