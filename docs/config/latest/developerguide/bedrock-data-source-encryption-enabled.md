---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/bedrock-data-source-encryption-enabled.html
---

# bedrock-data-source-encryption-enabled
<a name="bedrock-data-source-encryption-enabled"></a>

Checks whether an Amazon Bedrock data source is encrypted with a customer-managed KMS key. The rule is NON\_COMPLIANT if the data source does not have ServerSideEncryptionConfiguration.KmsKeyArn configured.

**Identifier:** BEDROCK\_DATA\_SOURCE\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::Bedrock::DataSource

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hong Kong), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d285c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
