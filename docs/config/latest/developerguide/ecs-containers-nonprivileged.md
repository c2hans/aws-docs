---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-nonprivileged.html
---

# ecs-containers-nonprivileged
<a name="ecs-containers-nonprivileged"></a>

Checks if the privileged parameter in the container definition of ECSTaskDefinitions is set to ‘true’. The rule is NON\_COMPLIANT if the privileged parameter is ‘true’.

**Note**
This rule only evaluates the latest active revision of an Amazon ECS task definition.

**Identifier:** ECS\_CONTAINERS\_NONPRIVILEGED

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d661c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
