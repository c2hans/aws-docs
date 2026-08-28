---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-auto-minor-version-upgrade-check.html
---

# elasticache-auto-minor-version-upgrade-check
<a name="elasticache-auto-minor-version-upgrade-check"></a>

Checks if Amazon ElastiCache clusters have auto minor version upgrades enabled. The rule is NON\_COMPLIANT for an ElastiCache cluster if it is using the Redis or Valkey engine and 'AutoMinorVersionUpgrade' is not set to 'true'.

**Identifier:** ELASTICACHE\_AUTO\_MINOR\_VERSION\_UPGRADE\_CHECK

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (UAE), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d739c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
