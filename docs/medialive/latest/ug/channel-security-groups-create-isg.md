---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-create-isg.html
---

# Step 1: Create or identify an input security group
<a name="channel-security-groups-create-isg"></a>

Before you create the channel, you must have an input security group that contains the CIDR allow list rules for the downstream systems that will connect to your SRT outputs configured in listener mode.

1. Identify the IP addresses of the downstream systems (SRT callers) that will connect to your MediaLive channel. These are the systems that will initiate connections to MediaLive.

1. If you don't already have an input security group with these IP addresses, create one. For instructions, see [Creating an input security group](create-input-security-groups.md).

   If you already have an input security group with the appropriate CIDR rules, you can reuse it. The same input security group can be used for both input security and channel security.

1. Make a note of the input security group ID. You will need this when you create the channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
