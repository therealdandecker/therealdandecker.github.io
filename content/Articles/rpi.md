Title: Virtual VNC
Date: 2020-06-04 22:54
Tags: Python, Raspberry Pi, VNC
Category: Data
Author: Dan

I wanted to share a quick post on [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/ "Raspberry Pi"). / [RealVNC](https://www.realvnc.com/en/ "RealVNC") after going through some challenges getting moving with this.  I have been enjoying using a Raspberry Pi 4 as a dev-box at home along with web browsing and reading the news.  

One of the things mentioned in my last post on Home Assistant was getting not one but two RPi4s. If you have a passing interest in open source software, hardware, or Linux I think it is definitely something worth looking at.  How did I end up with two? Home Assistant needs a dedicated device and I wanted to keep tinkering with the other one.

I went through seven operating systems total before I settled on a full Raspbian install on the Pi, not necessarily because it was my first choice, but because I realized it really was the best option.  If you have a Raspberry Pi a myriad of options exist for an operating system.  There is no shortage of articles available on different operating systems available.  Here is the thing - the OS is optimally designed to work with the hardware, and at the end of the day all anyone wants is solid performance.

One of the challenges I had - I bought a touch screen interface to go with the RPi4 before realizing that there really is not a good operating system/GUI for using with the touchscreen (forgo the touch screen if you're considering it.)  

Here is the main issue with the touchscreen, your options are: 
1.  Have Raspbian with a mediocre UI not optimized for touch screen; you can add a touchscreen keyboard and write some triggers to pull it up, but its not a real touchscreen experience if you have ever used a smartphone in your life
2.  You can definitely install Android OS on a Raspberry Pi with some ease, but now you have a fully functioning computer nerfed into a glorified tablet that will not work as well as an actual tablet (granted the price is right.) 
3.  Install Gnome3 on top of a Raspbian Lite install - this actaully almost worked and worked well.  Performance was a little laggy but this was largely resolved after overclocking.  The main issue was the screen size would not correctly render, a little portion of the screen was stretched outside the usable area which made things difficult, made the menu sometimes inaccessible and other small but annoying oddities that ultimately made me move on.

What I arrived at finally and has worked great was using the RPi4 as a dev box for Python and general tablet-esque things like reading the news.  I can remote in via VNC if needed for more control beyond the touchscreen keyboard;  we stationed it on a little breakfast bar where it can be used as a tablet for checking email or reading the news.  

The big trick in its useful life came with a simple shell script that is scheduled on startup:

vncserver -randr=1440x900
lxappearance

This handles two things:
1.  Spins up my VNC server on start-up with a virtual screen perfectly sized for my Macbook Air
2.  Fixes a weird mouse cursor issue, where the mouse cursor appears as an X instead of a normal arrow.  This one was harder to figure out but made me crazy so I had to fix it.

Since then, I have been able to do a lot with testing Python scripts in a much simpler environment, putting some things on Crontab / Python SMTP lib for daily notifications and playing around with Grafana, an open source dashboard tool  