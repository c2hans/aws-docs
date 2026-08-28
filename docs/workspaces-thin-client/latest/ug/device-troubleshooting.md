---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/device-troubleshooting.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Troubleshooting your WorkSpaces Thin Client device
<a name="device-troubleshooting"></a>

If you are having issues with your WorkSpaces Thin Client device, check the following procedures for help.

## Peripherals are not recognized
<a name="peripherals-not-recognized"></a>

If your WorkSpaces Thin Client device is not recognizing the peripherals that you are using, first, verify that they are compatible with WorkSpaces Thin Client. See [Supported devices](supported-peripherals.md) for a list of compatible peripheral devices.

If your peripheral device is compatible with WorkSpaces Thin Client and is still not recognized by the device, do the following:

1. Turn off the WorkSpaces Thin Client device.

1. Disconnect the peripheral device.

1. Reconnect the peripheral device.

1. Check that the USB hub is connected to a power supply with the included hub power adapter.

1. Check that the USB hub is plugged into the WorkSpaces Thin Client device.

1. Turn on your WorkSpaces Thin Client device.

1. Select the **Settings** gear icon on the toolbar, navigate to **Peripheral devices**, and verify the peripheral names.

## Unable to access WorkSpaces Thin Client workspace
<a name="unable-to-access-workspace"></a>

If your WorkSpaces Thin Client device cannot access your virtual WorkSpace, do the following:

1. Go to the network settings on your device.

1. Check that the device is connected to your Wi-Fi network.

1. Refer to the network troubleshooting section of your virtual service interface:
   + For WorkSpaces, go to [Troubleshoot WorkSpaces issues](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-troubleshooting.html)
   + For WorkSpaces Secure Browser, go to [Troubleshooting](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-troubleshooting.html)
   + For WorkSpaces Applications, go to [Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting.html)

## Volume on headset is very low or not audible
<a name="low-headset-volume"></a>

If you are experiencing volume issues with your headset, do the following:

1. Select the toolbar located on the right side of the screen. Go to **Settings** → **Peripheral devices**.

1. Scroll down to the Audio section and adjust the output volume.

**Note**
After a system restart, WorkSpaces Thin Client resets the volume level for connected USB headsets.

## Audio crackles or has disturbances during audio-video conference calls
<a name="audio-crackle"></a>

If you're experiencing audio issues with your WorkSpaces Thin Client, try one of the following procedures:

**Check your WorkSpaces Thin Client device**

1. Check that the audio USB headset is connected to the USB hub and that the USB hub is turned ON.

1. Check for supported peripheral devices to ensure that your device is supported.

**If you are on the login screen of a VDI session**

1. Select **Settings** at the top right of the screen.

1. Locate the device ID.

1. Run a diagnostic check and ensure that the device and advanced logging are both enabled.

**If you are currently in a VDI session**

1. Go to the toolbar on the right side of the screen.

1. Select **Settings** → **Peripheral Devices** → **Audio**.

1. Check that your USB headset is listed and that the volume is set to your desired level.

1. Check that the device is connected to Wi-Fi or Ethernet and that there is no issue with the connection to WorkSpaces.

**If you are not currently in a VDI session**

1. On the WorkSpaces login page, select **Settings** at the top right of the screen.

1. Locate the device ID.

1. Check that diagnostics and advanced logging are enabled.

## Secondary monitor goes dark during VDI session
<a name="dectect-display"></a>

If your second monitor goes dark while you are using it, try one of the following procedures:

**Detect display from **Settings****

1. Go to **Settings** then **Peripheral devices**.

1. Select **Detect Extended Display** under **DISPLAY RESOLUTION**.
![Settings page showing mouse, display resolution, and sound options with "Detect Extended Display" highlighted.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/settings-dectect-display.jpeg)

**Detect display from VDI toolbar**

1. Open your VDI toolbar.

1. Select **Detect Displays** on the toolbar.
![Amazon WorkSpaces desktop with icons and a side menu highlighting "Detect Displays".](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/silk-dectect-display.jpeg)

After doing either procedure, the secondary monitor should come back on. If the problem continues, restart your WorkSpaces Thin Client device.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
