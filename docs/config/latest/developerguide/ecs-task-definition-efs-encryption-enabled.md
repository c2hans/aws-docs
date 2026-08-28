---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-efs-encryption-enabled.html
---

# ecs-task-definition-efs-encryption-enabled
<a name="ecs-task-definition-efs-encryption-enabled"></a>

Checks if Amazon ECS Task Definitions with EFS volumes have in-transit encryption enabled. The rule is NON\_COMPLIANT if an ECS Task Definition contains an EFS volume without transit encryption enabled.

**Identifier:** ECS\_TASK\_DEFINITION\_EFS\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d673c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
