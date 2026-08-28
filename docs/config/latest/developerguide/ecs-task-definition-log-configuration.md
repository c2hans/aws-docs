---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html
---

# ecs-task-definition-log-configuration
<a name="ecs-task-definition-log-configuration"></a>

Checks if logConfiguration is set on active ECS Task Definitions. This rule is NON\_COMPLIANT if an active ECSTaskDefinition does not have the logConfiguration resource defined or the value for logConfiguration is null in at least one container definition.

**Note**
This rule only evaluates the latest active revision of an Amazon ECS task definition.

**Identifier:** ECS\_TASK\_DEFINITION\_LOG\_CONFIGURATION

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d677c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
