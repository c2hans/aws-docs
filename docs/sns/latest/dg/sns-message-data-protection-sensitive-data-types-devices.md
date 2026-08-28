---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-sensitive-data-types-devices.html
---

# Amazon SNS sensitive data types: Devices
<a name="sns-message-data-protection-sensitive-data-types-devices"></a>

The following table lists and describes the types of device identifiers that Amazon SNS can detect using managed data identifiers.

| Detection type | Managed data identifier ID | Keyword required | Countries and regions |
| --- | --- | --- | --- |
| IP Address | IpAddress | No | Any |

## Data identifier ARNs for device data types
<a name="sns-message-data-protection-devices-arns"></a>

The following lists the Amazon Resource Names (ARNs) for the data identifiers that you can add to your data protection policies.

| Device data identifier ARN |
| --- |
| arn:aws:dataprotection::aws:data-identifier/IpAddress |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
