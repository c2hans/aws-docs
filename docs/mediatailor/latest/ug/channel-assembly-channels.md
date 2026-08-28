---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html
---

# Working with channels
<a name="channel-assembly-channels"></a>

A channel assembles your source manifests into a linear stream. Each channel contains one or more outputs that correspond to your package configurations.

 First you create a channel, then you add your VOD sources and live sources to the channel's schedule by creating *programs*. Each program is associated with a VOD source or a live source.

**Topics**
+ [Create a channel using the MediaTailor console](channel-assembly-creating-channels.md)
+ [Using source groups with your channel's outputs](channel-assembly-source-groups.md)
+ [Delete a channel using the MediaTailor console](channel-assembly-starting-stopping-channels.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
