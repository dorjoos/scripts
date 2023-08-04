import hashlib
from multiprocessing import Process

def work(id, start, end):
    with open("rainbow_table" + str(id) + ".txt", 'w') as f:
        
        for i in range(start, end):
            string = str(i) + "salt_for_you"

            for j in range(0, 500):
                string = hashlib.sha1(string.encode('utf-8')).hexdigest()
            
            f.write(string[0:8] + "[" + str(i) + "]" + '\n')
            
if __name__ == "__main__":
    th1 = Process(target=work, args=(1, 10000000, 20000001))
    th2 = Process(target=work, args=(2, 20000001, 30000001))
    th3 = Process(target=work, args=(3, 30000001, 40000001))
    th4 = Process(target=work, args=(4, 40000001, 50000001))
    th5 = Process(target=work, args=(5, 50000001, 60000001))
    th6 = Process(target=work, args=(6, 60000001, 70000001))
    th7 = Process(target=work, args=(7, 70000001, 80000001))
    th8 = Process(target=work, args=(8, 80000001, 90000001))
    th9 = Process(target=work, args=(9, 90000001, 100000000))
        
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()
    th9.start()
    
    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()
    th7.join()
    th8.join()
    th9.join()