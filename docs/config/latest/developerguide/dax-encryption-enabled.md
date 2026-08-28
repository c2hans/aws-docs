---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/dax-encryption-enabled.html
---

# dax-encryption-enabled
<a name="dax-encryption-enabled"></a>

Checks if Amazon DynamoDB Accelerator (DAX) clusters are encrypted. The rule is NON\_COMPLIANT if a DAX cluster is not encrypted.

**Identifier:** DAX\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::DAX::Cluster

**Trigger type:** Periodic

**AWS Region:** Only available in Europe (Stockholm), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Europe (Spain), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d447c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
