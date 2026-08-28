---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/aurora-mysql-backtracking-enabled.html
---

# aurora-mysql-backtracking-enabled
<a name="aurora-mysql-backtracking-enabled"></a>

Checks if an Amazon Aurora MySQL cluster has backtracking enabled. The rule is NON\_COMPLIANT if the Aurora cluster uses MySQL and it does not have backtracking enabled.

**Identifier:** AURORA\_MYSQL\_BACKTRACKING\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain) Region

**Parameters:**

BacktrackWindowInHours (Optional)Type: double
Amount of time in hours (up to 72) to backtrack your Aurora MySQL cluster.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d223c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
