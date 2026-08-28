---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-how-it-works.html
---

# How channel security groups work
<a name="channel-security-groups-how-it-works"></a>

When you attach a channel security group to a channel, MediaLive performs the following actions:

1. MediaLive retrieves the CIDR allow list rules from the input security group that you selected.

1. MediaLive creates or updates security group rules to control access to the channel's outputs.

1. These rules allow inbound traffic from the specified CIDR blocks to the ports configured in your SRT outputs that are in listener mode.

**Relationship to input security groups**

Channel security groups and input security groups serve similar purposes but apply to different parts of the channel:
+ **Input security groups** – Control inbound traffic to channel inputs. They define which upstream systems can push content to MediaLive.
+ **Channel security groups** – Control inbound traffic to channel outputs. They define which downstream systems can connect to MediaLive to pull content.

Both use the same underlying mechanism: CIDR allow lists stored in input security groups. This design allows you to reuse existing input security groups for channel security, simplifying management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
