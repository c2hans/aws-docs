---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aiops-investigationgroup-encryptionconfigmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AIOps::InvestigationGroup EncryptionConfigMap
<a name="aws-properties-aiops-investigationgroup-encryptionconfigmap"></a>

Use this structure if you want to use a customer managed AWS KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an AWS key to encrypt the data. For more information, see [Encryption of investigation data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS).

## Syntax
<a name="aws-properties-aiops-investigationgroup-encryptionconfigmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aiops-investigationgroup-encryptionconfigmap-syntax.json"></a>

```
{
  "[EncryptionConfigurationType](#cfn-aiops-investigationgroup-encryptionconfigmap-encryptionconfigurationtype)" : {{String}},
  "[KmsKeyId](#cfn-aiops-investigationgroup-encryptionconfigmap-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-aiops-investigationgroup-encryptionconfigmap-syntax.yaml"></a>

```
  [EncryptionConfigurationType](#cfn-aiops-investigationgroup-encryptionconfigmap-encryptionconfigurationtype): {{String}}
  [KmsKeyId](#cfn-aiops-investigationgroup-encryptionconfigmap-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-aiops-investigationgroup-encryptionconfigmap-properties"></a>

`EncryptionConfigurationType`  <a name="cfn-aiops-investigationgroup-encryptionconfigmap-encryptionconfigurationtype"></a>
Displays whether investigation data is encrypted by a customer managed key or an AWS owned key.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-aiops-investigationgroup-encryptionconfigmap-kmskeyid"></a>
If the investigation group uses a customer managed key for encryption, this field displays the ID of that key.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
