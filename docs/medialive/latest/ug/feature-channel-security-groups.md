---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/feature-channel-security-groups.html
---

# Using channel security groups
<a name="feature-channel-security-groups"></a>

You can configure a MediaLive channel to use a channel security group. A channel security group controls inbound traffic associated with the channel's outputs. This feature enables pull-style outputs, where downstream systems initiate connections to MediaLive.

Channel security groups are required when you configure SRT outputs in listener mode. In listener mode, MediaLive acts as the server, listening on a local socket for external systems to establish connections.

**Topics**
+ [About channel security groups](channel-security-groups-about.md)
+ [When to use channel security groups](channel-security-groups-use-cases.md)
+ [How channel security groups work](channel-security-groups-how-it-works.md)
+ [Rules and constraints](channel-security-groups-rules.md)
+ [Setting up a channel security group](channel-security-groups-setup.md)
+ [Managing channel security groups](channel-security-groups-manage.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
