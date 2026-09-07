---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/managing-display-resolution.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Managing the display resolution
<a name="managing-display-resolution"></a>

WorkSpaces Thin Client supports a maximum of two displays - the primary monitor and the extended monitor.

If you have a second monitor connected, your display automatically extends to the second monitor on the launch of a desktop session and the online remote desktop toolbar shows a **Multiscreen** button. You can use this button to switch from using a single screen to using two screens. For more information, see the **Web browser client** section of [ Extending full-screen across all monitors](https://docs.aws.amazon.com/dcv/latest/userguide/full-screen-all-monitors.html) in the *Amazon DCV User Guide*.

Your device determines the best resolution to use with each of your displays when you start your device. The maximum supported resolution depends on the number of displays you have connected, as shown in the following table.

| Displays | Maximum Resolution |
| --- | --- |
| 1 (Primary monitor only) |  + Regular 1080p monitor – 1920x1080 (aspect ratio of 16:9)<br />+ 2K monitor – 2560x1440 (aspect ratio of 16:9)<br />+ 2K ultra-wide (UWD) monitor – 3440x1440 (aspect ratio of 21:9)<br />+ 4K monitor – 3840x2160 (aspect ratio of 16:9)  |
| 2 (Extended monitor) | 1920x1080 |

**Note**
While primary 4K monitors and 4K ultra-wide monitors are capable of the maximum resolution listed, some virtual desktop interfaces will have a lower resolution. See [4K monitor not at full resolution](known-issues.md#vdi-resolution).

## Connecting a 2K or 4K monitor
<a name="connecting-4k"></a>

2K and 4K resolution is only available through the primary monitor HDMI port located on your WorkSpaces Thin Client device.

![Device back panel with HDMI IN and HDMI OUT ports, with HDMI OUT port indicated.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/monitor-port.jpg)

WorkSpaces Thin Client automatically recognizes ultra-high definition (2K or 4k) monitors when they are connected to the primary monitor HDMI port. For a list of supported 2K and 4K monitors, see [Supported peripherals](supported-peripherals.md).

**Note**
You cannot use an extended monitor if you configure your primary monitor for 2K, 2K ultra wide, or 4K resolution.

**Using 4K resolution on WorkSpaces Thin Client**

1. Connect a 2K or 4k monitor to the HDMI OUT port located on the WorkSpaces Thin Client device.

1. Turn on the device.

The device should recognize the high density display and set the resolution automatically.

## Changing the display resolution
<a name="changing-display-resolution"></a>

You can change the resolution of your WorkSpaces Thin Client device display. If needed, you can lower your resolution setting on your 4K monitor.

If you lower your 2K or 4K display to a standard resolution, WorkSpaces Thin Client will remember this preference and start up in 1080p mode for that display. If this setting is not changed, 4K displays will continue to use 4K resolution automatically. This preference can be removed by resetting the resolution. For more information, see Resetting the display resolution.

**Note**
The WorkSpaces Thin Client device must be shut down before connecting a new display or switching between displays. Once the new display is connected, power up the device and set your resolution.

**Changing the display resolution**

1. Select **Settings** from the toolbar on the primary monitor.

1. Select **Peripheral Devices**.

1. Go to **Display Resolution**.

1. Select **Primary Monitor** to open the drop down menu.
![Settings page showing Peripheral devices section with mouse, display, sound, and camera options.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/scaling.png)

1. Select one of the following:
   + 3840x2160 – 4K resolution when using a single monitor that supports ultra-high definition.
   + 1920x1080 – Standard resolution when using any two monitors.

1. Select **Scaling** and select the desired setting from the drop down list.

1. Restart your device by selecting **Yes** in the pop-up window.
![Dialog box with No and Yes buttons to confirm resolution change and device restart.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/resolution_popup.png)

## Resetting the display resolution
<a name="reset-resolution"></a>

You can choose to reset the display preferences of your WorkSpaces Thin Client device. This deletes any preferences set for all connected displays. The device resets the setting back to the highest supported resolution for that display.

**Resetting the display resolution**

1. Select **Settings** from the toolbar on the primary monitor.

1. Select **Peripheral Devices**.

1. Go to **Display Resolution**.

1. Select **Clear display resolution preferences**.

1. Select **Restart** in the pop up window.
