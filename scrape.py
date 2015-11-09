import os.path
import requests # http://docs.python-requests.org/en/latest/index.html
import time

# input.txt (top 1M from alexa.com) taken from:
# http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

# exceptions.txt contains failures, or really slow sites

filename_input = "input.txt"
directory_output = "output"

current_ms = lambda: int(round(time.time() * 1000))

if os.path.isfile(filename_input):
    input = open(filename_input, 'r')
    for line in input:
        name = line[0:-1]
        url = "http://"+name
        start = current_ms()
        print(name),
        try:
            request = requests.get(url)
            if (request.status_code is 200):
                content = request.text.encode('utf-8')
                filename_output = directory_output+"/"+name
                output = open(filename_output, 'w+')
                output.write(content)
                output.close()
                print("--> "+str(len(content))+" bytes"),
                print("--> "+str(current_ms() - start)+" ms")
            else:
                print("--> FAILED")
        except:
            print("--> FAILED")
            pass
    input.close()
else:
    print("File '"+filename_input+"' not found")
