---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-capacity-provider-termination-check.html
---

# ecs-capacity-provider-termination-check
<a name="ecs-capacity-provider-termination-check"></a>

Checks if an Amazon ECS Capacity provider containing Auto Scaling groups has managed termination protection enabled. This rule is NON\_COMPLIANT if managed termination protection is disabled on the ECS Capacity Provider.

**Identifier:** ECS\_CAPACITY\_PROVIDER\_TERMINATION\_CHECK

**Resource Types:** AWS::ECS::CapacityProvider

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Malaysia), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d659c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
