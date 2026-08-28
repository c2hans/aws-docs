---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-use-cases.html
---

# When to use channel security groups
<a name="channel-security-groups-use-cases"></a>

Channel security groups are required in the following situations:
+ **SRT outputs in listener mode** – When you configure an SRT output in listener mode, you must attach a channel security group to the channel. The channel security group defines which downstream systems (SRT callers) are allowed to connect to the MediaLive listener endpoint.

Channel security groups are not used in the following situations:
+ **SRT caller outputs** – When MediaLive acts as the caller (initiating connections to downstream listeners), no channel security group is needed because MediaLive is making outbound connections.
+ **Other output types** – Channel security groups are not applicable to other output types such as HLS, MediaPackage, Archive, or UDP outputs.
+ **MediaLive Anywhere channels** – Channel security groups cannot be used with AWS Elemental MediaLive Anywhere channels. MediaLive Anywhere channels use different security mechanisms.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
