---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-mltransform-mluserdataencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::MLTransform MLUserDataEncryption
<a name="aws-properties-glue-mltransform-mluserdataencryption"></a>

The encryption-at-rest settings of the transform that apply to accessing user data.

## Syntax
<a name="aws-properties-glue-mltransform-mluserdataencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-mltransform-mluserdataencryption-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-glue-mltransform-mluserdataencryption-kmskeyid)" : {{String}},
  "[MLUserDataEncryptionMode](#cfn-glue-mltransform-mluserdataencryption-mluserdataencryptionmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-mltransform-mluserdataencryption-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-glue-mltransform-mluserdataencryption-kmskeyid): {{String}}
  [MLUserDataEncryptionMode](#cfn-glue-mltransform-mluserdataencryption-mluserdataencryptionmode): {{String}}
```

## Properties
<a name="aws-properties-glue-mltransform-mluserdataencryption-properties"></a>

`KmsKeyId`  <a name="cfn-glue-mltransform-mluserdataencryption-kmskeyid"></a>
The ID for the customer-provided KMS key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MLUserDataEncryptionMode`  <a name="cfn-glue-mltransform-mluserdataencryption-mluserdataencryptionmode"></a>
The encryption mode applied to user data. Valid values are:
+ DISABLED: encryption is disabled.
+ SSEKMS: use of server-side encryption with AWS Key Management Service (SSE-KMS) for user data stored in Amazon S3.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
