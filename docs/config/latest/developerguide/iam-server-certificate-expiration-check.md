---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/iam-server-certificate-expiration-check.html
---

# iam-server-certificate-expiration-check
<a name="iam-server-certificate-expiration-check"></a>

Checks if AWS IAM SSL/TLS server certificates stored in IAM are expired. The rule is NON\_COMPLIANT if an IAM server certificate is expired.

**Identifier:** IAM\_SERVER\_CERTIFICATE\_EXPIRATION\_CHECK

**Resource Types:** AWS::IAM::ServerCertificate

**Trigger type:** Periodic

**AWS Region:** Only available in China (Beijing), US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d947c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
