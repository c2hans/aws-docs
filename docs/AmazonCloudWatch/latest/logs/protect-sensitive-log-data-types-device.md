---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types-device.html
---

# Device identifiers
<a name="protect-sensitive-log-data-types-device"></a>

CloudWatch Logs data protection can find the following types of device identifiers.

| Type of data | Data identifier ID | Keyword required | Countries and regions |
| --- | --- | --- | --- |
| IP address | `IpAddress` | None | All |

## Data identifier ARNs for device data types
<a name="cwl-data-protection-devices-arns"></a>

The following lists the Amazon Resource Names (ARNs) for the data identifiers that you can add to your data protection policies.

| Device data identifier ARN |
| --- |
| arn:aws:dataprotection::aws:data-identifier/IpAddress |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
