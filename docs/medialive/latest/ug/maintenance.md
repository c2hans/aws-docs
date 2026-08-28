---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/maintenance.html
---

# Managing channel maintenance
<a name="maintenance"></a>

The AWS Elemental MediaLive service routinely performs maintenance on underlying systems for security, reliability, and operational performance. The maintenance activities include actions such as patching the operating system, updating drivers, or installing software and patches.

Maintenance is performed individually on each channel, as it is required.

You can't disable channel maintenance. But you can control when the maintenance occurs.

The routine for maintenance is the following:
+ When you create a channel, MediaLive automatically assigns an arbitrary maintenance window: a particular day of the week and a two-hour window. For example, Thursdays from 4:00 to 5:00 UTC.
+ When a channel needs maintenance, you receive notification in the Health Dashboard and by email. For more information, see [Managing maintenance notifications](maintenance-setup-notifications.md).
+ When you receive a notification, you should decide if you want to adjust the timing of the maintenance. There are several ways to adjust the timing. See [Options for handling maintenance](setting-maintenance.md#set-maintenance-change-options).

**Topics**
+ [Viewing maintenance information](viewing-maintenance.md)
+ [Managing maintenance notifications](maintenance-setup-notifications.md)
+ [Working with a maintenance event](setting-maintenance.md)
+ [Changing the maintenance window](set-maintenance-change-steps.md)
+ [How MediaLive performs channel maintenance](maintenance-how.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
