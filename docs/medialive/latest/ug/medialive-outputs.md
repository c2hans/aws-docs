---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/medialive-outputs.html
---

# Setup: Creating output groups and outputs
<a name="medialive-outputs"></a>

This section describes how to plan and create output groups and outputs in an AWS Elemental MediaLive.

You create output groups and outputs when you [create or edit a channel](creating-channel-scratch.md). When you create a channel, you must create at least one output group. After you have created the channel, you can edit it to add more output groups.

On the console, you create output groups on the **Outputs** section of the **Channel** page. You can't create the output groups and outputs separately from the channel that they belong to.

**Topics**
+ [Creating an Archive output group](opg-archive.md)
+ [Creating a CMAF Ingest output group](opg-cmafi.md)
+ [Creating a Frame capture output group](opg-framecapture.md)
+ [Creating an HLS output group](opg-hls.md)
+ [Creating a MediaConnect Router output group](opg-mediaconnect-router.md)
+ [Creating a MediaPackage output group](opg-mediapackage.md)
+ [Creating a Microsoft Smooth output group](opg-mss.md)
+ [Creating an RTMP output group](opg-rtmp.md)
+ [Creating an SRT output group](opg-srt.md)
+ [Creating a UDP output group](opg-udp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
