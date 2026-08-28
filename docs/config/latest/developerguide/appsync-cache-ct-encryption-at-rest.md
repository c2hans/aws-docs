---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appsync-cache-ct-encryption-at-rest.html
---

# appsync-cache-ct-encryption-at-rest
<a name="appsync-cache-ct-encryption-at-rest"></a>

Checks if an AWS AppSync API cache has encryption at rest enabled. This rule is NON\_COMPLIANT if 'AtRestEncryptionEnabled' is false.

**Identifier:** APPSYNC\_CACHE\_CT\_ENCRYPTION\_AT\_REST

**Resource Types:** AWS::AppSync::ApiCache

**Trigger type:** Configuration changes

**AWS Region:** Only available in Middle East (Bahrain), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d189c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
