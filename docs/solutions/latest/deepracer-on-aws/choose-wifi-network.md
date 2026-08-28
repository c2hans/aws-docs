---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/choose-wifi-network.html
---

# Set up your vehicle
<a name="choose-wifi-network"></a>

The first time you open your AWS DeepRacer vehicle, you must set it up to connect to a Wi-Fi network. Complete this setup to get the vehicle’s software updated and to get the IP address to access the vehicle’s device console.

This section walks you through the steps to perform the following tasks:
+ Connect your laptop or desktop computer to your vehicle.
+ Setup the vehicle’s Wi-Fi connection.
+ Update the vehicle’s software.
+ Get the vehicle’s IP address.
+ Test drive the vehicle.

Use a laptop or desktop computer to perform the setup tasks. We’ll refer to this setup computer as your computer, to avoid possible confusion with the vehicle’s compute module, which is running the Ubuntu operating system.

After the initial setup of the Wi-Fi connection, you can follow the same instructions to choose a different Wi-Fi network.

**Note**
AWS DeepRacer does not support Wi-Fi network that requires active captcha verification for user sign-in.

 **Topics**
+  [Get ready to setup Wi-Fi connection for your AWS DeepRacer vehicle](#get-ready-setup-wifi)
+  [Setup Wi-Fi connection and update your AWS DeepRacer vehicle’s software](#setup-wifi-update-software)

To setup your vehicle’s Wi-Fi connection, connect your a laptop or desktop computer to your vehicle’s compute module using the included USB-to-USB C cable.

To connect your computer to your vehicle’s compute module, follow the steps below.

1. Make sure your computer is disconnected from Wi-Fi before connecting your device.

1. Insert the USB end of the USB-to-USB C cable into your computer’s USB port.

1. Insert the cable’s USB C end into your vehicle’s USB C port.

You’re now ready to proceed to setting up your vehicle’s Wi-Fi connection.

Before you follow the steps here to setup the Wi-Fi connection, be sure you complete the steps in [Get ready to setup Wi-Fi connection for your AWS DeepRacer vehicle](#get-ready-setup-wifi).

1. Look at the bottom of your vehicle and make note of the password printed under Hostname. You’ll need it to login to the device control console to perform the setup.

1. On your computer, go to link:https://deepracer.aws to launch the device control console of your vehicle.

1. When prompted with a message that the connection is not private or secure, do one of the following.

   1. In Chrome, choose **Advanced** and then choose **Proceed to <device\_console\_ip\_address> (unsafe)**.

   1. In Safari, choose **Details**, follow the **visit this website** link, and the choose **Visit Websites**. If prompted for your password to update the certificate trust settings, type the password and then choose **Update settings**.

   1. In Opera, choose **Continue Anyway** when warned of an invalid certificate.

   1. In Edge, choose **Details** and then choose **Go on to the webpage (Not recommended)**.

   1. In Firefox, choose **Advanced**, choose **Add Exception**, and then choose **Confirm Security Exception**.

1. Under **Unlock your AWS DeepRacer vehicle**, enter the password noted in Step 1 and then choose **Access vehicle**.

1. On the **Connect your vehicle to your Wi-Fi network** pane, choose your Wi-Fi network name from the **Wi-Fi network name (SSID)** drop-down menu, type the password of your Wi-Fi network under **Wi-Fi password**, and choose **Connect**.

1. Wait until the Wi-Fi connection status changes from **Connecting to Wi-Fi network…​** to **Connected**. Then, choose **Next**.

1. On the **Software update** pane, if a software update is required, turn on the vehicle’s compute module, with the included power cord and power adapter, and then choose **Install software update**.

   Powering the vehicle with an external power source helps avoid interruption of the software update if the compute module’s power bank become discharged.

1. Wait until the software update status changes from **Installing software update** to **Software update installed successfully**.

1. Note the IP address shown under **Wi-Fi network details**. You’ll need it to open the vehicle’s device control console after the initial setup and any subsequent modification of the Wi-Fi network settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
