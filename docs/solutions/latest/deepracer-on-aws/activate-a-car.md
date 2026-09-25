---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/activate-a-car.html
---

# Activate a car
<a name="activate-a-car"></a>

Activating a car onboards it so that you can manage it remotely. Only administrators can activate a car.

 **To activate a car**

1. Choose **Devices** under **Device management** in the left sidebar.

1. From the device list, choose **Add device** to open the activation wizard.
![Add device button opening the activation wizard](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/device-management/activate-device-wizard-step-1.png)

1. For device type, select **Car**.
![Selecting the device type in the activation wizard](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/device-management/activate-device-wizard-step-1b-device-type-list.png)

1. Select a **fleet** for the car. A fleet is required.
![Selecting a fleet in the activation wizard](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/device-management/activate-device-wizard-step-2-fleet-selection-view.png)

1. For **device name**, enter a name with a maximum of 64 characters.

1. Enter a device-console password.

1. (Optional) Set a hidden Wi-Fi SSID and enable the Community Beta Console.
![Configuring the device name and options in the activation wizard](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/device-management/activate-device-wizard-step3-configure-device-view.png)

1. Choose **Generate** to produce a copy-and-paste activation command. You can also download the command as a script.

1. Run the command on the car as an administrator or root user. The command installs the AWS Systems Manager agent, customizes the car, and reboots it.

When the car reconnects, it appears in the selected fleet with the status **Online**, and the wizard confirms that the device is online.

![The activation wizard confirming the device is online](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/device-management/activate-device-wizard-step-5.png)

**Note**
Activation codes expire 24 hours after they are generated. If the code expires before you run it, generate a new one.
