---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cognito-identity-pool-unauth-access-check.html
---

# cognito-identity-pool-unauth-access-check
<a name="cognito-identity-pool-unauth-access-check"></a>

Checks if Amazon Cognito Identity Pool allows unauthenticated identities. The rule is NON\_COMPLIANT if the Identity Pool is configured to allow unauthenticated identities.

**Identifier:** COGNITO\_IDENTITY\_POOL\_UNAUTH\_ACCESS\_CHECK

**Resource Types:** AWS::Cognito::IdentityPool

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), AWS GovCloud (US-East), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d411c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
