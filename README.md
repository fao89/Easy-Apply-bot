# Easy Apply bot for LinkedIn

Bot for locating positions with the Easy Apply button and then send your resume.

## Getting Started

This bot launches the chromedriver, waits the user login into LinkedIn account.

#### Then the user:

* Specifies the desired job title;
* Specifies the desired location;
* Selects the resume file.

#### Installing project:
* Before start a virtual env: `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev python-tk python3-tk tk-dev`
*  `pip install -r requirements.txt`

#### Installing ChromeDriver:
* `sudo apt-get install chromium-chromedriver`
* `echo  'export PATH=$PATH:/usr/lib/chromium-browser/' >> ~/.bashrc`
