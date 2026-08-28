---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/docdb-cluster-backup-retention-check.html
---

# docdb-cluster-backup-retention-check
<a name="docdb-cluster-backup-retention-check"></a>

Checks if an Amazon Document DB cluster retention period is set to specific number of days. The rule is NON\_COMPLIANT if the retention period is less than the value specified by the parameter.

**Identifier:** DOCDB\_CLUSTER\_BACKUP\_RETENTION\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

minimumBackupRetentionPeriod (Optional)Type: int
Minimum days backups should be kept. Valid values 1 to 35, default value is 7. This rule is NON\_COMPLIANT if value is greater than 'backupRetentionPeriod'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d487c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
