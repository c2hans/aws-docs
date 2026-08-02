---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html
---

# Configuring a Link device
<a name="device-edit"></a>

The Link device has properties that control how it behaves when it is streaming. You should set these properties every time you get ready for a new video event.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Link input devices**. Find the Link that you want. If there are many devices listed, enter part of the name to filter the list.

1. Choose the hyperlink for the device. The **Device details** page for this device appears.

1. Choose **Modify** then **Configure device**. Change fields. For details about each field, see the sections after this procedure. Then choose **Update**.

   MediaLive sends the new values (except for the name) to the devices, so that the device can update itself.

1. Display the **Device details** page and take the appropriate action:
   + If the device is not attached to a MediaLive input or a MediaConnect flow, watch for the state of the device to return to **Idle**. You can now start the channel (which automatically starts the device), or you can start the device and the flow.
   + If the device is currently attached to a MediaLive input or a MediaConnect flow that is active, watch for the state of the device to return to **In use**. Note that there is no need for you to restart the input or flow.

| Field | Description |
| --- | --- |
| Name | Enter a descriptive nickname for the device, for use only in MediaLive.  |
| Input source | Configures the source that Link sends to MediaLive: SDI or HDMI.[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/device-edit.html) |
| Maximum bitrate | Set a value if you want to throttle the delivery bitrate to MediaLive. <br />Leave this field blank to let the device determine the bitrate that is best for the network conditions between the device and MediaLive. |
| Latency | Set the device buffer size (latency). [See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/device-edit.html)If you leave this field blank, the service uses the default value. <br />Default: 1000 ms (HD devices) or 2000 ms (UHD devices). <br />Minimum: 0 ms. Maximum: 6000 ms. |
| Availability Zone | The Availability Zone (AZ) for the device. This field has an effect only when the device is attached to a MediaLive input. It is ignored when the device is attached to a flow.You should change the Availability Zone for the device whenever the device needs to belong to a different Availability Zone. Key use cases for changing the Availability Zone are the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/device-edit.html)You can change the Availability Zone only when the device is attached to a MediaLive input. Typically you change the Availability Zone only when you're deploying it to use it with a new channel. Even if you stop the channel (which automatically stops the device), you can't simply change the Availability Zone. Doing so would probably make the channel inoperable. |
| Codec | This field applies only when the device is connected to a MediaConnect flows. Set this field to the codec you want to use for the event that you are getting ready for. The default is HEVC.Note the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/device-edit.html) |
| Input resolution | This field applies only if the device is a UHD device and only when the device is the source for a MediaLive input.<br />Choose the resolution to match the resolution that the device is sending, either HD or UHD. MediaLive uses the value you specify here to calculate the input charges that you will incur — either the charge for HD or the charge for UHD.Note the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/device-edit.html) |
