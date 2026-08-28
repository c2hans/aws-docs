---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/srt-listener-validation.html
---

# Validation rules for listener mode
<a name="srt-listener-validation"></a>

MediaLive enforces the following validation rules when you create or update SRT outputs in listener mode:
+ **Channel security group required (Public delivery method only)**: For channels using the Public delivery method, if the channel includes at least one SRT output configured in listener mode, you must attach a channel security group to the channel. If you attempt to create or start a channel using Public delivery with SRT outputs in listener mode but no channel security group, MediaLive returns an error. For channels using VPC delivery or MediaLive Anywhere channels, the channel security group is not required; you must configure your network to allow SRT connections from the caller destination.
+ **Port uniqueness**: Within a single channel, each SRT output in listener mode must use a unique port number. If you attempt to create two outputs with the same port, MediaLive returns an error.
+ **Listener port range**: The port number must be in the range 5000 to 5200 inclusive.
+ **Cannot remove channel security group**: If the channel has SRT outputs in listener mode, you cannot remove the channel security group. You must first remove all SRT outputs configured in listener mode, or change them to caller mode.
+ **Cannot change mode on running channel**: You cannot change an output's connection mode (from caller to listener or vice versa) while the channel is running. You must stop the channel first.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
