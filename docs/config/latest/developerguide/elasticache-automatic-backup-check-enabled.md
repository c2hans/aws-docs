---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-automatic-backup-check-enabled.html
---

# elasticache-automatic-backup-check-enabled
<a name="elasticache-automatic-backup-check-enabled"></a>

Checks if Amazon ElastiCache clusters (Valkey or Redis OSS) have automatic backup turned on. The rule is NON\_COMPLIANT if automated backup is not enabled or the SnapshotRetentionLimit for a cluster is less than the specified `snapshotRetentionPeriod`.

**Identifier:** ELASTICACHE\_AUTOMATIC\_BACKUP\_CHECK\_ENABLED

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

snapshotRetentionPeriod (Optional)Type: int
Minimum snapshot retention period in days for Valkey or Redis OSS. Valid values are 1 to 35. Default value is 1.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d737c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
