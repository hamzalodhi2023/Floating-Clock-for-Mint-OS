<!-- sudo apt update
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
Save kar do -->

# 🕒 Floating Clock for Linux Mint (XFCE)

A simple **floating desktop clock** for Linux Mint XFCE, built with Python and GTK.  
Keep your time visible while you work.

---

## 🚀 Features

- Lightweight and simple
- Auto-start on XFCE login
- Modern Design

---

## 🛠️ Prerequisites

Install the required dependencies:

````bash
sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0


---

## 📂 Installation

1. Create a folder for your scripts:

```bash
mkdir -p ~/Scripts
````

2. Copy the scripts `floating_clock.py` and `start_clock.sh` into the folder:

```text
/home/yourusername/Scripts/floating_clock.py
/home/yourusername/Scripts/start_clock.sh
```

3. Make the scripts executable:

```bash
chmod +x ~/Scripts/floating_clock.py
chmod +x ~/Scripts/start_clock.sh
```

---

## 🔄 Autostart on XFCE

1. Open **XFCE Menu → Session and Startup**
2. Go to the **Application Autostart** tab → **Add**
3. Fill in the details:

- **Name:** Floating Clock
- **Description:** Desktop Clock
- **Command:** `/home/yourusername/Scripts/start_clock.sh`

4. Save the entry. ✅

Now the clock will automatically start whenever you log in.

---

## 💻 Usage

Run the clock manually if needed:

```bash
~/Scripts/start_clock.sh
```

---

Made with ❤️ for Linux Mint XFCE
