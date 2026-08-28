---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-backup-enabled.html
---

# redshift-backup-enabled
<a name="redshift-backup-enabled"></a>

Checks that Amazon Redshift automated snapshots are enabled for clusters. The rule is NON\_COMPLIANT if the value for `automatedSnapshotRetentionPeriod` is greater than `MaxRetentionPeriod` or less than `MinRetentionPeriod` or the value is 0.

**Identifier:** REDSHIFT\_BACKUP\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

MinRetentionPeriod (Optional)Type: int
Minimum value for the retention period. Minimum value is 1.

MaxRetentionPeriod (Optional)Type: int
Maximum value for the retention period. Maximum value is 35.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1293c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
