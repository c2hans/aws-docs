---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ecs-no-environment-secrets.html
---

# ecs-no-environment-secrets
<a name="ecs-no-environment-secrets"></a>

Checks if secrets are passed as container environment variables. The rule is NON\_COMPLIANT if 1 or more environment variable key matches a key listed in the '`secretKeys`' parameter (excluding environmental variables from other locations such as Amazon S3).

**Note**
This rule only evaluates the latest active revision of an Amazon ECS task definition.

**Identifier:** ECS\_NO\_ENVIRONMENT\_SECRETS

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei) Region

**Parameters:**

secretKeysType: CSV
Comma-separated list of key names to search for in the environment variables of container definitions within Task Definitions. Extra spaces will be removed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d669c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
