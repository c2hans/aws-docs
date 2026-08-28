---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/aws-elemental-link-input-configuration.html
---

# AWS Elemental Link input configuration
<a name="aws-elemental-link-input-configuration"></a>

This solution includes support for the AWS Elemental Link device as a source for live streaming content. AWS Elemental Link offers a configuration-free, cost-efficient way to securely and reliably transfer video to MediaLive. For more details on the device, refer to the [AWS Elemental Link product page](https://aws.amazon.com/medialive/features/link/).

To configure this solution to use an AWS Elemental Link device you need the following:
+ A Link device powered on and connected to the internet.
+ The Link device ID. To find the device ID, sign in to the [AWS Elemental MediaLive console](https://console.aws.amazon.com/medialive/) and navigate to **MediaLive Devices** in the AWS Region where your device is registered. The device is listed with the Link device ID.

  Launch the solution in the same Region as the Link device with the following parameters:
+  **Source Input Type** - INPUT\_DEVICE
+  **AWS Elemental Link Input Device ID** - The ID of the Link device from the MediaLive console. You can only attach a Link device to one input at a time. If the Link device is already attached to an input, you cannot create a new input using that device.
+  **Encoding Profile** - Select the profile that best matches your source resolution.
+  **Start MediaLive Channel** - If your device is ready to stream, select true. Otherwise, select false—​you can start the MediaLive channel through the MediaLive console when you’re ready to stream.

**Note**
For a full list of input types and configuration details, refer to [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) in the *AWS Elemental MediaLive User Guide*.

 **AWS Elemental Link input configuration**

![link input config](http://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/images/link-input-config.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
