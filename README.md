![](https://img.shields.io/badge/PwnAI-v23-brightgreen)
<img width="1675" alt="Screenshot 2022-12-03 at 1 32 43 PM" src="https://user-images.githubusercontent.com/3261849/205458576-f5200aa1-bf4b-41a9-bc3b-3959427090ac.png">

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
<img width="940" alt="Screenshot 2022-12-03 at 1 24 53 PM" src="https://user-images.githubusercontent.com/3261849/205458297-8f3277e5-f9bf-4e72-83fe-678b4d70f0f8.png">

`Bulk searches`
```
python3 PwnAI_bulk.py
```
<img width="1071" alt="Screenshot 2022-12-03 at 1 27 55 PM" src="https://user-images.githubusercontent.com/3261849/205458428-f931e065-951a-4eec-8496-4c3969d158ee.png">
