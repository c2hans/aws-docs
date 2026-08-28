---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/emr-security-configuration-encryption-rest.html
---

# emr-security-configuration-encryption-rest
<a name="emr-security-configuration-encryption-rest"></a>

Checks if an Amazon EMR security configuration has encryption at rest enabled. The rule is NON\_COMPLIANT if configuration.SecurityConfiguration.EncryptionConfiguration.EnableAtRestEncryption is false.

**Identifier:** EMR\_SECURITY\_CONFIGURATION\_ENCRYPTION\_REST

**Resource Types:** AWS::EMR::SecurityConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d811c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
