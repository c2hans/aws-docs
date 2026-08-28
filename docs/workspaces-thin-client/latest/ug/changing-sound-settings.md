---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/changing-sound-settings.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Changing the Sound settings on the WorkSpaces Thin Client
<a name="changing-sound-settings"></a>

WorkSpaces Thin Client has a couple of sound settings that you can configure including volume and microphone muting.

## Setting the volume level from your virtual desktop
<a name="volume-settings"></a>

After you set up your peripheral, you can control your volume settings through the VDI toolbar or on the device. For more information, see [Changing the Sound settings on the WorkSpaces Thin Client](#changing-sound-settings).

For more information on your VDI toolbar, refer to the following:
+ For Amazon WorkSpaces Secure Borwser see [WorkSpaces Secure Browser Access](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-web-access.html)
+ For WorkSpaces Applications see [Web Browser Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-user.html#web-browser-access-v2)
+ For Amazon WorkSpaces Web see [Use the toolbar](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/use-toolbar.html)

After you set the volume it stays at that level, even if you restart your Amazon WorkSpaces Thin Client.

## Changing the default volume of the WorkSpaces Thin Client
<a name="changing-volume"></a>

Your WorkSpaces Thin Client device has two default volume settings depending on the peripheral.
+ Default volume for the WorkSpaces Thin Client device is 73.
+ Default volume for a connected headset is 40.

You can change these defaults.

**Changing the default volume (Output) of the device speaker**

1. Disconnect any headset from the device.

1. Change the volume by doing one of the following:
   + Go to **Settings**, **Peripheral Devices**, **Sound**, and change the **Output-Speaker** by using the \+ and − icons.
![Settings menu showing peripheral devices, with sound output speaker volume set to 73.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/sound2.png)
**Note**
Your built-in speaker volume stays the same even if you restart the device or change the volume of the headset.
   + Press the \+ and − volume buttons on the top of the device to raise or lower the volume.
![Smart speaker device with volume buttons on top and a blue light strip.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/volume-buttons.jpg)

**Changing the default volume (Output) of the headset**

1. Connect a headset to the device.

1. Change the volume by doing the following:
   + Go to **Settings**, **Peripheral Devices**, **Sound**, and change the **Output-Speaker** by using the \+ and − icons.
![Settings menu showing peripheral devices, with sound output speaker controls highlighted.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/sound1.png)
   + Press the \+ and − volume buttons on the top of the device to raise or lower the volume.
![](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/volume-buttons.jpg)
   + If your headset has volume buttons attached to it, you can use them.

## Using Mute on WorkSpaces Thin Client
<a name="muting-mic"></a>

You can use the Mute function by doing one of the following:
+ If you want to mute all connected and built-in microphones on your WorkSpaces Thin Client, use the **Mute** button on the top of the device. The icon on the button will glow red when Mute is activated.
![Cube-shaped device with light bar, microphones, and mute button for WorkSpaces Thin Client.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/mic-mute.jpg)
+ If you want to mute just the device microphone, connect a headset with microphone to the device. The device microphone is automatically muted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
