---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-application-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application EncryptionConfiguration
<a name="aws-properties-qbusiness-application-encryptionconfiguration"></a>

Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business. Amazon Q Business doesn't support asymmetric keys.

## Syntax
<a name="aws-properties-qbusiness-application-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-application-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-qbusiness-application-encryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-application-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-qbusiness-application-encryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-application-encryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-qbusiness-application-encryptionconfiguration-kmskeyid"></a>
The identifier of the AWS KMS key. Amazon Q Business doesn't support asymmetric keys.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
