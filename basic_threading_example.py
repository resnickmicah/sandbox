from threading import Thread

def p_one():
    for i in range(1,100):
        print(f"Printing {i} in first thread!")

def p_two():
    for i in range(1,100):
        print(f"Printing {i} in second thread!")

t1 = Thread(target=p_one)
t2 = Thread(target=p_two)

t1.start()
t2.start()