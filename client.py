# client.py
import xmlrpc.client
import random

# Function to execute remote code in Math server
def random_request(proxy, num1, num2, num3):
    op = random.choice(["add","sub","min","max"])
    if op == "add":
        return proxy.magicAdd(num1, num2), op
    elif op == "sub":
        return proxy.magicSubtract(num1, num2), op
    elif op == "min":
        num1, num2 = int(num1), int(num2)
        return proxy.magicFindMin(num1, num2, num3), op
    else:
        num1, num2 = int(num1), int(num2)
        return proxy.magicFindMax(num1, num2, num3), op

if __name__ == "__main__":
    while(True):
        try:
            IP = input("Please input Math Server IP: ")
            PORT = input("Please input Math Server port number: ")
            if (IP == "") or (PORT == ""):
                IP, PORT = " ", " "
            LINK = "http://" + IP + ":" + PORT + "/"
            proxy = xmlrpc.client.ServerProxy(LINK, allow_none=True)
            proxy.getTotCount()
        except KeyboardInterrupt:
            print("")
            break
        except:
            print("Please enter the correct IP/Port number!")
        else:
            # Loop to generate 1000 RPC requests
            for i in range(1000):
                num1, num2, num3 = random.random()*100, random.random()*100, random.randint(0,100)
                result, op = random_request(proxy, num1, num2, num3)
                if op in ["add", "sub"]:
                    print("%-15s %-20s %3s %10.2f" % ("Request %d:" % (i + 1), "%s(%.2f, %.2f)" % (op, num1, num2), "=", result))

                else:
                    print("%-15s %-20s %3s %10d" % ("Request %d:" % (i + 1), "%s(%d, %d, %d)" % (op, num1, num2, num3), "=", result))
                
            # Fetch and print counters
            print("")
            print("Add calls:\t", proxy.getAddCount())
            print("Sub calls:\t", proxy.getSubtractCount())
            print("Min calls:\t", proxy.getMinCount())
            print("Max calls:\t", proxy.getMaxCount())
            print("Total calls:\t", proxy.getTotCount())
            break
