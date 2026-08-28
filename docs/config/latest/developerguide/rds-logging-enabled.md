---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-logging-enabled.html
---

# rds-logging-enabled
<a name="rds-logging-enabled"></a>

Checks if respective logs of Amazon Relational Database Service (Amazon RDS) are enabled. The rule is NON\_COMPLIANT if any log types are not enabled.

**Note**
DB Instances that are not in 'available', 'backing-up', 'storage-optimization', or 'storage-full' status evaluate as `NOT_APPLICABLE`.

**Identifier:** RDS\_LOGGING\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

additionalLogs (Optional)Type: StringMap
Comma-separated list of engine names and log type names. For example, "additionalLogs": "oracle: general, slowquery ; aurora: alert, slowquery"

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1257c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
