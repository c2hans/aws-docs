---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html
---

# secretsmanager-scheduled-rotation-success-check
<a name="secretsmanager-scheduled-rotation-success-check"></a>

Checks if AWS Secrets Manager secrets rotated successfully according to the rotation schedule. Secrets Manager calculates the date the rotation should happen. The rule is NON\_COMPLIANT if the date passes and the secret isn't rotated.

**Note**
**Recording delays**
Evaluation results for this rule can be delayed for up to 2 days from a missed rotation date. For more immediate monitoring, see [Monitor AWS Secrets Manager with Amazon CloudWatch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring-cloudwatch.html) in the *Secrets Manager User Guide*.
**Secrets without rotation**
The rule returns `NOT_APPLICABLE` for secrets that aren't configured for rotation.

**Identifier:** SECRETSMANAGER\_SCHEDULED\_ROTATION\_SUCCESS\_CHECK

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1507c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
