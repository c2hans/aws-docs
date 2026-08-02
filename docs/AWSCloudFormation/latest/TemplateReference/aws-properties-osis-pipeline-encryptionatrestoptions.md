---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-encryptionatrestoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline EncryptionAtRestOptions
<a name="aws-properties-osis-pipeline-encryptionatrestoptions"></a>

Options to control how OpenSearch encrypts buffer data.

## Syntax
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-osis-pipeline-encryptionatrestoptions-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-osis-pipeline-encryptionatrestoptions-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-properties"></a>

`KmsKeyArn`  <a name="cfn-osis-pipeline-encryptionatrestoptions-kmskeyarn"></a>
The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an AWS owned key.
*Required*: Yes
*Type*: String
*Minimum*: `7`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
