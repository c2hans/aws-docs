---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-rotation-enabled-check.html
---

# secretsmanager-rotation-enabled-check
<a name="secretsmanager-rotation-enabled-check"></a>

Checks if AWS Secrets Manager secret has rotation enabled. The rule also checks an optional `maximumAllowedRotationFrequency` parameter. If the parameter is specified, the rotation frequency of the secret is compared with the maximum allowed frequency. The rule is NON\_COMPLIANT if the secret is not scheduled for rotation. The rule is also NON\_COMPLIANT if the rotation frequency is higher than the number specified in the maximumAllowedRotationFrequency parameter.

**Note**
Re-evaluating this rule within 4 hours of the first evaluation will have no effect on the results.

**Identifier:** SECRETSMANAGER\_ROTATION\_ENABLED\_CHECK

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

maximumAllowedRotationFrequencyInHours (Optional)Type: int
Maximum allowed rotation frequency of the secret in hours.

maximumAllowedRotationFrequency (Optional)Type: int
Maximum allowed rotation frequency of the secret in days.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1505c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
