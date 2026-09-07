---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/known-issues.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Known issues for the WorkSpaces Thin Client
<a name="known-issues"></a>

 The WorkSpaces Thin Client has the following known issues.

## If you select any link on the VDI login screen, you must return to the login screen.
<a name="vdi-login-screen"></a>

**Workaround:** Select the Lock/Unlock button. This returns you to the VDI login, and a second monitor will mirror the primary monitor.

## Using keyboard shortcuts may cause unexpected behavior.
<a name="keyboard-shortcuts"></a>

**Workaround:** There is no workaround for this issue.

## Some peripherals may not be recognized when the device is running.
<a name="peripherals-not-recognized"></a>

**Workaround:** Unplug the device and then plug it back in or reboot the device.

## You cannot view the IP address of the Ethernet network from settings.
<a name="cannot-see-ip-address"></a>

**Workaround:** There is no workaround for this issue.

## Some menu options in the VDI toolbar are displayed but not working.
<a name="vdi-toolbar"></a>

**Workaround:** These features are not enabled in this release.

## You cannot find a [supported keyboard layout](keyboard-layouts.md) in the OOBE or settings.
<a name="eu-keyboard"></a>

**Workaround:** Check that you are using software set 2.2.0 or higher. Check for the most current software set in [WorkSpaces Thin Client software releases](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-software-sets.html). You can also use an Ethernet connection if you cannot enter your Wi-Fi password without keyboard layout support.

## You can select a supported keyboard layout in device settings, but you cannot enter the specific keys within the virtual session.
<a name="eu-keyboard-vdi"></a>

**Workaround:** Check that the input method within the session is set to the corresponding language. For example, if you want to use an Italian layout keyboard, set the input method to Italian within the session. See the following figure.

![Italian keyboard layout](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/windows_language_input.png)

## Toolbar does not expand or collapse when you select it for the first time.
<a name="toolbar-first-expand"></a>

**Workaround:** Make sure the mouse pointer is on the primary monitor and try expanding or collapsing the toolbar again. To expand the toolbar, select the dark area over the collapsed toolbar. To collapse the toolbar, select any area on the primary monitor.

## On waking up from sleep, WorkSpaces Thin Client device shows the keyboard and mouse setup screen for a few seconds before launching the session.
<a name="waking-from-sleep"></a>

**Workaround:** The keyboard and mouse setup screen should automatically go away. If the screen remains after a few seconds, unplug the device and then plug it back in or [reboot the device](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/rebooting-device.html).

## On the restart of a WorkSpaces Thin Client device, end users will see repeated **Getting Ready** and **Checking for updates** transition screens before launching the session.
<a name="repeated-transitions"></a>

**Workaround:** None

## Updates for the WorkSpaces Thin Client device are not taking effect.
<a name="updates-no-effect"></a>

**Workaround:** Restart the device after every system update.

## The webcam is not enabled in WorkSpaces and its icon in the top toolbar remains gray.
<a name="webcam-not-enabling"></a>

**Workaround:**

1. Confirm your webcam is properly connected to your WorkSpaces Thin Client device.

1. Wait 30 seconds after your WorkSpaces session starts.

1. Check to see if your webcam is automatically enabled.

1.  If it is still not enabled, restart your WorkSpaces Thin Client device and check again.

## 4K monitor not at full resolution
<a name="vdi-resolution"></a>

WorkSpaces Thin Client supports up to 3840x2160 (4K) resolution on the primary monitor. With the scaling factor, you can stream 4K in WorkSpaces. However, WorkSpaces Secure Browser might not support 4k yet.

**Workaround:** None.

## WorkSpaces Thin Client Packet Loss notification.
<a name="packet-loss"></a>

**Workaround:**

The system may show no Packet Loss even if packet loss is occurring, please ignore the no packet loss message.

## Keyboard power operation is not correct in device settings
<a name="keyboard-power-issue"></a>

If a keyboard is turned on/off using its native power switch, the status may not reflect accurately in the device settings.

**Workaround:**

None.

## Headset volume change not reflected in device settings
<a name="headset-volume"></a>

For headsets with its own amplifier, pressing the volume button on the headset may not change the volume level shown in device settings.

**Workaround:**

None.

## Screen shows multiple updating screen fragments after reset
<a name="distorted-display"></a>

On monitors with 2560 x 1440 resolution and after you reset the WorkSpaces Thin Client device, the monitors display the AWS updating screen tiled across them.

**Workaround:**

None. The device reset works as expected and the screen will return to normal.

## Network icon opening Accessibility settings
<a name="accessibility-network-icon"></a>

Selecting the Network Icon on activation code screen may direct users to accessibility settings instead of network settings.

**Workaround:**

Enter your activation code to complete setup. The issue will resolve after the device updates to the latest software version.

## Server error code 1001 during setup
<a name="device-server-error"></a>

Device encounters server error (code 1001) at the end of setup.

**Workaround:**

The device needs to be reset and set up again.

1. Select the network icon to open **Settings**.

1. Select **About**.

1. Select **Reset device**.

1. Set up your device. See [Setting up your Amazon WorkSpaces Thin Client service](setting-up.md).

## FIDO2 details
<a name="fido2-prerelease"></a>

The FIDO2 feature is in a prerelease state and has some limitations to its use.

**Limitations:**
+ Only Yubico YubiKey 5 series USB security keys are supported with FIDO2/WebAuthn supported.
+ Yubico YubiKey bio-metric keys are not supported.
+ Registration flow requiring new PIN creation (i.e. `userVerification` set to `required`) is not supported. However if a PIN was previously set on the USB security key then it is supported.
+ Cross-origin WebAuthn credential creation is not supported.
+ Related Origin Requests are not supported.
+ Origin must use https scheme. Origin with ports are not supported (e.g: `https//example.com:8443`).
+ Only one USB security key can be connected at a time to the Amazon WorkSpaces Thin Client. Multiple USB security keys connected simultaneously is not supported.

## Disconnected from your WorkSpaces Applications session
<a name="as2-disconnect"></a>

When **Disconnect** on the toolbar is selected, you'll see a sign out page. This could be the regular WorkSpaces Applications sign out page or a custom page your administrator set up. After signing out, the **Sign In** button is missing from both the toolbar and the sign out page.

**Workaround:**

Do one of the following:
+ Restart the WorkSpaces Thin Client device.
+ Unlock the WorkSpaces Applications session by doing the following:

  1. Select the **Lock** button on the WorkSpaces Applications toolbar. The **Lock** page appears.

  1. Select **Unlock**. The sign on page appears.

  1. Sign in to start the session again.
