Title: A Search for the right Env
Date: 2020-04-06 20:39
Tags: Python, Virtualization
Category: Data
Author: Dan

Virtualization is all a necessity.  Docker containers, virtual desktops, whatever you might need.  As I write this post I am running on Windows Server 2016 on a VPS.  

So how did I end up here? Not my first choice I will tell you.  If I had my druthers I would probably have a pure Linux installation at this point.  Something about Bash just makes life infinitely easier than anything else, but we don't always get what we want.  

There were a few options to kick around, the big cloud computing platforms were out - I do not need something that big.  A cheap desktop with Windows Pro and Linux dual-boot would probably be my first choice, but I am not about to go to the store and I wanted to get started. I did Azure for a while, but found the pay-as-you-go prohibitive even when you deallocated the machine when you were done.  

I work 100% in a Microsoft environment professionally, and my personal machine is a 2013 Macbook Air.  Love it or hate it, Apple stuff lasts a long time.  Why a beast like Windows? Whether you are an MSFT fan or not, they have come a long way and much of their work now is open source.  Visual Studio Code is by far my preferred IDE.

The real reason - I had a needed (preferred) to run SQL Server.  I love SSMS, I am not ashamed despite the fact that a lot of respectable data folks would insist it is not a real database.  Can you write SQL there? Yes.  Besides, who wants the overhead of Oracle these days?  I seriously thought about Postgres and MySQL, and MySQL will probably be what I use in the back-end of the next project I endeavor to do, but I had my reasons.

A quick aside - SQLite is actually my preferred SQL when I need to work with SQL and Python - the new SQL Server Python is the Anaconda distribution but its still heavy; the beauty in SQLite is how lightweight it is.   Get in and get out with a lot of fuss; Pandas does everything in memory anyway, so as long as your data sets are not enormous its a logical choice.  

 I work in SQL Server everyday (as some former co-workers not so affectionately called it Squirrely Server) and for this project, I had steps I wanted to automate and knew how I could easily do so in a SQL Server Developer env.  

