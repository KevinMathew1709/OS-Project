# OS-Project
Contributors: 
1. Kevin Mathew Maran - UTSA - MS CS (https://github.com/KevinMathew1709)
2. Spandana Mary Gurivireddy - UTSA - MS CS (https://github.com/maryspandana11)

RPC Math Server and Client
•	Setting up Math server:
  -	Open terminal in local directory
  -	Run "python server.py"
  -	Enter the required port number to listen
  -	Math server starts running and shows IP:PORT

•	How to Connect Client to Server:
  -	In the same device or another device on the same network, open terminal in local directory
  -	Run "python client.py"
  -	Enter the IP address of Math Server (Can be seen in Server terminal output)
  -	Enter the open Port number (Can be seen in Server terminal output)
  -	Client connects to server and sends 1000 RPC requests
  -	Client retrieves count of operations done

•	Concurrent Execution:
  -	Setup the math server in any device using the previous instructions
  -	In two different devices (can be VMs), connect to the same Wi-Fi
  -	In both devices, follow the same instructions to enter the IP and port details of server
  -	Run them at the same time
  -	The Server logs the requests from both devices simultaneously while both clients will be showing the results of 1000 requests
  -	The client that completes first will show the instantaneous counter value at the time of completion while the other client will show the total requests processed, i.e., 1000
