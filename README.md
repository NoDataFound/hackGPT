![](https://img.shields.io/badge/PwnAI-v23-brightgreen)




<img width="977" alt="Screenshot 2022-12-04 at 6 27 59 PM" src="https://user-images.githubusercontent.com/3261849/205525745-fa26c95b-9d86-4c84-8669-be1cde4abaf2.png">

<img width="1269" alt="Screenshot 2022-12-04 at 6 32 40 PM" src="https://user-images.githubusercontent.com/3261849/205525669-9eb6e988-4440-43ea-8432-6f07066db7df.png">

https://user-images.githubusercontent.com/3261849/206036893-b583fad1-6b77-4dfb-8424-639229ffdd19.mov


## 𝗜𝗻𝘀𝘁𝗮𝗹𝗹𝗮𝘁𝗶𝗼𝗻
`Clone this repo`
```
git clone https://github.com/NoDataFound/PwnAI.git
```
`Install dependancies`
```
python3 -m pip install -r requirements.txt
```
`Review Input and Bulk Input samples`
```
head -n 10 input/malware/malware_sample && head -n 10 input/sample_sources

# Exploit Title: TP-Link Tapo c200 1.1.15 - Remote Code Execution (RCE)
# Date: 02/11/2022
# Exploit Author: hacefresko
# Vendor Homepage: https://www.tp-link.com/en/home-networking/cloud-camera/tapo-c200/
# Version: 1.1.15 and below
# Tested on: 1.1.11, 1.1.14 and 1.1.15
# CVE : CVE-2021-4045

# Write up of the vulnerability: https://www.hacefresko.com/posts/tp-link-tapo-c200-unauthenticated-rce

https://github.com/rapid7/metasploit-payloads/blob/master/python/meterpreter/meterpreter.py
https://github.com/rapid7/metasploit-payloads/blob/master/powershell/MSF.Powershell/Meterpreter/Core.cs
```

`Open Jupyter Notebook`
*Install Juypter Notebook if needed - use pip or download binaries here: https://jupyter.org/*
```
pip3 install jupyter notebook
```
`install (pictured) https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers`


## 𝖫𝖺𝗎𝗇𝖼𝗁 𝖭𝗈𝗍𝖾𝖻𝗈𝗈𝗄 𝘄𝗶𝘁𝗵 𝗩𝗦𝗰𝗼𝗱𝗲

<p align="center">
<img align="center" src="https://user-images.githubusercontent.com/3261849/205510169-5269cde5-7565-4094-9a07-2d41e65bc717.png"></p> 

`Configure .env with your OpenAI API key(notebook will help you)`

## Use Python 
`set API key on launch`
<img width="959" alt="Screenshot 2022-12-03 at 1 23 38 PM" src="https://user-images.githubusercontent.com/3261849/205458244-ed556dd8-c8d8-498d-9a1d-727d139e46d7.png">

`single searches`
```
python3 PwnAI.py
```
<img width="1147" alt="Screenshot 2022-12-04 at 6 26 38 PM" src="https://user-images.githubusercontent.com/3261849/205525796-d8d009b5-9d76-4b04-ae24-319e5f1ea924.png">


`Bulk searches`
```
python3 PwnAI_bulk.py
```
<img width="977" alt="Screenshot 2022-12-04 at 6 27 59 PM" src="https://user-images.githubusercontent.com/3261849/205525811-8c5eb58b-257e-4412-a462-89f0c3ccb5be.png">

