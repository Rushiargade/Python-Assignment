Python-Assignment

Welcome to my Python assignment submissions. Each script here tackles a different Python problem or use-case. Here’s a quick rundown of what each file does and how I approached the solution:

1. Assignment_solution_1.py — Password Strength Checker
I wrote a simple tool that checks how strong a password is. The program looks for things like

how long your password is,

whether you mixed uppercase and lowercase letters,

if you included numbers and special symbols.

It gives feedback directly to the user about the password’s strengths and areas to improve—all using basic string checks and regular expressions.

2. Cpu_Usage_Moniter.py — CPU Usage Monitor
This script keeps track of your computer’s CPU usage in real-time using the psutil library.
It runs in a loop, updating the stats live in your terminal, so you can instantly see how much processing power is being used at any moment.

3. config_parse.py — INI Config Parser & Flask API
Here, I made a program that reads a standard INI configuration file, grabs all the settings, and turns them into JSON format for easier reading and management.
On top of that, I set up a simple web API with Flask, so the config can be accessed securely through a web endpoint.

4. backup.py — Data Backup Script
This script lets you back up files from one folder to another.
It copies everything from your chosen source directory into a backup location, handling errors if files are missing or permission is denied—making it a straightforward way to safeguard your data
