---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-service-propagate-tags-enabled.html
---

# ecs-service-propagate-tags-enabled
<a name="ecs-service-propagate-tags-enabled"></a>

Checks if AWS ECS Service has property PropagateTags with value of either SERVICE or TASK\_DEFINITION. The rule is NON\_COMPLIANT if the property does not exist or is NONE.

**Identifier:** ECS\_SERVICE\_PROPAGATE\_TAGS\_ENABLED

**Resource Types:** AWS::ECS::Service

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d671c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
