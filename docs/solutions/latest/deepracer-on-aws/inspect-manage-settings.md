---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/inspect-manage-settings.html
---

# Inspect and manage vehicle settings
<a name="inspect-manage-settings"></a>

After the initial setup, you can use the AWS DeepRacer device control console to manage your vehicle’s settings. The tasks include the following:
+ choosing another Wi-Fi network,
+ resetting the device console password,
+ enabling or disabling the device SSH settings,
+ configuring the vehicle’s trail light LED color,
+ inspecting the device software and hardware versions,
+ checking the vehicle battery level.

The procedure below walks you through these tasks.

 **To inspect and manage your vehicle’s settings**

1. With your AWS DeepRacer vehicle connected to the Wi-Fi network, follow the instructions to sign into the vehicle’s device control console.

1. Choose **Settings** from the main navigation pane.
![Settings page overview](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-settings-page.png)

1. On the **Settings** page, perform one or more of the following tasks of your choosing.

   1. To choose another Wi-Fi network, choose **Edit** for **Network settings** and then follow the steps below.

      1. Follow the instructions, shown on **Edit network settings**, to connect your vehicle to your computer using the USB-to-USB-C cable. After the USB connection status becomes **Connected**, choose the **Go to deepracer.aws** button to open the device console login page.
![Edit network settings page](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-network-settings-edit.png)

      1. On the device console login page, type the password printed on the bottom of your vehicle and then choose **Access vehicle**.

      1. Under **Wi-Fi network details**, choose a Wi-Fi network from the drop-down list, type the password of the chosen network, and then choose **Connect**.
![Wi-fi network details page](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-wifi-network-details.png)

      1. After the **Vehicle status** for the Wi-Fi connection becomes **Connected**, choose **Next** to return to the **Settings** page of the device console, where you’ll see a new IP address of the vehicle.

   1. To reset the password for signing into the device console, choose **Edit** for **Device console password** and then follow the steps below.

      1. On **Edit device console password** page, type a new password in **New password**.

      1. Retype the new password in **Confirm password** to confirm your intention for the change. The password value must be the same before you can move on.

      1. Choose **Change password** to complete the task. This option is activated only if you have entered and confirmed a valid password value in the steps above.
![Change password page](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-change-password-page.png)

   1. To enable or disable SSH connection to the vehicle, choose **Edit** for **Device SSH** and then choose **Enable** or **Disable**.
![Device SSH settings](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-ssh-settings.png)

1. To change the vehicle’s trail light LED color to distinguish your vehicle on a track, choose **Edit** for **LED color** on the **Settings** page and do the following.

   1. Choose an available color from the **Select the color of the LEDs** drop-down list on the **Edit LED color** page.

      You should choose a color that can help identify your vehicle from other vehicles sharing the track at the same time.
![LED color selection](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/operatingthevehicle-led-color-settings.png)

   1. Choose **Save changes** to complete the task.

      The **Save changes** functionality becomes active only after you have chosen a color.

1. To inspect the device software and hardware versions and to find out the system and camera configurations, check the **About** section under **Settings**.

1. To inspect the vehicle battery’s charge level, check the lower part of the primary navigation pane.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
