---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cognito-user-pool-password-policy-check.html
---

# cognito-user-pool-password-policy-check
<a name="cognito-user-pool-password-policy-check"></a>

Checks if the password policy for Amazon cognito user pool meets the specified requirements indicated in the parameters. The rule is NON\_COMPLIANT if the user pool password policy does not meet the specified requirements.

**Identifier:** COGNITO\_USER\_POOL\_PASSWORD\_POLICY\_CHECK

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

requireSymbols (Optional)Type: booleanDefault: True
Whether to require at least one symbol in password.

temporaryPasswordValidity (Optional)Type: intDefault: 7
Number of days a temporary password remains valid. Valid values are 1 to 365.

minLength (Optional)Type: intDefault: 8
Minimum length required for user pool password. Valid values are 5 to 128.

requireNumbers (Optional)Type: booleanDefault: True
Whether to require at least one number in password.

requireUppercase (Optional)Type: booleanDefault: True
Whether to require at least one uppercase letter in password.

requireLowercase (Optional)Type: booleanDefault: True
Whether to require at least one lowercase letter in password.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d421c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
