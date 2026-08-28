---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-log-mon.html
---

# Security event logging and monitoring in Accelerate
<a name="acc-sec-log-mon"></a>

Accounts enrolled in AMS Accelerate are configured with a baseline deployment of CloudWatch [Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) and [Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) that have been optimized to reduce noise and to identify indications of a true incident. AMS Accelerate also employs GuardDuty for account monitoring. For more information, see [Monitor with GuardDuty](acc-sec-data-protect.md#acc-sec-data-protect-gd).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
