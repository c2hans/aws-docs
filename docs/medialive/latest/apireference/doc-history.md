---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/doc-history.html
---

# Document History
<a name="doc-history"></a>

The following table describes the main changes to this documentation.
+ **API version: latest**

| Change | Description | Date |
| --- | --- | --- |
| Workflow monitor | Workflow monitor features have been added to the API. Workflow monitor is a tool to analyze AWS media services and create signal maps, visualizations of the media workflow, between those services. Use the signal maps to generate monitoring alarms and notifications using CloudWatch, EventBridge, and CloudFormation. | April 11, 2024 |
| Features added since November, 2021 | Documentation for features added from November 2021 to July 2022, including:+  AWS Elemental Link remote reboots and remote software updates <br />+  Reservation automatic renewal <br />+  SCTE-35 input PID selection <br />+  PDT clock source selector for HLS outputs <br />+  Accessibility captions for HLS and MediaPackage outputs  | July 19, 2022 |
| Features added since April, 2021 | Documentation for features added from April 2021 to November 2021, including:+  Transport Stream (TS) file inputs <br />+  Nielsen watermarks <br />+  Support for font styles with WebVTT captions <br />+  WebVTT output captions <br />+  Amazon CloudWatch metrics <br />+  Pipeline locking with UDP outputs <br />+  Trick-play in MediaPackage output group  | November 5, 2021 |
| Features added since December, 2020 | Documentation for features added from December 2020 to April 2021, including:+  Delivery via your VPC <br />+  Captions in CDI inputs <br />+  Clipping a file input that is stored on an HTTP server <br />+  Trick-play in HLS outputs (according to the Image media playlist specification) <br />+  Automatic input failover with CDI inputs <br />+  Support for transferring AWS Elemental Link devices between Regions <br />+  Support for ACLs when delivering outputs to Amazon S3 <br />+  Support for motion graphics overlays via the channel schedule <br />+  Font styling on TTML output captions  | May 3, 2020 |
| Features added since August, 2020 | Documentation for features added since August, 2020, including:+  Batch operations for the channel <br />+  Operations to handle transfers of AWS Elemental Link devices <br />+  Operations for input thumbnails.  | December 28, 2020 |
| Rewrite of resources. | The descriptions of many of the elements in the resources other than Channel have been revised. | August 26, 2020 |
| Rewrite of Channels and Channels (ID) resources. | The descriptions of many of the elements in these two resources have been revised. | August 20, 2020 |
| Features added since September, 2019 | Documentation for features added since September, 2019, including:+  EBU-TT-D captions in a captions output <br />+  AWS Elemental Devices and the AWS Elemental Link hardware device <br />+  Multiplex <br />+  Automatic input failover <br />+  Input prepare action in the schedule <br />+  Immediate mode for all actions in the schedule <br />+  Follow mode for SCTE-35 actions in the schedule <br />+  Enhanced VQ mode <br />+  ID3 segment tagging <br />+  Nielsen watermarks  | August 10, 2020 |
| Changes to support the H.265 (HEVC) codec | Documentation for configuring H.265 in Channels | September 12, 2019 |
| Changes to support SDR and HDR color space handling | Documentation for handling color space in the input, in VideoSelector in Channels<br />Documentation for handling color space in the output, in H264ColorMetadata, H264ColorSpaceSettings, H265ColorMetadata and H265ColorSpaceSettings in Channels | September 12, 2019 |
| Changes to support input clipping when switching inputs, in the channel schedule | Documentation for InputClippingSettings in Channels channelId Schedule | July 25, 2019 |
| Changes to support switching inputs immediately, in the channel schedule | Documentation for urlPath in InputSwitchScheduleActionSettings in Channels channelId Schedule | July 25, 2019 |
| Changes to support dynamic inputs in the channel schedule | Documentation for urlPath in InputSwitchScheduleActionSettings in Channels channelId Schedule | July 25, 2019 |
| UpdateChannelClass operation in the channel, and more | Documentation for the UpdateChannelClass operation in the channel<br />Documentation for the MediaPackage output group type<br />Documentation for pausing and unpausing a channel using the channel schedule<br />Documentation for the RTP push input and RTMP push input connected to an upstream system that is in your Amazon VPC<br />Documentation for tagging using MediaLive<br />Documentation for the frame capture output group | May 2, 2019 |
| Integration with AWS Elemental MediaConnect, and more | Documentation for the MediaConnect input type in the Channel resourceDocumentation for Input switching using the channel schedule<br />Documentation for Schedule feature in the Channel resource<br />Documentation for Reservations resource<br />Documentation for the RTMP output type in the Channel resource | December 7, 2018 |
| New AWS Elemental MediaLive service release | Initial documentation for the MediaLive service. | November 27, 2017 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
