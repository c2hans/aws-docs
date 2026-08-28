---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/enabling-mic-webcam.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Enabling the microphone and webcam
<a name="enabling-mic-webcam"></a>

Your WorkSpaces Thin Client device can connect to your audio and visual devices. To use your microphone and webcam within a virtual desktop session, you will need to enable permissions in your Windows Settings, on the virtual desktop toolbar, and your browser settings.

WorkSpaces Thin Client is compatible with the webcams and headsets listed in the [Peripherals](supported-peripherals.md) section.

Confirm your webcam and microphone are properly connected to your WorkSpaces Thin Client.

1. Go to **Settings**.

1. Select **Peripheral Devices**.

1. Verify that your webcam and microphone are listed.
![Peripheral devices settings showing connected mouse, sound devices, and camera listed.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/confirm_webcam_microphone.png)

1. Verify that your microphone and webcam are enabled on your VDI. Depending on what VDI you are using, do one of the following:
   + For Windows, use [Enabling permissions in Windows](#enabling-mic-webcam-windows).
   + For Amazon WorkSpaces, use [Enabling permissions in Amazon WorkSpaces](#enabling-mic-webcam-ws).
   + For WorkSpaces Applications or Amazon WorkSpaces Secure Browser, use [Enabling permissions in WorkSpaces Applications and Amazon WorkSpaces Secure Browser](#enabling-mic-webcam-vdi).

## Enabling permissions for microphone and webcam in the VDI
<a name="enabling-permissions-mic-webcam"></a>

### Enabling permissions in Windows
<a name="enabling-mic-webcam-windows"></a>

1. Select the **Settings** icon.

1. Select the **Privacy** icon from the **Settings** menu.
![Windows Settings menu with Privacy option highlighted in red box.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/windows-settings-privacy.jpg)

1. Do one of the following:
   + Select **Camera** from the list on the left, and change **Allow apps to access your camera** to **On**.
![Camera settings page with Camera option selected in left navigation menu.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/windows-settings-camera.jpg)
   + Select **Microphone** from the list on the left, and change **Allow apps to access your camera** to **On**.
![Microphone settings page with Microphone selected in left navigation and toggle options.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/windows-settings-microphone.jpg)

After you have enabled permissions in Windows, you will need to enable them from your web browser. See [Enabling permissions in the web browser](#enabling-mic-webcam-browser).

### Enabling permissions in Amazon WorkSpaces
<a name="enabling-mic-webcam-ws"></a>

Permissions for webcam and microphone are automatically enabled for use with WorkSpaces Thin Client.

The virtual desktop toolbar will display the status of you microphone and webcam.

WorkSpaces Thin Client is compatible with the webcams and headsets listed in the [Peripherals](supported-peripherals.md) section.

Confirm your webcam and microphone are properly connected to your WorkSpaces Thin Client.

![Windows desktop showing default blue background with desktop icons and taskbar.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/dcv-toolbar.png)

The icons for **Microphone** and **Webcam** will indicate their status.

| Icon | Status |
| --- | --- |
| ![Circular icon with an X symbol inside, representing cancellation or closure.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/cam-off.png)  | Camera is not on. |
| ![Blue circular icon with a white webcam or video camera symbol inside.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/cam-enabled.png)  | Camera is on but not streaming. |
| ![Webcam icon with circular target symbol in the center, representing video capture.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/cam-streaming.png)  | Camera is on and streaming. |
|  ![Microphone icon with a zero and multiplication symbol, indicating muted audio.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/mic-off.png)  | Microphone is not on. |
| ![Microphone icon enclosed in a blue circle, representing audio input or voice recording.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/mic-enabled.png)  | Microphone is on. |

After you have confirmed that your peripheral is enabled in Amazon WorkSpaces, you will need to enable them from your web browser. See [Enabling permissions in the web browser](#enabling-mic-webcam-browser)

### Enabling permissions in WorkSpaces Applications and Amazon WorkSpaces Secure Browser
<a name="enabling-mic-webcam-vdi"></a>

Your WorkSpaces Thin Client device can connect to your audio and visual devices. To use your microphone and webcam within a virtual desktop session, you will need to enable permissions in your Windows Settings, on the virtual desktop toolbar, and your browser settings.

Confirm your webcam and microphone are properly connected to your WorkSpaces Thin Client.

1. Go to **Settings**.

1. Select **Peripheral Devices**.

1. Verify that your webcam and microphone are listed.

After you have confirmed that your peripheral is enabled in either WorkSpaces Applications or Amazon WorkSpaces Secure Browser, you will need to enable them from your web browser. See [Enabling permissions in the web browser](#enabling-mic-webcam-browser).

## Enabling permissions in the web browser
<a name="enabling-mic-webcam-browser"></a>

1. A pop-up window will appear asking for Microphone and Webcam permissions. If you do not see the pop-up, you can select the icon next to the address bar.
![Permission dialog requesting access to camera and microphone with Allow and Block buttons.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/enable_browser.png)

1. Select Allow in the pop up window.

1. Select the **Settings** icon on the browser search bar and make sure **Microphone** and **Webcam** are enabled.
![Browser permissions panel showing Camera, Microphone, and Notifications enabled for app.chime.aws.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/confirm_broswer.png)

**Note**
You may need to repeat the above step every time you want to use your webcam and microphone in a website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
