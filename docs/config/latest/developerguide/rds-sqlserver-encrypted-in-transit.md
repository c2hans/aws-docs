---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-sqlserver-encrypted-in-transit.html
---

# rds-sqlserver-encrypted-in-transit
<a name="rds-sqlserver-encrypted-in-transit"></a>

Checks if connections to Amazon RDS SQL server database instances are configured to use encryption in transit. The rule is NON\_COMPLIANT if the DB parameter force\_ssl for the parameter group is not set to 1 or the ApplyStatus parameter is not 'in-sync'.

**Identifier:** RDS\_SQLSERVER\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1285c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
