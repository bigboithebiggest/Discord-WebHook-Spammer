import time, requests, pyfiglet, threading
print(pyfiglet.figlet_format("KINGMAN"))

msg = input("test: ")
webhook = input("https://discord.com/api/webhooks/1404186544255930469/J1wOAyzDxdFMWRxcO2U773kx0-GwsnTPOf3ElYpZUF_w56fj7QxVPQ5H-wTlH_K8-Umz: ")
th = int(input('200: '))
sleep = int(input("2: "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()

