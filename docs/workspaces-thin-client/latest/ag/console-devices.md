---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/console-devices.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Devices
<a name="console-devices"></a>

Each WorkSpaces Thin Client end user has a dedicated device that connects them to their virtual desktop environments and online resources. These devices are managed through the WorkSpaces Thin Client administrator console on the [AWS site](https://aws.amazon.com/).

From this console, you can order devices for your team.

## Device list
<a name="device-list"></a>

There are a number of parameters for any device in your network for you to review as well as some actions you can take.

![Devices table showing device ID G0723H08 with active status and no device name assigned.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/device-list.png)

### Device list details
<a name="device-list-details"></a>

The parameters for your device are listed for your review. The following table lists each element in the summary and how it functions.

| Element | Description |
| --- | --- |
| Device serial number | The identification number assigned to an individual device. |
| Device name | (optional) The unique name that you give to a device. |
| Last used by | The identification number of the user accessing the device. Only available when using WorkSpaces Personal. |
| Activity status | The current status of a device. There are two status states:+ **Active** – Connected to a network at least once in the past seven days.<br />+ **Inactive** – Not connected to a network in the past seven days. |
| Enrollment status | Confirmation that a device has been set up, is associated with this AWS account, and is part of a specific environment. It can be in one of the following states:+ **Registered** – This is the default status.<br />+ **Deregistering** – The device is in the **Reset and Deregister** process. You can delete a device if it is in a deregistering state. <br />+ **Deregsitered** – The device has been successfully deregistered. You can only delete a device if it’s in either a **Deregistering** or **Deregistered** status. <br />+ **Archived** – The device is archived. |
| Environment ID | The identifier of the environment to which this device is attached. |
| Software compliance | The compliance status of the device software. There are two status states:+ **Compliant**<br />+ **Not compliant** |

### Device list actions
<a name="device-list-actions"></a>

There are a number of actions you can perform from here. Select any of these to perform the corresponding action.

| Element | Description |
| --- | --- |
| Search | Searches all devices that you manage. |
| Refresh | Refreshes the device list. |
| View details | Displays Device details. |
| Actions | Opens a dropdown list where you can do the following:+ [Edit device name](editing-a-device-name.md)<br />+ [Deregister](resetting-and-deregsitering-a-device.md)<br />+ [Archive](archiving-a-device.md)<br />+ [Delete](deleting-a-device.md)<br />+ [Export device details](exporting-device-details.md) |
| Order devices | Starts the process of ordering devices. |

**Topics**
+ [Device list](#device-list)
+ [Device details](device-details.md)
+ [Editing a device name](editing-a-device-name.md)
+ [Resetting and deregistering a device](resetting-and-deregsitering-a-device.md)
+ [Archiving a device](archiving-a-device.md)
+ [Deleting a device](deleting-a-device.md)
+ [Exporting device details](exporting-device-details.md)
