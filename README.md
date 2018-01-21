# ivle-downloader
This is a Python project that uses Selenium to download lecture notes from your NUS IVLE account.

## Selenium + Web Driver

Selenium is used to emulate the browser, and allow the files to display using Javascript. 
This project uses ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) 
but any web driver can be used. 

## Use

Simply change the folder to download the files to, as well as your username and password listed, and you're good to go! 

Download both `ivleDownload.py` and `chromedriver.exe` (or whatever driver you need) into the same folder, and run:

```shell
python ivleDownload.py
```
