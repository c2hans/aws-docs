---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-email-notification.html
---

# Requirements for CloudWatch and Amazon SNS—setting up email notification
<a name="requirements-for-email-notification"></a>

MediaLive provides information about channels as they are running. It sends this information to Amazon CloudWatch as events. The details of these events can optionally be distributed to one or more users. Someone must set up this distribution. (For the setup procedure, see [Monitoring a channel or multiplex using Amazon CloudWatch Events](monitoring-via-cloudwatch.md).)

You must decide if you want to give some or all of your users these permissions. You might choose to allow each user to perform their own distribution setup. Or you might decide that an administrator must be responsible for performing the setup at startup for applicable users, and then again whenever a new user is added.

The following table shows the actions in IAM that relate to access for setting up email notification.

| Permissions | Service Name in IAM | Actions |
| --- | --- | --- |
| Write  | CloudWatch Events | All actions |
| Write | SNS  | All actions |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
