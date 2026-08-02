---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/rtmp-push-and-rtp-push-input-configuration.html
---

# RTMP Push and RTP Push input configuration
<a name="rtmp-push-and-rtp-push-input-configuration"></a>

RTP and RTMP Push provide the option to push a transport stream (TS) MediaLive. In both options, the following parameters are required to configure the solution:
+  **Source Input Type** - RTP\_PUSH / RTMP\_PUSH
+  **Input Security Group CIDR Block** - A valid CIDR block used to create a security group to restrict access to the MediaLive input.
+  **Encoding Profile** - Select the profile that best matches your source resolution.
+  **Start MediaLive Channel** - If your device is ready to stream, select true. Otherwise, select false—​you can start the MediaLive channel through the AWS console when you’re ready to stream.

**Note**
Refer to the [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) topic in the *AWS Elemental MediaLive User Guide* for a full list of input types and configuration details.

 **RTMP Push and RTP Push input configuration**

![rtmp rtp input config](http://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/images/rtmp-rtp-input-config.png)
