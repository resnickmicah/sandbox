from threading import Thread

def print_range():
    for i in range(1,100):
        print(f"Printing {i} in first thread!")

t1 = Thread(target=print_range)
t1.name = "one"
t2 = Thread(target=print_range)
t2.name = "two"

t1.start()
t2.start()