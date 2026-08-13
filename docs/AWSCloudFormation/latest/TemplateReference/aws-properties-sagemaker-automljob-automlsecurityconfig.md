---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-automljob-automlsecurityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AutoMLJob AutoMLSecurityConfig
<a name="aws-properties-sagemaker-automljob-automlsecurityconfig"></a>

Security options.

## Syntax
<a name="aws-properties-sagemaker-automljob-automlsecurityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-automljob-automlsecurityconfig-syntax.json"></a>

```
{
  "[EnableInterContainerTrafficEncryption](#cfn-sagemaker-automljob-automlsecurityconfig-enableintercontainertrafficencryption)" : {{Boolean}},
  "[VolumeKmsKeyId](#cfn-sagemaker-automljob-automlsecurityconfig-volumekmskeyid)" : {{String}},
  "[VpcConfig](#cfn-sagemaker-automljob-automlsecurityconfig-vpcconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-automljob-automlsecurityconfig-syntax.yaml"></a>

```
  [EnableInterContainerTrafficEncryption](#cfn-sagemaker-automljob-automlsecurityconfig-enableintercontainertrafficencryption): {{Boolean}}
  [VolumeKmsKeyId](#cfn-sagemaker-automljob-automlsecurityconfig-volumekmskeyid): {{String}}
  [VpcConfig](#cfn-sagemaker-automljob-automlsecurityconfig-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-sagemaker-automljob-automlsecurityconfig-properties"></a>

`EnableInterContainerTrafficEncryption`  <a name="cfn-sagemaker-automljob-automlsecurityconfig-enableintercontainertrafficencryption"></a>
Whether to use traffic encryption between the container layers.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeKmsKeyId`  <a name="cfn-sagemaker-automljob-automlsecurityconfig-volumekmskeyid"></a>
The key used to encrypt stored data.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-sagemaker-automljob-automlsecurityconfig-vpcconfig"></a>
The VPC configuration.
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-automljob-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
