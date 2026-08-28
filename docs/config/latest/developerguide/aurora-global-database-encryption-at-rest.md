---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/aurora-global-database-encryption-at-rest.html
---

# aurora-global-database-encryption-at-rest
<a name="aurora-global-database-encryption-at-rest"></a>

Checks if Amazon Aurora Global Databases have storage encryption enabled. This rule is NON\_COMPLIANT if an Amazon Aurora Global Database does not have storage encryption enabled.

**Identifier:** AURORA\_GLOBAL\_DATABASE\_ENCRYPTION\_AT\_REST

**Resource Types:** AWS::RDS::GlobalCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d217c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
