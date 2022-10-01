# Index Number: 20000278
# Registration Number : 2020/CS/0027
# Name: Dayalan S.K
 
Please visit my GitHub page to see the readme file in a more user-friendly format  
=> https://github.com/DevSachia
 
 
# Create a Simple Web Server 
 
## Introduction  
 
- This is a very simple and basic web server. 
- Created by the Python programing language using Socket Programming concept. 
- What's the Socket Programming - https://realpython.com/python-sockets/ 
 
## File Introduction 
 
 - server.py => Server source code  
 - htdocs => Contain web pages 
 - readme => Contains instructions to execute the web server 
 
 
## Installation 
 
 
 
Preparing the Environment to Run the Program 
 
1. Clone the Git Repository From by GitHub or Download the Zip file From my GitHub 
bash 
  https://github.com/DevSachia
 
 
2. Download & Install the Python on Your Os: 
bash 
  - Windows 
  - Ubuntu 
  - Mac  
 
 
bash 
  https://www.python.org/downloads/ 
 
 
3. Start the Web Server 
 
Run the server.py file, type in the terminal: 
bash 
  >> py server.py 
 
or 
bash 
  >> python server.py 
 
 
 
4. Open the browser and type the URL  
 
- To visit localhost(default routing path) 
bash 
    http://localhost:2728 
 
Or 
 
bash 
    http://localhost:2728/ 
 
 
- To visit my aboutMe page 
bash 
    http://localhost:2728/about 
 
- If visit any other pages  
bash 
    404 Not Found 
 
 
 
## Example 
 
 
01.  
- Visit localhost - http://localhost:2728 
 
C:\Users\admin\Downloads\server> & C:/Python310/python.exe c:/Users/admin/Downloads/server/server.py 
[Starting] Server is starting
[Listening] server is listening on 192.168.114.194

Current Path :/ 
[New connection] ('127.0.0.1', 51733) connected
 ['']
Path - C:\Users\admin\Downloads\server\htdocs\index.html


 
 
02. 
- Visit aboutMe page - http://localhost:2728/aboutme 
 
PS C:\Users\admin\Downloads\server> & C:/Python310/python.exe c:/Users/admin/Downloads/server/server.py 
[Starting] Server is starting
[Listening] server is listening on 192.168.114.194
/about ['/about']
C:\Users\admin\Downloads\server\htdocs\about.html
[New connection] ('127.0.0.1', 51742) connected
 
03. 
- Visit any other page - http://localhost:2728/xyz 
 
PS C:\Users\admin\Downloads\server> & C:/Python310/python.exe c:/Users/admin/Downloads/server/server.py 
[Starting] Server is starting
[Listening] server is listening on 192.168.114.194
Got connection from ('127.0.0.1', 1808) 
Current Path :/xyz 
404 Not Found Error 
 
 
 
 
## Authors 
 
- [@devsachi](https://github.com/DevSachia) 
 
 
##  Contact me  
 
Email: 
- 2020cs027@stu.ucsc.cmb.ac.lk
