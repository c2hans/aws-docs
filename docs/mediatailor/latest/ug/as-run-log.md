---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/as-run-log.html
---

# "As Run" log for AWS Elemental MediaTailor Channel Assembly
<a name="as-run-log"></a>

The *As Run* log, in the CloudWatch `MediaTailor/Channel/AsRunLog` log group, shows information about programs and ad breaks as they play.

When you create a channel, the As Run log is disabled by default. Using the Console or the AWS Command Line Interface (AWS CLI), you can enable and disable the As Run log state for each channel in your account.

When you enable the As Run log, MediaTailor automatically creates a service-linked role that allows MediaTailor to write and manage the As Run log in your CloudWatch Logs account. For more information about service-linked roles, see [Using service-linked roles for MediaTailor](using-service-linked-roles.md).

**Note**
The As Run Log currently only supports the default program. For now it doesn't support the alternateMedia created by program rules. This means that it currently does not generate the As Run Log for alternateMedia.

**Topics**
+ [Enabling the As Run log](enabling-as-run-log.md)
+ [Disabling the As Run log](disabling-as-run-log.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
