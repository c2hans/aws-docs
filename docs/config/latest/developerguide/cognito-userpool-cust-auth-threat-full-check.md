---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cognito-userpool-cust-auth-threat-full-check.html
---

# cognito-userpool-cust-auth-threat-full-check
<a name="cognito-userpool-cust-auth-threat-full-check"></a>

Checks if Amazon Cognito user pools have threat protection enabled with full-function enforcement mode for custom authentication. This rule is NON\_COMPLIANT if threat protection for custom authentication is not set to full-function enforcement mode.

**Identifier:** COGNITO\_USERPOOL\_CUST\_AUTH\_THREAT\_FULL\_CHECK

**Resource Types:** AWS::Cognito::UserPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d413c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
