---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-attach.html
---

# Step 2: Attach the channel security group to the channel
<a name="channel-security-groups-attach"></a>

When you create a channel with SRT outputs in listener mode, you must attach a channel security group.

1. On the **Create channel** page, choose **Channel and input details** in the navigation pane.

1. In the **General settings** section, find the **Channel security groups** field.

1. From the dropdown list, select the input security group that you want to use as the channel security group.

   The dropdown list shows all input security groups in your account, identified by their ID and any tags.

1. Continue creating the channel, including configuring your SRT outputs in listener mode. For information about creating SRT outputs, see [Creating an SRT output group](opg-srt.md).

**Result**

When you create the channel, MediaLive retrieves the CIDR rules from the input security group and applies them to control access to the channel's outputs. Downstream systems with IP addresses in the allow list can now connect to the SRT listener endpoints on your channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
