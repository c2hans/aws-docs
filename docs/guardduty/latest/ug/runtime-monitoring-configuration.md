---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-configuration.html
---

# Enabling GuardDuty Runtime Monitoring
<a name="runtime-monitoring-configuration"></a>

Before enabling Runtime Monitoring in your account, make sure that the resource type for which you want to monitor the runtime events, supports the platforms requirements. For more information, see [Prerequisites](runtime-monitoring-prerequisites.md).

If you have been using EKS Runtime Monitoring prior to the launch of Runtime Monitoring, you can use the APIs to check and update the existing configuration for EKS Runtime Monitoring. You can also migrate your existing configuration from EKS Runtime Monitoring to Runtime Monitoring. For more information, see [Migrating from EKS Runtime Monitoring to Runtime Monitoring](migrating-from-eksrunmon-to-runtime-monitoring.md).

**Note**
Presently, this documentation provides steps to enable Runtime Monitoring for your accounts and organization by console only. You can also enable Runtime Monitoring by using [API Actions](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Operations.html) or [AWS CLI for GuardDuty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty).

You can configure Runtime Monitoring by using the steps in the following topics.

**Topics**
+ [Enabling Runtime Monitoring for multiple-account environments](enable-runtime-monitoring-multiple-acc-env.md)
+ [Enabling Runtime Monitoring for a standalone account](enable-runtime-monitoring-standalone-acc.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
