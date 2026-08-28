---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-encrypted-at-rest.html
---

# elasticsearch-encrypted-at-rest
<a name="elasticsearch-encrypted-at-rest"></a>

Checks if Amazon OpenSearch Service (previously called Elasticsearch) domains have encryption at rest configuration enabled. The rule is NON\_COMPLIANT if the EncryptionAtRestOptions field is not enabled.

**Identifier:** ELASTICSEARCH\_ENCRYPTED\_AT\_REST

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d763c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
