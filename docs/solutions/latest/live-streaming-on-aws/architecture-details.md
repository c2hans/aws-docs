---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

Live Streaming on AWS solution architecture details

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

<a name="aws-services-in-this-solution"></a>== AWS services in this solution

| AWS service | Description |
| --- | --- |
|  [Amazon Elemental MediaLive](https://aws.amazon.com/medialive/)  |  **Core.** It ingests two input feeds and transcodes your content into two adaptive bitrate (ABR) HTTP Live Streaming (HLS) streams as outputs. |
|  [Amazon Elemental Mediapackage](https://aws.amazon.com/mediapackage/)  |  **Core.** It ingests the MediaLive ABR output and packages the live stream into HLS, Dynamic Adaptive Streaming over HTTP (DASH), and Common Media Application Format (CMAF) formats that are delivered to three MediaPackage custom endpoints. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core.** It uses the MediaPackage custom endpoints and its origin and includes a CDN identifier custom HTTP header to authenticate requests. |
|  [Amazon Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  **Core.** It stores securely the CDN identifier from Amazon CloudFront. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core.** It stores a demo HTML preview player to help you test the solution. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Provides application-level resource monitoring and visualization of resource operations and cost data. |

<a name="html-preview-player"></a>== HTML preview player

A demo HTML preview player is available to help you test the solution. The player is a static website hosted in an Amazon S3 bucket. It is pre-populated with the URLs that point to the newly created customer stream. The HTML/JavaScript application plays back the HLS, DASH, MSS, and CMAF streams. In addition, the solution can be configured to ingest a Demo HLS feed hosted on AWS. Customize the HTML in the `DemoBucket` S3 bucket to suit your needs. For details about putting the HLS video into a webpage, refer to the [Apache 2.0 Video.JS](https://videojs.github.io/videojs-contrib-hls/) open-source project.

To check output on the player, start the AWS Elemental MediaLive channel. Even if you selected `no` for the **Start MediaLive Channel** CloudFormation template parameter, you can go to the [MediaLive](https://console.aws.amazon.com/medialive/) channel to start the player when you are ready to start testing.

<a name="url-pull-input-configuration"></a>== URL\_PULL (HLS) input configuration

 `URL_PULL` provides the option to ingest an HTTP live streaming (HLS) stream over HTTP or HTTPS. The following parameters are required to configure the solution to ingest an HLS stream:

 **Source Input Type** - `URL_PULL`.

 **Primary Source URL** - The HTTP(s) link to the HLS stream manifest file. The default value is a demo stream from AWS.

 **Primary Source Username** - Only required if you have basic authentication setup on your source HLS stream.

 **Primary Source Password** - Only required if you have basic authentication setup on your source HLS stream.

 **Secondary Source URL** - The HTTP(s) link to the HLS stream manifest file. The default value is a demo stream from AWS.

 **Secondary Source Username** - Only required if you have basic authentication setup on your source HLS stream.

 **Secondary Source Password** - Only required if you have basic authentication setup on your source HLS stream.

 **Encoding Profile** - Select the profile that best matches your source resolution.

 **Start MediaLive Channel** - If your device is ready to stream, select `yes`. Otherwise, select `no` — you can start the AWS Elemental MediaLive channel through the AWS Management Console when you’re ready to stream.

**Note**
For a full list of input types and configuration details, refer to the [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) topic in the *AWS Elemental MediaLive User Guide*.

<a name="rtmp-pull-input-configuration"></a>== RTMP\_PULL input configuration

 `RTMP_PULL` provides the option to ingest an RTMP stream. The following parameters are required to configure the solution to ingest an RTMP stream:

 **Source Input Type** - `RTMP_PULL`.

 **Primary Source URL** - The RTMP link to the primary source stream, for example `rtmp://203.0.113.20:1935/primary`.

 **Primary Source Username** - Only required if you have basic authentication setup on your source stream.

 **Primary Source Password** - Only required if you have basic authentication setup on your source stream.

 **Secondary Source URL** - The RTMP link to the primary source stream, for example `rtmp://203.0.113.20:1935/secondary`.

 **Secondary Source Username** - Only required if you have basic authentication setup on your source stream.

 **Secondary Source Password** - Only required if you have basic authentication setup on your source stream.

 **Encoding Profile** - Select the profile that best matches your source resolution.

 **Start MediaLive Channel** - If your device is ready to stream, select `yes`. Otherwise, select `no` — you can start the AWS Elemental MediaLive channel through the AWS Management Console when you’re ready to stream.

**Note**
For a full list of input types and configuration details, refer to the [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) topic in the *AWS Elemental MediaLive User Guide*.

<a name="rtmp-push-rtp-push-input-configuration"></a>== RTMP\_PUSH and RTP\_PUSH input configuration

 `RTMP_PUSH` and `RTP_PUSH` provide the option to push a transport stream (TS) to AWS Elemental MediaLive. In both options, the following parameters are required to configure the solution:

 **Source Input Type** - `RTP_PUSH` or `RTMP_PUSH`

 **Input Security Group CIDR Block** - A valid CIDR block used to create a security group to restrict access to the MediaLive input.

 **Encoding Profile** - Select the profile that best matches your source resolution.

 **Start MediaLive Channel** - If your device is ready to stream, select `yes`. Otherwise, select `no` — you can start the MediaLive channel through the AWS Management Console when you’re ready to stream.

**Note**
For a full list of input types and configuration details, refer to the [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) topic in the *AWS Elemental MediaLive User Guide*.

<a name="mediaconnect-input-configuration"></a>== MEDIACONNECT input configuration

 `MEDIACONNECT` provides the option to ingest a stream from Elemental MediaConnect. The following parameters are required to configure the solution to ingest from MediaConnect:

 **Source Input Type** - `MEDIACONNECT`.

 **Primary MediaConnect ARN** - The ARN of the primary source stream, for example: `arn:aws:mediaconnect:uswest1:111122223333:flow:1bgf67:primary`. This MediaConnect flow must be in a different Availability Zone as the secondary stream.

 **Secondary MediaConnect ARN** - The ARN of the secondary source stream, for example: `arn:aws:mediaconnect:uswest1:111122223333:flow:1bgf67:secondary`. This MediaConnect flow must be in a different Availability Zone as the primary stream.

 **Encoding Profile** - Select the profile that best matches your source resolution.

 **Start MediaLive Channel** - If your device is ready to stream, select `yes`. Otherwise, select `no` — you can start the AWS Elemental MediaLive channel through the AWS Management Console when you’re ready to stream.

**Note**
For a full list of input types and configuration details, refer to the [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) topic in the *AWS Elemental MediaLive User Guide*.
