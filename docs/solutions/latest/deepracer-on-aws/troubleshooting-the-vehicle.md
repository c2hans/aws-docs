---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/troubleshooting-the-vehicle.html
---

# Troubleshooting the vehicle
<a name="troubleshooting-the-vehicle"></a>

## How to resolve issues connecting your computer directly to the vehicle using a USB cable
<a name="how-to-resolve-issues-connecting-your-computer-directly-to-the-vehicle-using-a-usb-cable"></a>

When setting up your vehicle for the first time, you might find it unable to open the device console (also known as the device web server, `https://deepracer.aws`, hosted on the vehicle) after connecting your AWS DeepRacer vehicle to your computer with a micro-USB/USB cable (USB is also referred to as USB-A).

Multiple causes may be behind this. Typically, you can resolve the issue with the following simple remedy. To activate your device’s USB-over-Ethernet network
+ Turn off Wi-Fi on your computer and unplug any Ethernet cable connected to it.
+ Press the **RESET** button on the vehicle to reboot the device.
+ Open the device console by navigating to `https://deepracer.aws` from a web browser on your computer.

If the previous procedure doesn’t work, you can check your computer’s network preferences to verify that they’re properly configured to let the computer connect to the device’s network, whose network name is `Deepracer`. To do this, follow the steps in the following procedure.

**Note**
The instructions below assume you’re working with a MacOS computer. For other computer systems, consult with the network preferences documentation for the respective operating system and use the below instructions as a general guide.

<a name="activate-usb-over-ethernet"></a> **To activate the device’s USB-over-ethernet network on your MacOS computer**

1. Choose the network icon (on the top-right corner of the display) to open **Network preferences**. Alternatively, choose **Command\+space**, type **Network**, and then choose **Network System Preferences**.

1. Check if **Deepracer** is listed as **Connected**. If **DeepRacer** is listed but not connected, make sure the micro-USB/USB cable is tightly plugged in between the vehicle and your computer.

1. If the **Deepracer** network is not listed there or is listed but not connected when the USB cable is plugged in, choose **Automatic** from the **Location** preference and then choose **Apply**.

1. Verify that the AWS DeepRacer network is up and running as **Connected**.

1. When your computer is connected to the **Deepracer** network, refresh the `https://deepracer.aws` page on the browser, and continue with the rest of **Get Started Guide** instructions of **Connect to Wi-Fi**.

1. If the **Deepracer** network is not connected, disconnect your computer from the AWS DeepRacer vehicle and then reconnect it. When the **Deepracer** network becomes **Connected**, continue with the **Get Started** **Guide**.

1. If the **Deepracer** network on the device is still not connected, reboot your computer and AWS DeepRacer vehicle and repeat from **Step 1** of this procedure, if necessary.

If the above remedy still doesn’t resolve the issue, the device certificate might have been corrupted. Follow the steps below to generate a new certificate for your AWS DeepRacer vehicle to repair the corrupted file.

 **To generate a new certificate on the AWS DeepRacer vehicle**

1. Terminate the USB connection between your computer and your AWS DeepRacer vehicle by unplugging the micro-USB/USB cable.

1. Connect your AWS DeepRacer vehicle to a monitor (with a HDMI-to-HDMI cable) and to USB keyboard and mouse.

1. Log in to the AWS DeepRacer operating system. If this is the first login to the device operating system, use `deepracer` for the password, when asked for, and then proceed to change the password, as required, and use the updated password for subsequent logins.

1. Open a terminal window and type the following Shell command. You can choose the **Terminal** shortcut from **Applications** → **System Tools** on the desktop to open a terminal window. Or you can use the file browser, navigate to the `/usr/bin` folder, and choose **gnome-terminal** to open it.

   ```
   sudo /opt/aws/deepracer/nginx/nginx_install_certs.sh && sudo reboot
   ```

   Enter the password, which you used or updated in the previous step, when prompted.

   The above command installs a new certificate and reboots the device. It also reverts the device console’s password to the default value printed at the bottom of the AWS DeepRacer vehicle.

1. Disconnect the monitor, keyboard and mouse from the vehicle and reconnect it to your computer with the micro-USB/USB cable.

