---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.html
---

# elasticache-redis-cluster-automatic-backup-check
<a name="elasticache-redis-cluster-automatic-backup-check"></a>

Check if the Amazon ElastiCache Redis clusters have automatic backup turned on. The rule is NON\_COMPLIANT if the SnapshotRetentionLimit for Redis cluster is less than the SnapshotRetentionPeriod parameter. For example: If the parameter is 15 then the rule is non-compliant if the snapshotRetentionPeriod is between 0-15.

**Identifier:** ELASTICACHE\_REDIS\_CLUSTER\_AUTOMATIC\_BACKUP\_CHECK

**Resource Types:** AWS::ElastiCache::CacheCluster, AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

snapshotRetentionPeriod (Optional)Type: intDefault: 15
Minimum snapshot retention period in days for Redis cluster. Default is 15 days.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d743c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
