---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-cache-enabled-and-encrypted.html
---

# api-gw-cache-enabled-and-encrypted
<a name="api-gw-cache-enabled-and-encrypted"></a>

Checks if all methods in Amazon API Gateway stages have cache enabled and cache encrypted. The rule is NON\_COMPLIANT if any method in an Amazon API Gateway stage is not configured to cache or the cache is not encrypted.

**Identifier:** API\_GW\_CACHE\_ENABLED\_AND\_ENCRYPTED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7c75c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
