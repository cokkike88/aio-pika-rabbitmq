
# import time
# startTime = time.time()
# for i in range(0,10):
#    print(i)
#    if(i==7):
#        break
#    # making delay for 1 second
#    time.sleep(0.5)
# endTime = time.time()
# elapsedTime = endTime - startTime
# print("Elapsed Time = %s" % elapsedTime)


# print('===================== WHILE ======================')


# startTime = time.time()
# i = 0
# while i < 10:
#    print(i)
#    if(i==7):
#        break
#    # making delay for 1 second
#    time.sleep(0.5)
#    i += 1 
# endTime = time.time()
# elapsedTime = endTime - startTime
# print("Elapsed Time = %s" % elapsedTime)



from retrying import retry
from retry.api import retry_call
import requests
import random

def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    print('RESULT---- ', result, result is None)
    return result is None

@retry(wait_fixed=2000, stop_max_delay=4000,retry_on_result=retry_if_result_none)
def do_something_unreliable():
        r = random.randint(0, 10) 
        print(r)
        if r > 1:
            # raise IOError("Broken sauce, everything is hosed!!!111one")
            print("Broken sauce, everything is hosed!!!111one")
        else:
            return "Awesome sauce!"


print (do_something_unreliable())

def make_trouble(service, info=None):
    print(service)
    print("info", info)
    if not info:
        info = ''
    r = requests.get(service + info)
    return r.text


def what_is_my_ip(approach=None):
    if approach == "optimistic":
        tries = 1
    elif approach == "conservative":
        tries = 3
    else:
        # skeptical
        tries = -1
    result = retry_call(make_trouble, fargs=["http://ipinfo.io/"], fkwargs={"info": "ip"}, tries=tries)
    print(result)

# what_is_my_ip("conservative")


def make_trouble2():
    r = random.randint(0, 100) 
    print(r)
    if r < 1:        
        return "Awesome sauce!"
  
def execute_timer():
    result = retry_call(make_trouble2, delay=1000, tries=9)
    print(result)
    
# execute_timer()    
