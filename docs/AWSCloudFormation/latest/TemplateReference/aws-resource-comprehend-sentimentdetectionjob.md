---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-sentimentdetectionjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::SentimentDetectionJob
<a name="aws-resource-comprehend-sentimentdetectionjob"></a>

<a name="aws-resource-comprehend-sentimentdetectionjob-description"></a>The `AWS::Comprehend::SentimentDetectionJob` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-sentimentdetectionjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-sentimentdetectionjob-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::SentimentDetectionJob",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-sentimentdetectionjob-dataaccessrolearn)" : {{String}},
      "[InputDataConfig](#cfn-comprehend-sentimentdetectionjob-inputdataconfig)" : {{InputDataConfig}},
      "[JobName](#cfn-comprehend-sentimentdetectionjob-jobname)" : {{String}},
      "[LanguageCode](#cfn-comprehend-sentimentdetectionjob-languagecode)" : {{String}},
      "[Tags](#cfn-comprehend-sentimentdetectionjob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-sentimentdetectionjob-syntax.yaml"></a>

```
Type: AWS::Comprehend::SentimentDetectionJob
Properties:
  [DataAccessRoleArn](#cfn-comprehend-sentimentdetectionjob-dataaccessrolearn): {{String}}
  [InputDataConfig](#cfn-comprehend-sentimentdetectionjob-inputdataconfig): {{
    InputDataConfig}}
  [JobName](#cfn-comprehend-sentimentdetectionjob-jobname): {{String}}
  [LanguageCode](#cfn-comprehend-sentimentdetectionjob-languagecode): {{String}}
  [Tags](#cfn-comprehend-sentimentdetectionjob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-comprehend-sentimentdetectionjob-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-sentimentdetectionjob-dataaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-comprehend-sentimentdetectionjob-inputdataconfig"></a>
The input data configuration that you supplied when you created the sentiment detection job.
*Required*: Yes
*Type*: [InputDataConfig](aws-properties-comprehend-sentimentdetectionjob-inputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobName`  <a name="cfn-comprehend-sentimentdetectionjob-jobname"></a>
The name that you assigned to the sentiment detection job
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LanguageCode`  <a name="cfn-comprehend-sentimentdetectionjob-languagecode"></a>
The language code of the input documents.
*Required*: Yes
*Type*: String
*Allowed values*: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-sentimentdetectionjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-sentimentdetectionjob-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-sentimentdetectionjob-return-values"></a>

### Ref
<a name="aws-resource-comprehend-sentimentdetectionjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-sentimentdetectionjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-sentimentdetectionjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`JobId`  <a name="JobId-fn::getatt"></a>
The identifier assigned to the sentiment detection job.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the sentiment detection job. If the status is `FAILED`, the `Messages` field shows the reason for the failure.
