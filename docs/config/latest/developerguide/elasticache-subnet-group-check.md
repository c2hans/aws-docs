---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-subnet-group-check.html
---

# elasticache-subnet-group-check
<a name="elasticache-subnet-group-check"></a>

Checks if Amazon ElastiCache clusters are configured with a custom subnet group. The rule is NON\_COMPLIANT for an ElastiCache cluster if it is using a default subnet group.

**Identifier:** ELASTICACHE\_SUBNET\_GROUP\_CHECK

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d753c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
