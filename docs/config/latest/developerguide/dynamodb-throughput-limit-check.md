---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-throughput-limit-check.html
---

# dynamodb-throughput-limit-check
<a name="dynamodb-throughput-limit-check"></a>

Checks if provisioned DynamoDB throughput is approaching the maximum limit for your account. By default, the rule checks if provisioned throughput exceeds a threshold of 80 percent of your account limits.

**Identifier:** DYNAMODB\_THROUGHPUT\_LIMIT\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

accountRCUThresholdPercentage (Optional)Type: intDefault: 80
Percentage of provisioned read capacity units for your account. When this value is reached, the rule is marked as noncompliant.

accountWCUThresholdPercentage (Optional)Type: intDefault: 80
Percentage of provisioned write capacity units for your account. When this value is reached, the rule is marked as noncompliant.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d515c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
