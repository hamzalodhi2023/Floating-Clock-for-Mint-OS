sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0

mkdir -p ~/Scripts

paste floating_clock.py & start_clock.sh into /home/yourusername/Scripts

chmod +x ~/Scripts/floating_clock.py
chmod +x ~/Scripts/start_clock.sh

XFCE menu (Startup Menu) → Session and Startup
Application Autostart tab me → Add
Fill karo:
Name: Floating Clock
Description: Desktop clock
Command: /home/yourusername/Scripts/start_clock.sh
Save kar do
