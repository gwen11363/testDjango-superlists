Provisoining a new site
=======================

##需要套件

*nginx
*Python3
*Git
*pip
*virtualenv

e.g.,, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

##Nginx虛擬主機設定
*path:/etc/nginx/sites-available/SITENAME
*see nginx.tamplate.conf
*replace SITENAME with, e.g., nana.nctu.me

##systemd工作
*path:/lib/systemd/system/gunicorn-SITENAME.service
*see gunicorn-system.tamplate.conf
*replace SITENAME with, e.g., nana.nctu.me
*using commands to start service:
    sudo systemctl start gunicorn-SITENAME.service
    sudo systemctl enable gunicorn-SITENAME.service
    (make symbolic link
    /etc/systemd/system/multi-user.target.wants/gunicorn-nana.nctu.me.service ->
    /lib/systemd/system/gunicorn-nana.nctu.me.service)

##資料夾結構
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv