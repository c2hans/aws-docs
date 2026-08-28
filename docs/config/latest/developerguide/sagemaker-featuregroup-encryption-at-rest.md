---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-featuregroup-encryption-at-rest.html
---

# sagemaker-featuregroup-encryption-at-rest
<a name="sagemaker-featuregroup-encryption-at-rest"></a>

Checks if SageMaker feature groups have KMS encryption for OfflineStore. The rule is NON\_COMPLIANT if offline store S3 storage does not have KMS key encryption.

**Identifier:** SAGEMAKER\_FEATUREGROUP\_ENCRYPTION\_AT\_REST

**Resource Types:** AWS::SageMaker::FeatureGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1453c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
