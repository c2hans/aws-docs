---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/channel-security-groups-setup.html
---

# Setting up a channel security group
<a name="channel-security-groups-setup"></a>

To use a channel security group, you must first have an input security group with the appropriate CIDR allow list rules. Then you can attach that input security group to your channel as a channel security group.

**Note**
The information in this section assumes that you are familiar with the general steps for [creating a channel](creating-channel-scratch.md) and with [working with input security groups](working-with-input-security-groups.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
