---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-supported-engine-version.html
---

# elasticache-supported-engine-version
<a name="elasticache-supported-engine-version"></a>

Checks if ElastiCache clusters are running a version greater or equal to the recommended engine version. The rule is NON\_COMPLIANT if the 'EngineVersion' for an ElastiCache cluster is less than the specified recommended version for its given engine.

**Identifier:** ELASTICACHE\_SUPPORTED\_ENGINE\_VERSION

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

latestMemcachedVersionType: String
The latest recommended engine version for Memcached. Valid values are in semantic versioning (SemVer) format with 3-component number for major, minor, and patch versions (for example, 1.6.6, not 1.6).

latestRedisVersionType: String
The latest recommended engine version for Redis. Valid values are in semantic versioning (SemVer) format with 3-component number for major, minor, and patch versions (for example, 7.0.5, not 7.0).

## AWS CloudFormation template
<a name="w2aac20c16c17b7d755c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