1. Follow the second [procedure](#activate-usb-over-ethernet) in this topic to verify your computer is indeed connected to the device network before opening the device console (https://deepracer.aws) again and, then, continue with the **Connect to Wi-Fi** instructions in **Get Started Guide**.

## How to switch compute module power from battery to power outlet
<a name="how-to-switch-compute-module-power-from-battery-to-power-outlet"></a>

If the compute module battery level is low when you set up your AWS DeepRacer for the first time, follow the steps below to switch the compute power supply from the battery to a power outlet:

1. Unplug the USB-C cable from the vehicle’s compute power port.

1. Attach the AC power cord and the USB-C cable to the computer module power adapter. Plug the power cord to a power outlet and plug the USB-C cable the vehicle’s computer module power port.

## How to connect your vehicle to a Wi-Fi network using a flash drive
<a name="how-to-connect-your-vehicle-to-a-wi-fi-network-using-a-flash-drive"></a>

To connect an AWS DeepRacer vehicle to your home or office Wi-Fi network using a USB flash drive, you need the following:
+ A USB flash drive
+ The name (SSID) and password for the Wi-Fi network that you want to join

**Note**
AWS DeepRacer does not support Wi-Fi networks that require active captcha verification for user sign-in.

 **To connect an AWS DeepRacer vehicle to a Wi-Fi network using a USB flash drive**

1. Plug the USB flash drive into your computer.

1. Open a web browser on your computer and navigate to https://aws.amazon.com/deepracer/usbwifi. This link opens a text file named wifi-creds.txt hosted on GitHub.

1. Save `wifi-creds.txt` to your USB flash drive. Depending on which web browser you use, the text file might download to your computer and open in your default code editor automatically. If `wifi-creds.txt` doesn’t download automatically, open the context (right-click) menu and choose **Save as** to save the text file to your USB flash drive. **Warning**: Do not change the file name.

1. If `wifi-creds.txt` isn’t already open, open it in a code editor in plain text mode. Some text editors default to rich text (.rtf) instead of plain text (.txt) when the file type isn’t specified, so if you are having trouble editing the file, check your settings. If you are using Windows, you can also try to open the file using the Sublime Text application, which you can download for free, or, if you use a Mac, try the TextEdit application, which is pre-installed on most Mac devices and defaults to plain text.

1. In between the single quotation marks at the bottom of the file, enter the name (SSID) and password of the Wi-Fi network that you want to use. SSID stands for "Service Set Identifier." It is the technical term for the name of your Wi-Fi network.
   + If the network name (SSID) or password contains a space, such as in *Your-Wi-Fi 100*, enter the name exactly, including the space, inside the quotation marks (''). If there is no space, using quotation marks is optional. For example, the Wi-Fi password, *Passwd1234* doesn’t contain a space, so using single quotation marks works but isn’t necessary. Both SSID and password are case sensitive.

1. Save the file on your USB flash drive.

1. Eject the USB drive from your computer and plug it into the USB-A port on the back of the AWS DeepRacer vehicle between the compute battery power button and the rear stanchion.

1. Ensure that the AWS DeepRacer is powered on.

1. Watch the Wi-Fi LED on the vehicle. If it blinks and then changes from white to blue, the vehicle is connected to the Wi-Fi network. Unplug the USB drive and skip to step 11.
   + If the USB drive was plugged into the vehicle before you attempted to connect the vehicle to a Wi-Fi network, a list of available Wi-Fi networks will be automatically displayed in `wifi-creds.txt` file on your flash drive. Uncomment the one that you want to connect to by removing the pound sign.

1. If the Wi-Fi LED turns red after blinking, unplug the USB drive from the vehicle and plug it back into your computer. Check the Wi-Fi name and password that you entered in the text file for typos, errors in spacing, incorrect sentence casing, or missing or misused single quotation marks. Correct mistakes, and re-save the file, and repeat Steps 7-9.

1. After the vehicle Wi-Fi LED turns blue, unplug the USB drive from the vehicle and plug it into your computer.

1. Open the `wifi-creds.txt` file. Find your vehicle’s IP address at the bottom of the text file and copy it.

1. Make sure your computer is in the same network as the vehicle, then paste the IP address into your web browser.
   + If you are using macOS Catalina, use the Firefox web browser. Chrome is not supported.

1. When prompted with a message that the connection is not private or secure, accept the security warning and proceed to the host page.

Your AWS DeepRacer is now connected to Wi-Fi.

## How to charge the drive module battery
<a name="how-to-charge-the-drive-module-battery"></a>

The AWS DeepRacer drive module battery has two sets of cables with two different color JST connectors, white and red. The white 3-pin connector, at the end of the black, red, and white cables, connects the vehicle module battery to its battery charger. The red 2-pin connector, at the end of the black and red cables, connects the battery to the vehicle drive train.

Follow the steps below to charge your AWS DeepRacer drive module battery:

1. To access the drive module battery if it is connected to the vehicle, lift the compute module, being careful not to loosen the wires connecting it to the drive train.

1. Optionally, to remove the drive module battery from the vehicle, disconnect the red 2-pin battery connector from the black and red drive train connector and unstrap the Velcro strap.

1. Attach the battery to the battery charger by connecting the battery’s white 3-pin connector to the charger port.
   +  *Red light \+ green light = not fully charged*

1. Plug the power cord of the battery charger into a power outlet. When only the green light is illuminated, your battery is fully charged.

1. Disconnect the charged vehicle battery’s white 3-pin connector from the charge adapter. If you removed the battery to charge it (optional) make sure to reconnect its red 2-pin connector to the vehicle drive train connector and secure the battery to the vehicle with the Velcro strap.

1. Turn on the vehicle drive train by pushing its switch to the "on" position. Listen for the indicator sound (two short beeps) to confirm a successful charge. If you don’t hear two beeps, try [unlocking your vehicle battery](#battery-lockout).

## How to charge the compute module battery
<a name="how-to-charge-the-compute-module-battery"></a>

Follow the steps below to charge your AWS DeepRacer compute module battery:

1. Optionally remove the compute module battery from the vehicle.

1. Attach the compute power charger to the compute module battery.

1. Plug the power cord of the compute battery charger into a power outlet.

## My battery is charged but my AWS DeepRacer vehicle doesn’t move
<a name="my-battery-is-charged-but-my-aws-deepracer-vehicle-doesnt-move"></a>

Follow these steps if your AWS DeepRacer console is set up, your compute battery is charged, and your Wi-Fi is connected, but your vehicle still doesn’t move:

1. Lift the compute module, being careful not to loosen the wires connecting it to the drive train. Make sure the vehicle battery underneath is correctly connected, red 2-pin connector to black and red drive train connector.

1. Turn on the vehicle drive train by pushing the switch to the "on" position. Listen for the indicator sound (two short beeps) to confirm that the vehicle has charge. If the vehicle powers on successfully, skip to step 4.

1. If you do not hear two beeps when you switch on your vehicle battery, ensure that the battery is fully charged. Plug the vehicle battery’s white connector cable into its charge adapter, which can be differentiated from the compute module’s adapter by its red and green LED indicator lights. Connect the adapter to its charge cable and plug it into a power outlet. When both red and green lights on the vehicle battery charge adapter are lit, it indicates that the battery still needs charging.

    *Red light \+ green light = **not** fully charged*

   When only the green light is illuminated, your battery is fully charged and ready to use. Disconnect the car battery’s white connector from the charge adapter, and reconnect its red connector to the vehicle. If you removed the battery to charge it (optional) make sure to once again secure it to the drive train with the Velcro strap. Turn on the vehicle drive train by pushing its switch to the "on" position. If you still don’t hear two beeps, try [unlocking your vehicle battery](#battery-lockout).

1. Connect your vehicle to Wi-Fi and open the AWS DeepRacer console in your browser. Manually drive your vehicle with the touch joystick to confirm that it can move.

**Note**
To get the most mileage out of your vehicle battery, make sure to switch off the vehicle drive train or disconnect its battery when you are not using your AWS DeepRacer.

## How to resolve a battery lockout
<a name="battery-lockout"></a>

**Important**
This battery is only for use with the DeepRacer Car. This battery must be handled properly to avoid risk of fire, explosion, or other safety concerns. Follow all instructions and heed all warnings included in the [AWS DeepRacer Device Safety Guide](https://d1.awsstatic.com/legal/AWSDeepRacerDeviceTermsofUse/Global%20AWS%20DeepRacer%20Safety%20Guide%20Sept%202019.pdf).

 **AWS DeepRacer Device Terms, Warranties, and Notices**
+  [AWS DeepRacer Device Terms of Use](https://aws.amazon.com/deepracer/device-terms-of-use/)
+  [One-Year Limited Warranty for AWS DeepRacer Device](https://aws.amazon.com/deepracer/warranty)
+  [AWS DeepRacer Device Safety Guide](https://d1.awsstatic.com/legal/AWSDeepRacerDeviceTermsofUse/Global%20AWS%20DeepRacer%20Safety%20Guide%20Sept%202019.pdf)

 **Preventing a battery lockout**

To preserve battery health, the AWS DeepRacer vehicle battery goes into lockout state. When this happens, the battery won’t power your vehicle even if it’s still partially charged. To prevent your car battery from entering lockout state, do the following:
+ When you finish using your AWS DeepRacer, turn off the vehicle to preserve the battery’s charge.
+ When the device console alerts you that your vehicle battery’s power level is low, charge it as soon as possible.
+ When you think you won’t use AWS DeepRacer for a while, disconnect the battery from the vehicle and fully charge it. We suggest you charge your vehicle battery at least once a year to protect it and prevent lockout.

**Note**
All lithium polymer (LiPo) batteries slowly discharge over time, even when not in use.

 **Unlocking a battery after lockout**

To unlock your vehicle battery after lockout, use the unlock cable, which is a short cable that has a white, 3-pin connector on one end, and a red, 2-pin connector on the other end.

1. Insert battery connectors into the matching colored cable connectors, red to red and white to white.

1. Disconnect the battery from the cable.

1. Your AWS DeepRacer vehicle battery is immediately ready for use. Reconnect its red 2-pin connector to the vehicle drive train connector and secure the battery to the vehicle with the Velcro strap.

1. Turn on the vehicle drive train by pushing its switch to the "on" position. Listen for the indicator sound (two short beeps) to confirm that the battery has been successfully unlocked.

## How to wrap compute module battery connector cable when installing LiDAR sensor
<a name="how-to-wrap-compute-module-battery-connector-cable-when-installing-lidar-sensor"></a>

Fitting the Evo shell over a LiDAR sensor connected to an AWS DeepRacer vehicle using the extra-long Dell USB-C to angle USB-C connector cable requires a specific cable wrapping technique.

To watch a video of this process, see [AWS DeepRacer: Install LiDAR Sensor and wrap Dell compute battery connector cable](https://youtu.be/H4GcdxtJ1OM) on YouTube. The video starts with the installation of the LiDAR sensor on the AWS DeepRacer vehicle. The Dell battery wrapping technique begins at 00:01:27 seconds.

**Note**
The Dell compute battery connector cable has a barrel, a standard USB-C end, and an angle USB-C end.

 **To wrap a Dell battery cable around a LiDAR sensor to accommodate the Evo shell**

1. Facing the rear of the AWS DeepRacer vehicle, plug the angle end of the compute battery connector cable into the compute battery USB-C port with the connector cable pointing to the left.

1. Turning the vehicle slightly to the left, find the opening to the space in between the LiDAR holder and the compute battery just below the rear stanchions and lace the cable through. Stop pulling the cable through when the barrel is inserted into this space. There should be a loop of slack cable to the left of the USB-C port.

1. Facing the rear of the AWS DeepRacer vehicle, wrap the cable counterclockwise around the base of the LiDAR sensor, using the cable clips to secure the cable to itself to ensure a snug fit.

1. Turn the vehicle slightly to the right and plug the standard USB-C end of the cable into the USB-C port.

1. Place the Evo shell on your AWS DeepRacer vehicle and fasten it with pins to test the fit. When the shell fits correctly, the LiDAR sensor is fully visible through the cutout in the shell, and you have access to the pin holes on the top of the stanchions. Remove the shell and adjust your cable as necessary.

Your LiDAR sensor should now be connected. You are ready to turn on your vehicle, drive, and experiment.

## How to maintain your vehicle’s Wi-Fi connection
<a name="how-to-maintain-your-vehicles-wi-fi-connection"></a>

 **How to troubleshoot Wi-Fi connection if your vehicle’s Wi-Fi LED indicator flashes blue, then turns red for two seconds, and finally off**

Check the following to verify you have the valid Wi-Fi connection settings.
+ Verify that the USB drive has only one disk partition with only one `wifi-creds.txt` file on it. If multiple `wifi-creds.txt` files are found, all of them will be processed in the order they were found, which may lead to unpredictable behavior.
+ Verify the Wi-Fi network’s SSID and password are correctly specified in the `wifi-creds.txt` file. An example of this file is shown as follows:

  ```
  ###################################################################################
  #                                   AWS DeepRacer                                 #
  # File name: wifi-creds.txt                                                       #
  #                                                                                 #
  # ...                                                                             #
  ###################################################################################

  # Provide your SSID and password below
  ssid: ' MyHomeWi-Fi'
  password: myWiFiPassword
  ```
+ Verify both the field names of `ssid` and `password` in the `wifi-creds.txt` file are in lower case.
+ Verify that each of the field name and value is separated by one colon (:). For example. `ssid : ' MyHomeWi-Fi'`
+ Verify that the field value containing a space is enclosed by a pair of single quotes. On Mac, TextEdit or some other text editor shows single quotes as of the '…​' form, but not of ‘…​’. If the field value does not contain spaces, the value can be without single quotes.

 **What does it mean when the vehicle’s Wi-Fi or power LED indicator flashes blue?**

If the USB drive contains the `wifi-creds.txt` file, the Wi-Fi LED indicator flashes blue while the vehicle is attempting to connect to the Wi-Fi network specified in the file.

If the USB drive has the `models` directory, the Power LED flashes blue while the vehicle is attempting to load the model files inside the directory.

If the USB drive has both the `wifi-creds.txt` file and the `models` directory, the vehicle will process the two sequentially, starting with an attempt to connect to Wi-Fi and then loading models.

The Wi-Fi LED might also turn red for two seconds if the Wi-Fi connection attempt fails.

 **How can I connect to the vehicle’s device console using its hostname?**

When connecting to the vehicle’s device console using its hostname, make sure you type: `https://hostname.local` in the browser, where `hostname` (of `AMSS-1234` format) is printed on the bottom of the AWS DeepRacer vehicle.

 **How to connect to the vehicle’s device console using its IP address**

To connect to the device console using IP address as shown in the `device-status.txt` file (found on the USB drive), make sure the following conditions are met.
+ Check your laptop or mobile devices are in the same network as the AWS DeepRacer vehicle.
+ Check if you have connected to any VPN, if so, disconnect first.
+ Try a different Wi-Fi network. For example, turn on personal hotspot on your phone.

## How to get the MAC address for your vehicle
<a name="how-to-get-the-mac-address-for-your-vehicle"></a>

Follow the instructions below to get the MAC address of your AWS DeepRacer device:

1. Make sure that your AWS DeepRacer device is only connected to a Wi-Fi network.

1. Connect your AWS DeepRacer device to a monitor. You’ll need a HDMI-to-HDMI, HDMI-to-DVI or similar cable and insert one end of the cable into the HDMI port on the vehicle’s chassis and plug the other end into a supported display port on the monitor.

1. Connect a USB keyboard to your AWS DeepRacer using the USB port on the device’s compute module, after the compute module is booted.

1. Type `deepracer` in the **Username** input field.

1. Type the device SSH password in the **Password** input field.

   If this is your first time logging in to the device, type `deepracer` in the **Password** input field. Reset the password, as required, before moving to the next step. You’ll use the new password for future logins. For security reasons, use a complex or strong password phrase for the new password.

1. After logging in, open a Terminal window. You can use the Search button for the Terminal application.

1. Type the following Ubuntu shell command in the Terminal window:

    `ifconfig | grep HWaddr`

   The command produces an output similar to the following:

    `mlan0 Link encap:Ethernet HWaddr 01:2a:34:b5:c6:de`

   The hexadecimal numbers are the device’s MAC address.

## How to recover your vehicle’s default password
<a name="how-to-recover-your-vehicles-default-password"></a>

Recovering your AWS DeepRacer device console default password involves retrieving or resetting the default password. The default password is printed on the bottom of the device.

Follow the instructions in the following procedure to recover the password for your AWS DeepRacer device web server using an Ubuntu terminal window.

1. Connect your AWS DeepRacer device to a monitor. You’ll need a HDMI-to-HDMI, HDMI-to-DVI or similar cable and insert one end of the cable into the HDMI port on the vehicle’s chassis and plug the other end into a supported display port on the monitor.

1. Connect a USB keyboard to your AWS DeepRacer using the USB port on the device’s compute module, after the compute module is booted.

1. In the **Username**, enter `deepracer`.

1. In **Password**, enter the device SSH password. \+ If this is your first time to log in to the device, enter `deepracer` in **Password**. Reset the password, as required, before moving to the next step. You’ll use the new password for future logins. For security reasons, use a complex or strong password phrase for the new password.

1. After you’re logged in, open a terminal window. You can use the search button to find the terminal window application.

1. To get the default device console password, type the following command in the terminal window:

    `$cat /sys/class/dmi/id/chassis_asset_tag`

   The command outputs the default password as its result.

1. To reset the device console password to the default, run the following Python script in the terminal window:

    `sudo python /opt/aws/deepracer/nginx/reset_default_password.py`

## How to manually update your vehicle
<a name="how-to-manually-update-your-vehicle"></a>

Recent changes in the AWS DeepRacer service has made certain legacy devices, such as those distributed at AWS re:Invent 2018, unable to update automatically. Follow the steps below to manually update such a device.

 **To manually update an AWS DeepRacer device**

1. Download and unzip this [device script](https://docs.aws.amazon.com/deepracer/latest/developerguide/samples/deepracer-device-manual-update.sh.zip).

   The default name of the uncompressed file for this script is `deepracer-device-manual-update.sh`. In this topic, we’ll assume you use this default script file name.

1. Copy the downloaded and uncompressed the script file (`deepracer-device-manual-update.sh`) from your computer to a USB drive.

1. Connect the device to a monitor using a HDMI-HDMI cable, to a USB keyboard, and to a USB mouse.

1. Power on the device and sign into the OS after the device is booted up.

   You’ll need to set the new OS password, if this is your first sign-in to the device.

1. Plug in the USB drive into the device and copy the script file to a folder (for example, \~/Desktop) on the device.

1. From a terminal on the device, type the following command to go to the script file’s folder and to add execution permission to the script file:

   ```
   cd ~/Desktop
   chmod +x deepracer-device-manual-update.sh
   ```

1. Type the following shell command to run the script:

   ```
   sudo -H ./deepracer-device-manual-update.sh
   ```

1. When done with updating the device, open a web browser on your computer or a mobile device and navigate to the device IP address, e.g., `192.168.1.11` in a home network or `10.56.101.13` in an office network.

   Make sure that your device is connected to your Wi-Fi network and use a browser in the same network without tunneling through a VPN.

1. On the device console, type the password for the device console to sign in. Wait for the update screen to show up. When prompted for further updates, follow the instructions therein.

## How to diagnose and resolve common operational issues
<a name="how-to-diagnose-and-resolve-common-operational-issues"></a>

As you explore reinforcement learning with your AWS DeepRacer vehicle, the device may become non functional. The following troubleshooting topics help you diagnose the problems and resolve the issues.

 **Topics**
+  [Why doesn’t the video player on the device console show the video stream from my vehicle’s camera?](#common-operational-issue-001)
+  [Why doesn’t my AWS DeepRacer vehicle move?](#common-operational-issue-002)
+  [Why don’t I see the latest device update? How do I get the latest update?](#common-operational-issue-003)
+  [Why isn’t my AWS DeepRacer vehicle connected to my Wi-Fi network?](#common-operational-issue-004)
+  [Why does the AWS DeepRacer device console page take a long time to load?](#common-operational-issue-005)
+  [Why does a model fail to perform well when deployed to an AWS DeepRacer vehicle?](#common-operational-issue-006)

<a name="common-operational-issue-001"></a> **Why doesn’t the video player on the device console show the video stream from my vehicle’s camera?**

After logging into the AWS DeepRacer device console, you don’t see any live video streamed from the camera mounted on the AWS DeepRacer vehicle in the video player in **Device Controls**. The following could cause this issue:
+ The camera might have a loose connection to the USB port. Unplug the camera module from the vehicle, replug it into the USB port, power off the device, and then power on the device to restart it.
+ The camera might be defective. Use a known working camera from another AWS DeepRacer vehicle, if available, to test whether this is the cause.

<a name="common-operational-issue-002"></a> **Why doesn’t my AWS DeepRacer vehicle move?**

You powered on your AWS DeepRacer vehicle, but you can’t get it to move. The following could cause this issue:
+ The vehicle’s power bank is not turned on or the power bank is not connected to the vehicle. Make sure to connect the provided USB-C-to-USB C cable between the USB-C port on the power bank and the USB-C port on the vehicle chassis. Verify that the LED indicators light up, which indicates the charge levels of the power bank. If not, push the power button on the power bank, and then push the power button on the vehicle’s chassis to boot up the device. The device is booted up when its tail lights light up.
+ If the power bank is on and the vehicle is booted up, but the vehicle does not move in either manual or autonomous driving mode, check if the vehicle’s battery under the vehicle chassis is charged and turned on. If not, recharge the vehicle battery and then turn it on after the battery is fully charged.
+ The vehicle battery cable connectors are not fully plugged into the device driving module power cable connector. Make sure the cable connectors are tightly coupled.
+ The battery cables are defective. Test this battery on another working vehicle, if possible, to test whether this is the cause.
+ The power switch of the vehicle battery is not turned on. Turn on the power switch and make sure you hear two beeps followed by a long beep.

<a name="common-operational-issue-003"></a> **Why don’t I see the latest device update? How do I get the latest update?**

Why is my AWS DeepRacer vehicle’s software outdated?
+ No automatic update is performed on the device lately. You may need to perform a manual update.
+ The vehicle is not connected to the Internet. Make sure the vehicle is connected to a Wi-Fi or Ethernet network with internet access.

<a name="common-operational-issue-004"></a> **Why isn’t my AWS DeepRacer vehicle connected to my Wi-Fi network?**

When I check the network status on the vehicle’s OS, I don’t see the AWS DeepRacer vehicle connected to any Wi-Fi network. This could happen because of the following issues:
+ No Wi-Fi has been configured for the AWS DeepRacer vehicle.
+ The vehicle is out of the active network signal range. Make sure to operate the vehicle within the chosen Wi-Fi network range.
+ The vehicle’s pre-configured Wi-Fi network doesn’t match the available Wi-Fi network.

<a name="common-operational-issue-005"></a> **Why does the AWS DeepRacer device console page take a long time to load?**

When I tried to open the device console of my AWS DeepRacer vehicle, the device console page appears to take a long time to load.
+ Your vehicle is down or off. Make sure the vehicle is powered on when the tail lights are on.
+ The IP address of your vehicle has been changed, most likely by your network’s DHCP server. To find out the vehicle’s new IP address, sign in to the device console with the USB-US cable connection between your computer and the vehicle. View the new IP address in Settings. Alternatively, you can examine the list of devices attached to your network to discover the new IP address. If you’re not a network administrator, ask the administrator to investigate this for you.

<a name="common-operational-issue-006"></a> **Why does a model fail to perform well when deployed to an AWS DeepRacer vehicle?**

After training a model and deploying its artifacts to your AWS DeepRacer vehicle, sometimes the vehicle doesn’t perform as expected. What went wrong?

In general, optimizing a trained model for transfer to a physical AWS DeepRacer vehicle is a challenging learning process. It often requires iterations through trial and error.

The following are some likely common factors affecting the model performance in your AWS DeepRacer vehicle:
+ Your model has not converged in training. Clone the model to continue the training or retrain the model for a longer period of time. Make sure the agent continuously finishes laps in the simulation (that is, 100% process towards the end of the training).
+ Your model was over-trained (that is, over-fitted). It fits too well to the training data, but doesn’t generalize to unknown situations. Retrain the model with a more flexible or accommodating reward function or increase the granularities of the action space. You should also evaluate a trained model on different tracks to see if the model generalizes well.
+ Your AWS DeepRacer vehicle might not have been calibrated properly. To test whether this is true, switch to manual driving and see if the vehicle drives as expected. If it doesn’t, calibrate the vehicle.
+ You are running the vehicle autonomously on a track that doesn’t meet the requirements. For track requirements, see the Build your track section in this guide.
+ There are too many objects close to the physical track, making the track significantly different from the simulated environment. Clear the track surroundings to make the physical track as close to the simulated one as possible.
+ Reflection from the track surface or a near-by object can create glare to confuse the camera. Adjust lighting and avoid making the track on smooth-surfaced concrete floors or with other shiny materials.
