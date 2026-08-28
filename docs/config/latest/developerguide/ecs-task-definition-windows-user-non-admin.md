---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-windows-user-non-admin.html
---

# ecs-task-definition-windows-user-non-admin
<a name="ecs-task-definition-windows-user-non-admin"></a>

Checks if the latest active revision of an Amazon ECS task definition configures Windows containers to run as non-administrator users. The rule is NON\_COMPLIANT if default administrator user is specified or user configuration is absent for any container.

**Identifier:** ECS\_TASK\_DEFINITION\_WINDOWS\_USER\_NON\_ADMIN

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d689c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
