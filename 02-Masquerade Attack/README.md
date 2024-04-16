# Application-security-

<h1>### Masquerade Attack ###</h1>

Introduction :- A masquerade attack refers to a cyber attack where an attacker impersonates a legitimate user or device in order to gain unauthorized access to a network or                 system. In masquerade attack the attacker pretend to the server or network that he/she is the valid user.

<h2>Note:- please first read all the instructions carefully and then perform every single instruction one by one...........</h2>
Process ----------------------------

1. Create Pycharm project.
2. Copy all the files in /.venv/ folder
3. Download Wireshark (https://www.wireshark.org/download.html)
4. Open the Wireshark and navigate or double click to the "Adapter for loopback traffic capture".

# Establishe connection between new_server and new_client
5. Run new_server.py
6. Run new_client.py
7. when new_server and new_client connected successfully try to send messages
   from client to server and from server to client

   # output should look like that
   ###>  new_server.py
   C:\Users\manju\PycharmProjects\pythonProject5\.venv\Scripts\python.exe C:\Users\manju\OneDrive\Desktop\pythonProject5\.venv\new_server.py 
Server listening...
Connected by ('127.0.0.1', 61220)
Client's Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1KPTgn6Qdu0GYbfBn/BN
SfFuuiCn9Zz7Z/gEaKzBxkzeMMc3NBZxUq5b9q81M9u1fY2Sl5rl6rJ5HqoXdyGz
Jb/6eVkUd9kFBNRxTxg2ddwMbem3wHPXkxh2PZxP13V3N2QhsXYuILfaBtqtMBr+
Lx/moRnefm27cMMADkaM1v/ZnTJSAeB24jCEIfndHUXPM6NyW3kmLSSDGTNjxdRL
kONTr1XVS0tRIuagfniLjaMBEvAPgiO9zg5lbuTuthP2p0J2/HWF1JaD8+8azcRA
ZVmcXGP3nF+yUrvOdlALHUnK5+rOSFtga1bezruDTRO0La5aeVazKmlIw+hpmkIJ
SQIDAQAB
-----END PUBLIC KEY-----

Client message:  hi
Server message: hello
-----------:Encrypted message:--------------
b'\xc4DR\x14\x8a\xd3J\x96\x19\xfdH+\xdf\xa3=\xde\x80\xe8\x90\x92k\x918K\x86\xce:\xa9K\xfeay\xfe\xf5"t,u-\x84\xca\xe9\xa35&/\xdeG\xdcA\x8a\x1b\xa9c\xda3\xa7\x1f\xbc\x9e[-Kr\x9d!\xd3\x19;\x88\xf6\x03$\x15Q\xb6\x8b\xca\xc0^\x9bWz\xa5\xae\xc6"\xb86X\x16\xc2S\xd6\xde\xfd\xa5~\xeb\x07\xd4\xa3K\xc9z\x93\xd8\xd0\xba\xc5-\xc7g\x88Hc"\xf7\xc9\x11\x02!\xeb3W\x03is\x0f\x00k\xe3\xc9\xeeI\xb7N z\x9d\xfd!\x08\xe5\xed\x18!e\x04\xca\xec\x9e\xf9\xb8\xd2{q\xfa\x14\x8a\xbb\\\xc6\xcc<\xd0\xdaj\x9a\x00\xf7\x98\xccQ\xef\xeeP\xf4g\xcf\x95:\xcb\xa75\xb3\x98\xabPQ\xa8\xb3\x86Q\x86\x9a$m\xc6\x8aY\xea\x06~Q\xa3O\x91\xbe!:q\x1d[`\x12\x02\xd6fi\x9b8\x11n\xee\x9f#\xf9H~zp\xe2:g\x91\xb3\xffzChT+u\xc6\xfa\x1b\xba\x84k-\x83\x0f\xb8Iu'
------------------:end:---------------------

  ###> new_client.py
C:\Users\manju\PycharmProjects\pythonProject5\.venv\Scripts\python.exe C:\Users\manju\OneDrive\Desktop\pythonProject5\.venv\new_client.py 
Server's Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt0NcmwzZCEJS+dt0+f2u
1hyuxgWbvLNmVBuikvw2t2h3qEu410ewubS9UBKeppegrT/sER0y3fY8iafdXye4
Ix2fGfmMhAw3wXDyk6bqrdSp3fvj1ub6Skx+Q3dGWYtpC45ungdlP28t6m3gcT4B
yvRI8oBHJiLemM4KIJbBrE9fNgWwsIZ1/4KNFexZIiT60m5VkNr0TtHhYgAaX3YX
r90mpJqhXxDZcDDVz6wOcKxcjHc3iaD7iygRhf1a+FFQVaIz+jGysaSv8y4Q6d44
izkQw1W1kOWQOjgjTJpujfhjGIxDhtcdzxicequT85Nkwsi1PcIx+lBc7Z47ukT+
uQIDAQAB
-----END PUBLIC KEY-----

Client message: hi
-----------:Encrypted message:--------------
b'\x84E\x17D\x1f\xd0\xf3,\xa7\x9b\xf5\xc8\xeeP\x8c\xf3\xe1\x89\xb5\x13k\x15:\x1c\x8e\x94%\xd2r\xc4\xea\xdfS\x01\xad\x1c&2*\x1c?\xc4\xed^\x13\xa2\xe8.\\\xac;7](Zw\xe5\xf2\x0e\xea\x134\xd5\x82\xe8~\xadL\xed\xce\xd0h\xf8)D\xcc2\x91\xa9\xfe\x04\x99\xf3\xaa\x90bw\x04k\xf3\x14N/\xaa\x11\x14;\xa23R-\xe0*\x8aN\x9a>\xbcK\x8bE\xad>\x89\xcf\x9c\x19\x8d\xce\xc6*\x14lq\xf6\x08L|\xea\xa6\xad"\xff\x1b\xd7\xb7\xf4\xb3\xf8\'YW\x95[W(\x10\xb121 h\xa3\xd5M_.!\n\'\x92\xd8\x80B\x98g\n\x80\x9fr\x0f\xa0\x1fx\xef\xaaY\x88;I\xa7\x96sPONl\xe4\x13\'r\xc1og\x98\xaf\x84\x9b\xf3\xe2\xc3\xad6\'>\xeeZ\xf2\x8e\x1c\x19 \xe9\xa9\xff\xf9 \xe6\xfd\xc6\x18N\xd8\xfb\x9e|7U\x7f\xa19q\xda\x17"\xefQY\x06\xc5\xa6\x92\xe0k\xec\xb2G_\x98!\xeb\x8e\x18\xf8:\x02'
------------------:end:---------------------
Server message: hello
Client message: 


-------------------------------------------------------------------------------------------


8. now check the Wireshark console, you would notice there is the sharing of key between server and client when server and client successfully established the connection.
9. if do not find the port in the console (port= 12345) then try "tcp.port == 12345 || tcp.port == 12345" in filter.
10. now find like "2494 16.292802     127.0.0.1     127.0.0.1    TCP    495 12345 -> 63766  [PSH, ACK]  Seq=1 Ack= 452 Win=2619648 Len=451"
    there will 2 which will look like this but double click the the one which have keywords "[PSH, ACK] and Len=451" in it. remember Ack should not equal to 1.
    ![Screenshot 2024-03-24 141417](https://github.com/the-zoomeee/Application-security-/assets/154297263/db0a40bb-6d82-448d-a5ef-8e3dfba367aa)
12. after navigate to the DATA, you will find how number like "41 42 43 44 45" and some random characters (public key)
13. right click on the characters and click the (....printable text)


    #### now till now you have completed the process of tapping targets device and capturing the server's public key which will help to send messages from fake client
14. now open the Hacked.pem and past the key in propar format (for you we have already done this process).
15. now simply terminate the new_client.py file using button to the left side of the terminal (square like button)
16. now run the fake_client.py file.
17. now you can able to send messages from fake client and it will proceed by server as valid client


    ### hance we reached to our goal......................
