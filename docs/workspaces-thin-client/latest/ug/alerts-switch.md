---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/alerts-switch.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# System and network alerts
<a name="alerts-switch"></a>

WorkSpaces Thin Client uses alerts to inform you of system and network issues that may affect your device. Some of these notifications contain a button to restart the device when it is updated or modified.

These notifications are, by default, disabled. If desired, they can be enabled.

**Note**
 This feature should only be enabled for troubleshooting issues. It is not intended for daily use.

## Enabling system alerts
<a name="system-alerts"></a>

As part of the operating system of your WorkSpaces Thin Client device, you will receive notifications regarding your system. These notifications alert you if you experience any change to you device or connected peripheral. Some of them include:
+ Monitor added
+ Monitor removed

If needed, you can turn on these notifications. By default, notifications are set to **Off**.

**Turning network notifications on and off**

1. Open the toolbar on the side of your display.

1. Select **Settings**, **About**, **SYSTEMS ALERT**.

1. Select the switch to **On** to enable the notifications.
![Settings interface showing options for About Device, Network Alerts, and System Alerts with toggle switches.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/notifications-system.png)

## Enabling network alerts
<a name="network-alerts"></a>

As part of the operating system of your WorkSpaces Thin Client device, you will receive notifications regarding your network. These notifications alert you if you experience any degraded network conditions. Some of them include:
+ Ethernet or WiFi Network disruptions
+ Wifi signal strength
+ Packet loss or data lost in transmission

If needed, you can turn on these notifications. By default, notifications are set to **Off**.

**Turning network notifications on and off**

1. Open the toolbar on the side of your display.

1. Select **Settings**, **About**, **NETWORK CONDITIONS ALERT**.

1. Select the switch to **On** to enable the notifications.
![Settings interface showing network condition alerts off and system alerts on.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/notifications-network.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
