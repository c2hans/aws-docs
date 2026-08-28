---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecr-private-tag-immutability-enabled.html
---

# ecr-private-tag-immutability-enabled
<a name="ecr-private-tag-immutability-enabled"></a>

Checks if a private Amazon Elastic Container Registry (ECR) repository has tag immutability enabled. This rule is NON\_COMPLIANT if tag immutability is not enabled for the private ECR repository.

**Identifier:** ECR\_PRIVATE\_TAG\_IMMUTABILITY\_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), Israel (Tel Aviv), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d649c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
