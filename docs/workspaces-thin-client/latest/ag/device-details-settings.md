---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-details-settings.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Device settings
<a name="device-details-settings"></a>

The parameters for your device are listed for your review. The following table lists each element and how it functions.

**Note**
Device settings information is updated only when device is online. If device is offline, some information may be out of date.

## Heading and Network
<a name="device-settings-network"></a>

WorkSpaces Thin Client device details provides an overview of the device's network connections. The following table lists each element and how it functions.

![Network section showing connection type as ETHERNET with Connected status.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/device-settings-network.png)

| Element | Description |
| --- | --- |
| Last synced on | The date and time of the most recent device settings sync with console. |
| Connection type | The type of network connection used by the device. The connection type can either be Ethernet or Wifi. |
| Status | The status of the network. If the device is currently connected, or connected within the past 20 minutes, the status will show up as ‘connected’. If the network has been disconnected for more than 20 min, the status will change to show the time passed since the device is last connected to internet, e.g. “last connected 20 minutes ago”. |
| Local IP address | The local IP address of the connected network. |
| Gateway address | The gateway address of the connected network. |

## Bluetooth and peripheral devices
<a name="device-settings-peripheral"></a>

WorkSpaces Thin Client device details provide a list of any connected peripherals connect to a device. The following table lists each element and how it functions.

![Bluetooth and peripheral devices settings showing 5 connected USB devices including mouse, keyboard, speaker, microphone, and webcam.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/device-settings-peripheral.png)

| Element | Description |
| --- | --- |
| Bluetooth | The Bluetooth status of the device. The two status states are:+ Enabled<br />+ Disabled |
| Connected peripheral devices | The list of names of the connected peripherals, such as Logitech mouse, and the type of the connected peripherals, such as Mouse (USB). |

## Power and sleep
<a name="device-settings-sleep"></a>

Each WorkSpaces Thin Client device has a power saving mode. The following table lists the status of this mode.

![Power and sleep section showing Turn off display after setting configured to Never.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/device-settings-power.png)

| Element | Description |
| --- | --- |
| Turn off display after | The period of inactive time after which the device turns off its display. |
