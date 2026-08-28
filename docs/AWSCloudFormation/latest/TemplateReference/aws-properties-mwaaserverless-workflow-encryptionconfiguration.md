---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow EncryptionConfiguration
<a name="aws-properties-mwaaserverless-workflow-encryptionconfiguration"></a>

Configuration for encrypting workflow data at rest and in transit. Amazon Managed Workflows for Apache Airflow Serverless provides comprehensive encryption capabilities to protect sensitive workflow data, parameters, and execution logs. When using customer-managed keys, the service integrates with AWSAWS KMS to provide fine-grained access control and audit capabilities. Encryption is applied consistently across the distributed execution environment including task containers, metadata storage, and log streams.

## Syntax
<a name="aws-properties-mwaaserverless-workflow-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaaserverless-workflow-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-mwaaserverless-workflow-encryptionconfiguration-kmskeyid)" : {{String}},
  "[Type](#cfn-mwaaserverless-workflow-encryptionconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-mwaaserverless-workflow-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-mwaaserverless-workflow-encryptionconfiguration-kmskeyid): {{String}}
  [Type](#cfn-mwaaserverless-workflow-encryptionconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-mwaaserverless-workflow-encryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-mwaaserverless-workflow-encryptionconfiguration-kmskeyid"></a>
The ID or ARN of the AWS KMS key to use for encryption. Required when `Type` is `CUSTOMER_MANAGED_KEY`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-mwaaserverless-workflow-encryptionconfiguration-type"></a>
The type of encryption to use. Values are `AWS_MANAGED_KEY` (AWS manages the encryption key) or `CUSTOMER_MANAGED_KEY` (you provide a KMS key).
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_MANAGED_KEY | CUSTOMER_MANAGED_KEY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
