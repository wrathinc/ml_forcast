import socket
import threading
from queue import Queue 



print_lock = threading.Lock()



def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try: 
		con = s.connect((target,port))
		with print_lock:
			print(f"port {port} is open!")
		con.close()
		
			
	except:
		pass

target = 'newmauricepoolandspas.townsquareinteractive.com'




def threader():
	while True:
		worker = q.get()
		portscan(worker)
		q.task_done()

q = Queue()

for x in range(500):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()

for worker in range(1,10000):
	q.put(worker)

q.join()

access_token: "Aa836he24krnhfae5944id2vrccbh7gd9i8irr9"
server = Cowboy