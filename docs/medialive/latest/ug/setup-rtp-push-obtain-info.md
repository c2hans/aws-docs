---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-rtp-push-obtain-info.html
---

# Obtain information
<a name="setup-rtp-push-obtain-info"></a>

Obtain the following information from your contact person at the upstream system:
+ The public network IP addresses. You need two sets of IP addresses because an RTP input is always a [standard-class input](class-channel-input.md), even if your channel is a single-pipeline channel. For information about input classes, see [Choosing the channel class and input class](class-channel-input.md).

  These are the sets of IP addresses where the source or sources for the content will appear on the public network. You need this information to create the input security group.

  For example:
  + For one source: `203.0.113.19, 203.0.113.58, 203.0.113.25`
  + For the other source: `198.51.100.19, 198.51.100.59, 198.51.100.21`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
