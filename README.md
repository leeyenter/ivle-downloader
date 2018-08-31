# ivle-downloader
This is a Python project that uses Selenium to download lecture notes from your NUS IVLE account.

## Selenium + Web Driver

Selenium is used to emulate the browser, and allow the files to display using Javascript. 
This project uses ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) 
but any web driver can be used. 

## Installation

1. Python 3 first needs to be installed (https://www.python.org/downloads/)
2. Selenium and requests also need to be installed. In Command Prompt/Terminal, run:

```bash
pip install selenium requests
```

3. The repo contains a `chromedriver.exe`, but if you use another browser or another OS, you can download the relevant ones at http://chromedriver.chromium.org/downloads or https://github.com/mozilla/geckodriver/releases

## Use

Simply change the folder to download the files to, as well as your username and password listed, and you're good to go! 

Download both `ivleDownload.py` and `chromedriver.exe` (or whatever driver you need) into the same folder, and run:

```shell
python ivleDownload.py
```
