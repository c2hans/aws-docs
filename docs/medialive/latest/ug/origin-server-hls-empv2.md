---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/origin-server-hls-empv2.html
---

# HLS output group to MediaPackage v2
<a name="origin-server-hls-empv2"></a>

Follow this procedure if you [determined](delivering-to-mediapackage.md) that you will create an HLS output group, and will send to MediaPackage v2. You and the operator of the downstream system must agree about the destination for the output of the HLS output group.

**To arrange setup of the destination**

1. Ask the MediaPackage user to create one channel on MediaPackage. Even if the MediaLive channel is a [standard channel](plan-redundancy.md) (with two pipelines), you need only one MediaPackage channel.

1. Obtain the two URLs (input endpoints is the MediaPackage terminology) for the channel. The two URLs for a channel look like this:

    `https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index`

    `https://mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index`

   The two URLs are slightly different, as shown in the examples above.

   Make sure that you obtain the URLs (which start with `https://`), not the channel name (which starts with `arn`).

   Note that you don't use user credentials in order to send to MediaPackage v2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
