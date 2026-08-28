---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-repl-grp-encrypted-in-transit.html
---

# elasticache-repl-grp-encrypted-in-transit
<a name="elasticache-repl-grp-encrypted-in-transit"></a>

Checks if Amazon ElastiCache replication groups have encryption-in-transit enabled. The rule is NON\_COMPLIANT for an ElastiCache replication group if ‘TransitEncryptionEnabled’ is set to ‘false’.

**Identifier:** ELASTICACHE\_REPL\_GRP\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::ElastiCache::ReplicationGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d749c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
