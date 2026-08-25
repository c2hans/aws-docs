---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-dominantlanguagedetectionjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::DominantLanguageDetectionJob
<a name="aws-resource-comprehend-dominantlanguagedetectionjob"></a>

<a name="aws-resource-comprehend-dominantlanguagedetectionjob-description"></a>The `AWS::Comprehend::DominantLanguageDetectionJob` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::DominantLanguageDetectionJob",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-dominantlanguagedetectionjob-dataaccessrolearn)" : {{String}},
      "[InputDataConfig](#cfn-comprehend-dominantlanguagedetectionjob-inputdataconfig)" : {{InputDataConfig}},
      "[JobName](#cfn-comprehend-dominantlanguagedetectionjob-jobname)" : {{String}},
      "[Tags](#cfn-comprehend-dominantlanguagedetectionjob-tags)" : {{[ Tag, ... ]}},
      "[VolumeKmsKeyId](#cfn-comprehend-dominantlanguagedetectionjob-volumekmskeyid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-syntax.yaml"></a>

```
Type: AWS::Comprehend::DominantLanguageDetectionJob
Properties:
  [DataAccessRoleArn](#cfn-comprehend-dominantlanguagedetectionjob-dataaccessrolearn): {{String}}
  [InputDataConfig](#cfn-comprehend-dominantlanguagedetectionjob-inputdataconfig): {{
    InputDataConfig}}
  [JobName](#cfn-comprehend-dominantlanguagedetectionjob-jobname): {{String}}
  [Tags](#cfn-comprehend-dominantlanguagedetectionjob-tags): {{
    - Tag}}
  [VolumeKmsKeyId](#cfn-comprehend-dominantlanguagedetectionjob-volumekmskeyid): {{String}}
```

## Properties
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-dominantlanguagedetectionjob-dataaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-comprehend-dominantlanguagedetectionjob-inputdataconfig"></a>
The input data configuration that you supplied when you created the dominant language detection job.
*Required*: No
*Type*: [InputDataConfig](aws-properties-comprehend-dominantlanguagedetectionjob-inputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobName`  <a name="cfn-comprehend-dominantlanguagedetectionjob-jobname"></a>
The name that you assigned to the dominant language detection job.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-dominantlanguagedetectionjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-dominantlanguagedetectionjob-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeKmsKeyId`  <a name="cfn-comprehend-dominantlanguagedetectionjob-volumekmskeyid"></a>
ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-return-values"></a>

### Ref
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-dominantlanguagedetectionjob-return-values-fn--getatt-fn--getatt"></a>

`JobArn`  <a name="JobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dominant language detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, AWS Region, and the job ID. The format of the ARN is as follows:
 `arn:<partition>:comprehend:<region>:<account-id>:dominant-language-detection-job/<job-id>`
The following is an example job ARN:
 `arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/1234abcd12ab34cd56ef1234567890ab`

`JobId`  <a name="JobId-fn::getatt"></a>
The identifier assigned to the dominant language detection job.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the dominant language detection job. If the status is `FAILED`, the `Message` field shows the reason for the failure.
