---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-transformjob-datacaptureconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TransformJob DataCaptureConfig
<a name="aws-properties-sagemaker-transformjob-datacaptureconfig"></a>

Configuration to control how SageMaker AI captures inference data.

## Syntax
<a name="aws-properties-sagemaker-transformjob-datacaptureconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-transformjob-datacaptureconfig-syntax.json"></a>

```
{
  "[DestinationS3Uri](#cfn-sagemaker-transformjob-datacaptureconfig-destinations3uri)" : {{String}},
  "[GenerateInferenceId](#cfn-sagemaker-transformjob-datacaptureconfig-generateinferenceid)" : {{Boolean}},
  "[KmsKeyId](#cfn-sagemaker-transformjob-datacaptureconfig-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-transformjob-datacaptureconfig-syntax.yaml"></a>

```
  [DestinationS3Uri](#cfn-sagemaker-transformjob-datacaptureconfig-destinations3uri): {{String}}
  [GenerateInferenceId](#cfn-sagemaker-transformjob-datacaptureconfig-generateinferenceid): {{Boolean}}
  [KmsKeyId](#cfn-sagemaker-transformjob-datacaptureconfig-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-transformjob-datacaptureconfig-properties"></a>

`DestinationS3Uri`  <a name="cfn-sagemaker-transformjob-datacaptureconfig-destinations3uri"></a>
The Amazon S3 location used to capture the data.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GenerateInferenceId`  <a name="cfn-sagemaker-transformjob-datacaptureconfig-generateinferenceid"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-sagemaker-transformjob-datacaptureconfig-kmskeyid"></a>
The Amazon Resource Name (ARN) of an AWS Key Management Service key that SageMaker AI uses to encrypt the captured data at rest using Amazon S3 server-side encryption.
The KmsKeyId can be any of the following formats:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
