---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-entityrecognizer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizer
<a name="aws-resource-comprehend-entityrecognizer"></a>

Creates an entity recognizer using submitted files. After your `CreateEntityRecognizer` request is submitted, you can check job status using the `DescribeEntityRecognizer` API.

## Syntax
<a name="aws-resource-comprehend-entityrecognizer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-entityrecognizer-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::EntityRecognizer",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-entityrecognizer-dataaccessrolearn)" : {{String}},
      "[InputDataConfig](#cfn-comprehend-entityrecognizer-inputdataconfig)" : {{EntityRecognizerInputDataConfig}},
      "[LanguageCode](#cfn-comprehend-entityrecognizer-languagecode)" : {{String}},
      "[ModelKmsKeyId](#cfn-comprehend-entityrecognizer-modelkmskeyid)" : {{String}},
      "[ModelPolicy](#cfn-comprehend-entityrecognizer-modelpolicy)" : {{String}},
      "[RecognizerName](#cfn-comprehend-entityrecognizer-recognizername)" : {{String}},
      "[Tags](#cfn-comprehend-entityrecognizer-tags)" : {{[ Tag, ... ]}},
      "[VersionName](#cfn-comprehend-entityrecognizer-versionname)" : {{String}},
      "[VolumeKmsKeyId](#cfn-comprehend-entityrecognizer-volumekmskeyid)" : {{String}},
      "[VpcConfig](#cfn-comprehend-entityrecognizer-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-entityrecognizer-syntax.yaml"></a>

```
Type: AWS::Comprehend::EntityRecognizer
Properties:
  [DataAccessRoleArn](#cfn-comprehend-entityrecognizer-dataaccessrolearn): {{String}}
  [InputDataConfig](#cfn-comprehend-entityrecognizer-inputdataconfig): {{
    EntityRecognizerInputDataConfig}}
  [LanguageCode](#cfn-comprehend-entityrecognizer-languagecode): {{String}}
  [ModelKmsKeyId](#cfn-comprehend-entityrecognizer-modelkmskeyid): {{String}}
  [ModelPolicy](#cfn-comprehend-entityrecognizer-modelpolicy): {{String}}
  [RecognizerName](#cfn-comprehend-entityrecognizer-recognizername): {{String}}
  [Tags](#cfn-comprehend-entityrecognizer-tags): {{
    - Tag}}
  [VersionName](#cfn-comprehend-entityrecognizer-versionname): {{String}}
  [VolumeKmsKeyId](#cfn-comprehend-entityrecognizer-volumekmskeyid): {{String}}
  [VpcConfig](#cfn-comprehend-entityrecognizer-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-comprehend-entityrecognizer-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-entityrecognizer-dataaccessrolearn"></a>
 The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-comprehend-entityrecognizer-inputdataconfig"></a>
The input data properties of an entity recognizer.
*Required*: Yes
*Type*: [EntityRecognizerInputDataConfig](aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LanguageCode`  <a name="cfn-comprehend-entityrecognizer-languagecode"></a>
 The language of the input documents. All documents must be in the same language. Only English ("en") is currently supported.
*Required*: Yes
*Type*: String
*Allowed values*: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelKmsKeyId`  <a name="cfn-comprehend-entityrecognizer-modelkmskeyid"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
*Required*: No
*Type*: String
*Pattern*: `^\p{ASCII}+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelPolicy`  <a name="cfn-comprehend-entityrecognizer-modelpolicy"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\u0009\u000A\u000D\u0020-\u00FF]+$`
*Minimum*: `1`
*Maximum*: `20000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecognizerName`  <a name="cfn-comprehend-entityrecognizer-recognizername"></a>
 The name that you assigned the entity recognizer.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-entityrecognizer-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-entityrecognizer-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionName`  <a name="cfn-comprehend-entityrecognizer-versionname"></a>
The version name you assigned to the entity recognizer.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeKmsKeyId`  <a name="cfn-comprehend-entityrecognizer-volumekmskeyid"></a>
ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
*Required*: No
*Type*: String
*Pattern*: `^\p{ASCII}+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfig`  <a name="cfn-comprehend-entityrecognizer-vpcconfig"></a>
 Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
*Required*: No
*Type*: [VpcConfig](aws-properties-comprehend-entityrecognizer-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-entityrecognizer-return-values"></a>

### Ref
<a name="aws-resource-comprehend-entityrecognizer-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-entityrecognizer-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-entityrecognizer-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.
