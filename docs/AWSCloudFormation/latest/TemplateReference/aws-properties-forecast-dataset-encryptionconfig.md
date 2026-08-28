---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-forecast-dataset-encryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Forecast::Dataset EncryptionConfig
<a name="aws-properties-forecast-dataset-encryptionconfig"></a>

An AWS Key Management Service (KMS) key and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key. You can specify this optional object in the [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html) and [CreatePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictor.html) requests.

## Syntax
<a name="aws-properties-forecast-dataset-encryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-forecast-dataset-encryptionconfig-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-forecast-dataset-encryptionconfig-kmskeyarn)" : {{String}},
  "[RoleArn](#cfn-forecast-dataset-encryptionconfig-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-forecast-dataset-encryptionconfig-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-forecast-dataset-encryptionconfig-kmskeyarn): {{String}}
  [RoleArn](#cfn-forecast-dataset-encryptionconfig-rolearn): {{String}}
```

## Properties
<a name="aws-properties-forecast-dataset-encryptionconfig-properties"></a>

`KmsKeyArn`  <a name="cfn-forecast-dataset-encryptionconfig-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key.
*Required*: No
*Type*: String
*Pattern*: `arn:aws[-a-z]*:kms:.*:key/.*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-forecast-dataset-encryptionconfig-rolearn"></a>
The ARN of the IAM role that Amazon Forecast can assume to access the AWS KMS key.
Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an `InvalidInputException` error.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\_\.\/\:]+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
