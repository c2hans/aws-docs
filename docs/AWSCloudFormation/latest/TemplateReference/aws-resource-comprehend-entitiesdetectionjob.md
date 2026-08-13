---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-entitiesdetectionjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntitiesDetectionJob
<a name="aws-resource-comprehend-entitiesdetectionjob"></a>

<a name="aws-resource-comprehend-entitiesdetectionjob-description"></a>The `AWS::Comprehend::EntitiesDetectionJob` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-entitiesdetectionjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-entitiesdetectionjob-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::EntitiesDetectionJob",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-entitiesdetectionjob-dataaccessrolearn)" : {{String}},
      "[InputDataConfig](#cfn-comprehend-entitiesdetectionjob-inputdataconfig)" : {{InputDataConfig}},
      "[JobName](#cfn-comprehend-entitiesdetectionjob-jobname)" : {{String}},
      "[LanguageCode](#cfn-comprehend-entitiesdetectionjob-languagecode)" : {{String}},
      "[Tags](#cfn-comprehend-entitiesdetectionjob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-entitiesdetectionjob-syntax.yaml"></a>

```
Type: AWS::Comprehend::EntitiesDetectionJob
Properties:
  [DataAccessRoleArn](#cfn-comprehend-entitiesdetectionjob-dataaccessrolearn): {{String}}
  [InputDataConfig](#cfn-comprehend-entitiesdetectionjob-inputdataconfig): {{
    InputDataConfig}}
  [JobName](#cfn-comprehend-entitiesdetectionjob-jobname): {{String}}
  [LanguageCode](#cfn-comprehend-entitiesdetectionjob-languagecode): {{String}}
  [Tags](#cfn-comprehend-entitiesdetectionjob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-comprehend-entitiesdetectionjob-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-entitiesdetectionjob-dataaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-comprehend-entitiesdetectionjob-inputdataconfig"></a>
The input properties for a PII entities detection job.
*Required*: Yes
*Type*: [InputDataConfig](aws-properties-comprehend-entitiesdetectionjob-inputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobName`  <a name="cfn-comprehend-entitiesdetectionjob-jobname"></a>
The name that you assigned the PII entities detection job.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LanguageCode`  <a name="cfn-comprehend-entitiesdetectionjob-languagecode"></a>
The language code of the input documents.
*Required*: Yes
*Type*: String
*Allowed values*: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-entitiesdetectionjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-entitiesdetectionjob-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-entitiesdetectionjob-return-values"></a>

### Ref
<a name="aws-resource-comprehend-entitiesdetectionjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-entitiesdetectionjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-entitiesdetectionjob-return-values-fn--getatt-fn--getatt"></a>

`JobArn`  <a name="JobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the PII entities detection job. It is a unique, fully qualified identifier for the job. It includes the AWS account, AWS Region, and the job ID. The format of the ARN is as follows:
 `arn:<partition>:comprehend:<region>:<account-id>:pii-entities-detection-job/<job-id>`
The following is an example job ARN:
 `arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab`

`JobId`  <a name="JobId-fn::getatt"></a>
The identifier assigned to the PII entities detection job.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the PII entities detection job. If the status is `FAILED`, the `Message` field shows the reason for the failure.

`SubmitTime`  <a name="SubmitTime-fn::getatt"></a>
The time that the PII entities detection job was submitted for processing.
