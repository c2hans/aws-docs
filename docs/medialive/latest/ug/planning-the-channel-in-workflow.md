---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/planning-the-channel-in-workflow.html
---

# Planning the outputs in the channel
<a name="planning-the-channel-in-workflow"></a>

You should plan the AWS Elemental MediaLive channel as the second stage of planning a transcoding *workflow*. You should have already performed the first stage of setting up the upstream and downstream systems, as described in [Preparing the upstream and downstream systems in a workflow](container-planning-uss-dss.md).

The channel provides the ability to configure for different characteristics of the outputs, and for including a wide array of video features. But before you plan these details, you should plan the basic features for the channel.

**Note**
On the output side, we refer to each video or audio or caption stream, track, or program as an *encode*.

**Topics**
+ [Identify the output encodes](planning-encodes.md)
+ [Map the output encodes to the sources](channel-map-output-source.md)
+ [Design the encodes](designing-encodes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
