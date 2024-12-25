import os
import subprocess
import shutil

CRD_SSH_Code = input("Google CRD SSH Code :")
username = "tohan" #@param {type:"string"}
password = "root" #@param {type:"string"}
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 12345678 #@param {type: "integer"}
Autostart = True #@param {type: "boolean"}

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installDesktopEnvironment()
        self.changewall()
        self.installGoogleChrome()
        self.installCRD()
        self.installTelegram()
        self.installQbit()
        self.finish(user)


    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("sudo apt purge light-locker")
        os.system("sudo apt install --reinstall xfce4-screensaver")
        os.system("systemctl disable lightdm.service")
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m XFCE4 Desktop Environment has been installed successfully. Please wait for the next package installation...\033[0m")
        # Extra
        os.system("apt install --assume-yes dbus-x11")
        ####
        os.system("apt install --assume-yes snapd")
        os.system("snap install snap-store")
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m Snap Store has been installed successfully. Please wait for the next package installation...\033[0m")
        ####
    @staticmethod
    def changewall():
        os.system(f"curl -s -L -k -o xfce-verticals.png https://tuahahadi.wordpress.com/wp-content/uploads/2024/12/pc_wall-1.png")
        current_directory = os.getcwd()
        custom_wallpaper_path = os.path.join(current_directory, "xfce-verticals.png")
        destination_path = '/usr/share/backgrounds/xfce/'
        shutil.copy(custom_wallpaper_path, destination_path)
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m Tohan System update successfully. Please wait for the required package installation...\033[0m")

    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m Google Chrome has been installed successfully. Please wait for the next package installation...\033[0m")

    @staticmethod
    def installCRD():
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m Chrome Remote Desktop has been installed successfully. Please wait for the next package installation...\033[0m")
    
    @staticmethod
    def installTelegram():
        subprocess.run(["apt", "install", "--assume-yes", "telegram-desktop"])
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m Telegram Desktop has been installed successfully. Please wait for the next package installation...\033[0m")
   
    @staticmethod
    def installQbit():
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "qbittorrent"])
        print("\033[34m[ \033[32m✔︎ \033[34m] \033[96m Qbittorrent has been installed successfully. Almost done...\033[0m")

    @staticmethod
    def finish(user):
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "www.github.com/thuahahadi"
            colab_autostart = """[Desktop Entry]
            print("⏳ \033[32mFinalizing the setup...\033[0m")

Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")
            
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        
        print(r'''
          
+----------------------- Tohan RDP Server ----------------------+
| @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ | 
| @@@@@@        @@@     @@@  @@@@@  @@@@@  @@@@@  @@@@@  @@@@@@ |
| @@@@@@@@@  @@@@  @@@@% @@  @@@@@  @@@@    @@@@   &@@@  @@@@@@ |
| @@@@@@@@@  @@@  @@@@@@ #@         @@@ .@&, @@@  @. &@  @@@@@@ |
| @@@@@@@@@  @@@  @@@@@  @@  @@@@@  @@ ______ &@  @@@*   @@@@@@ |
| @@@@@@@@@  @@@@(    (@@@@  @@@@@  @ .@@@@@@  @  @@@@@  @@@@@@ |
| @@@@@@@@&@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@ |
+-------------------------[by Thuaha Hadi]----------------------+      
                 
    ''')
        print ("\033[32mCongratulations! \033[0mYour RDP server is now ready. \nYou can access it through \033[95mGoogle Remote Desktop \033[0mapp or by using the link: https://remotedesktop.google.com. \nYour login credentials are provided below.\n")

        print(r'''
            
            +------------------------------------------+  
            |             Login Credentials            |
            +------------------------------------------+
            |  GRD Login PIN     :       12345678      |
            +------------------------------------------+
            |  User Name         :       tohan         |
            +------------------------------------------+
            |  User Password     :       root          |
            +------------------------------------------+
              ''')
        while True:
            pass

try:
    if CRD_SSH_Code == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
