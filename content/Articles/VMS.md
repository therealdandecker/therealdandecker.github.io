Title: A Search for the right Env
Date: 2020-04-06 20:39
Tags: F#, Virtualization
Category: Data
Author: Dan

Virtualization is all the rage.  Docker containers, virtual desktops, whatever you might need.  As I write this post I am running on Windows Server 2016 on a VPS.  

So how did I end up here? Not my first choice I will tell you.  If I had my druthers I would probably have a pure Linux installation at this point.  Something about Bash just makes everything better, and with the Catalina switch to zsh I am ready for an open source system.

There were a few options to kick around, the big cloud computing platforms were out - I do not need something that big.  A cheap desktop  would probably be my first choice, but I am not about to go to the store (see: Corona virus) and I wanted to get started. Azure and the other cloud providers were off the table - the pay as you go solutions are too expensive and I did not need anything dedicated the way they have it structured.

I work 100% in a Microsoft environment professionally, and my personal machine is a 2013 Macbook Air.  Love it or hate it, Apple stuff lasts a long time.  Why a beast like Windows? Whether you are an MSFT fan or not, they have come a long way and much of their work now is open source.  Visual Studio Code is by far my preferred IDE.

The real reason though - the next project I am looking at entails using F# and SQL, so the natural choice is a Microsoft env.  I know F# is cross platform, but I tried running it natively on Mac and it was a little clunky.  

Sure for SQL you have a lot of choices but I will be honest, I love SSMS, I am not ashamed despite the fact that a lot of respectable data folks would insist it is not a real database.  Can you write SQL there? Yes.  Besides, who wants the overhead of Oracle these days?  I seriously thought about Postgres and MySQL, and MySQL will probably be what I use in the back-end of the next project I endeavor to do, but without knowing a lot about F# I know it will play best with MSFT.

 Given that I work in SQL Server everyday (as some former co-workers not so affectionately called it Squirrely Server) and how wild F# is, I thought it would be the best set up.  

