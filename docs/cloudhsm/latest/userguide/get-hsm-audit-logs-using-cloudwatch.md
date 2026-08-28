---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-hsm-audit-logs-using-cloudwatch.html
---

# Working with Amazon CloudWatch Logs and AWS CloudHSM Audit Logs
<a name="get-hsm-audit-logs-using-cloudwatch"></a>

When an HSM in your account receives a command from the AWS CloudHSM [command line tools](command-line-tools.md) or [software libraries](use-hsm.md), it records its execution of the command in audit log form. The HSM audit logs include all client-initiated [management commands](cloudhsm-audit-log-reference.md), including those that create and delete the HSM, log into and out of the HSM, and manage users and keys. These logs provide a reliable record of actions that have changed the state of the HSM.

AWS CloudHSM collects your HSM audit logs and sends them to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) on your behalf. You can use the features of CloudWatch Logs to manage your AWS CloudHSM Audit Logs, including searching and filtering the logs and exporting log data to Amazon S3. You can work with your HSM audit logs in the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/) or use the CloudWatch Logs commands in the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/logs/index.html) and [CloudWatch Logs SDKs](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/).

**Topics**
+ [How HSM audit logging works](get-audit-logs-from-cloudwatch.md)
+ [Viewing AWS CloudHSM audit logs in CloudWatch Logs](understand-audit-logs.md)
+ [Interpreting AWS CloudHSM audit logs](interpreting-audit-logs.md)
+ [AWS CloudHSM audit log reference](cloudhsm-audit-log-reference.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
