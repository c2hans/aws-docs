---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/event-data-store-cmk-encryption-enabled.html
---

# event-data-store-cmk-encryption-enabled
<a name="event-data-store-cmk-encryption-enabled"></a>

Checks if AWS Cloud Trail event data stores have customer managed AWS KMS keys enabled. The rule is NON\_COMPLIANT if an event data store has disabled customer managed KMS keys. Optionally, you can specify a list of KMS keys for the rule to check.

**Identifier:** EVENT\_DATA\_STORE\_CMK\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::CloudTrail::EventDataStore

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV
Comma-separated list of Amazon Resource Names (ARNs) of AWS KMS keys for the rule to check. If provided, the rule is NON\_COMPLIANT if an AWS Cloud Trail event data store is not encrypted with one of these KMS keys.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d821c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
