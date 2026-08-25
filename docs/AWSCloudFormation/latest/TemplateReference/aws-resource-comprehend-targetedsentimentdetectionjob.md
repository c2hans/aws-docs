---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-targetedsentimentdetectionjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::TargetedSentimentDetectionJob
<a name="aws-resource-comprehend-targetedsentimentdetectionjob"></a>

<a name="aws-resource-comprehend-targetedsentimentdetectionjob-description"></a>The `AWS::Comprehend::TargetedSentimentDetectionJob` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::TargetedSentimentDetectionJob",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-targetedsentimentdetectionjob-dataaccessrolearn)" : {{String}},
      "[InputDataConfig](#cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig)" : {{InputDataConfig}},
      "[JobName](#cfn-comprehend-targetedsentimentdetectionjob-jobname)" : {{String}},
      "[LanguageCode](#cfn-comprehend-targetedsentimentdetectionjob-languagecode)" : {{String}},
      "[Tags](#cfn-comprehend-targetedsentimentdetectionjob-tags)" : {{[ TagsItems, ... ]}},
      "[VolumeKmsKeyId](#cfn-comprehend-targetedsentimentdetectionjob-volumekmskeyid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-syntax.yaml"></a>

```
Type: AWS::Comprehend::TargetedSentimentDetectionJob
Properties:
  [DataAccessRoleArn](#cfn-comprehend-targetedsentimentdetectionjob-dataaccessrolearn): {{String}}
  [InputDataConfig](#cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig): {{
    InputDataConfig}}
  [JobName](#cfn-comprehend-targetedsentimentdetectionjob-jobname): {{String}}
  [LanguageCode](#cfn-comprehend-targetedsentimentdetectionjob-languagecode): {{String}}
  [Tags](#cfn-comprehend-targetedsentimentdetectionjob-tags): {{
    - TagsItems}}
  [VolumeKmsKeyId](#cfn-comprehend-targetedsentimentdetectionjob-volumekmskeyid): {{String}}
```

## Properties
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-targetedsentimentdetectionjob-dataaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig"></a>
The input properties for an inference job. The document reader config field applies only to non-text inputs for custom analysis.
*Required*: Yes
*Type*: [InputDataConfig](aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobName`  <a name="cfn-comprehend-targetedsentimentdetectionjob-jobname"></a>
The name that you assigned to the targeted sentiment detection job.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LanguageCode`  <a name="cfn-comprehend-targetedsentimentdetectionjob-languagecode"></a>
The language code of the input documents.
*Required*: Yes
*Type*: String
*Allowed values*: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-targetedsentimentdetectionjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-comprehend-targetedsentimentdetectionjob-tagsitems.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeKmsKeyId`  <a name="cfn-comprehend-targetedsentimentdetectionjob-volumekmskeyid"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data on the storage volume attached to the ML compute instance(s) that process the targeted sentiment detection job. The VolumeKmsKeyId can be either of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
*Required*: No
*Type*: String
*Pattern*: `^\p{ASCII}+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-return-values"></a>

### Ref
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-targetedsentimentdetectionjob-return-values-fn--getatt-fn--getatt"></a>

`EndTime`  <a name="EndTime-fn::getatt"></a>
The time that the targeted sentiment detection job ended.

`JobArn`  <a name="JobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the targeted sentiment detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, AWS Region, and the job ID. The format of the ARN is as follows:
 `arn:<partition>:comprehend:<region>:<account-id>:targeted-sentiment-detection-job/<job-id>`
The following is an example job ARN:
 `arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/1234abcd12ab34cd56ef1234567890ab`

`JobId`  <a name="JobId-fn::getatt"></a>
The identifier assigned to the targeted sentiment detection job.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the targeted sentiment detection job. If the status is `FAILED`, the `Messages` field shows the reason for the failure.

`SubmitTime`  <a name="SubmitTime-fn::getatt"></a>
The time that the targeted sentiment detection job was submitted for processing.
