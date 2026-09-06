---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-securityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage SecurityConfig
<a name="aws-properties-sagemaker-modelpackage-securityconfig"></a>

Security configuration for the model package.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-securityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-securityconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-modelpackage-securityconfig-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-securityconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-modelpackage-securityconfig-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-securityconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-modelpackage-securityconfig-kmskeyid"></a>
The AWS KMS key ID used to encrypt the model package.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
