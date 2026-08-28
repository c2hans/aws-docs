---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/setup-rtmp-push-obtain-info.html
---

# Obtain information
<a name="setup-rtmp-push-obtain-info"></a>

Obtain the following information from your contact person at the upstream system:
+ The application name and application instance for the source content. (The application instance is also known as the *stream* or *stream key*.) There are two sources for a standard-class input, or one source for a single-class input. For information about input classes and their uses, see [Choosing the channel class and input class](class-channel-input.md). For information about input classes and their uses, see [Choosing the channel class and input class](class-channel-input.md).

  The operator of the upstream system might already have rules for assigning these names. If not, you might have names that you would like to use. Make sure that you and the operator of the upstream system are clear about these names.

  In this example, the application name and instance name are identical. But they could be different:

  Application name: `live`, and instance name `curling`

  Application name: `live`, and instance name `curling`
+ The public network IP addresses. These are the sets of IP addresses where the source or sources for the content will appear on the public network. You need this information to create the input security group.

  For example:
  + For one source: `203.0.113.19, 203.0.113.58, 203.0.113.25`
  + For the other source: `198.51.100.19, 198.51.100.59, 198.51.100.21`

  These addresses are the addresses shown in the red boxes in [the diagram after this procedure](setup-result-rtmp-push.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
