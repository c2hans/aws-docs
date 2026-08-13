---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-documentclassificationjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::DocumentClassificationJob
<a name="aws-resource-comprehend-documentclassificationjob"></a>

<a name="aws-resource-comprehend-documentclassificationjob-description"></a>The `AWS::Comprehend::DocumentClassificationJob` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-documentclassificationjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-documentclassificationjob-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::DocumentClassificationJob",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-documentclassificationjob-dataaccessrolearn)" : {{String}},
      "[DocumentClassifierArn](#cfn-comprehend-documentclassificationjob-documentclassifierarn)" : {{String}},
      "[InputDataConfig](#cfn-comprehend-documentclassificationjob-inputdataconfig)" : {{InputDataConfig}},
      "[JobName](#cfn-comprehend-documentclassificationjob-jobname)" : {{String}},
      "[Tags](#cfn-comprehend-documentclassificationjob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-documentclassificationjob-syntax.yaml"></a>

```
Type: AWS::Comprehend::DocumentClassificationJob
Properties:
  [DataAccessRoleArn](#cfn-comprehend-documentclassificationjob-dataaccessrolearn): {{String}}
  [DocumentClassifierArn](#cfn-comprehend-documentclassificationjob-documentclassifierarn): {{String}}
  [InputDataConfig](#cfn-comprehend-documentclassificationjob-inputdataconfig): {{
    InputDataConfig}}
  [JobName](#cfn-comprehend-documentclassificationjob-jobname): {{String}}
  [Tags](#cfn-comprehend-documentclassificationjob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-comprehend-documentclassificationjob-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-documentclassificationjob-dataaccessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DocumentClassifierArn`  <a name="cfn-comprehend-documentclassificationjob-documentclassifierarn"></a>
The Amazon Resource Name (ARN) that identifies the document classifier.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:document-classifier/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputDataConfig`  <a name="cfn-comprehend-documentclassificationjob-inputdataconfig"></a>
The input data configuration that you supplied when you created the document classification job.
*Required*: Yes
*Type*: [InputDataConfig](aws-properties-comprehend-documentclassificationjob-inputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobName`  <a name="cfn-comprehend-documentclassificationjob-jobname"></a>
The name that you assigned to the document classification job.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-documentclassificationjob-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-documentclassificationjob-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-documentclassificationjob-return-values"></a>

### Ref
<a name="aws-resource-comprehend-documentclassificationjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-documentclassificationjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-documentclassificationjob-return-values-fn--getatt-fn--getatt"></a>

`JobArn`  <a name="JobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the document classification job. It is a unique, fully qualified identifier for the job. It includes the AWS account, AWS Region, and the job ID. The format of the ARN is as follows:
 `arn:<partition>:comprehend:<region>:<account-id>:document-classification-job/<job-id>`
The following is an example job ARN:
 `arn:aws:comprehend:us-west-2:111122223333:document-classification-job/1234abcd12ab34cd56ef1234567890ab`

`JobId`  <a name="JobId-fn::getatt"></a>
The identifier assigned to the document classification job.

`JobStatus`  <a name="JobStatus-fn::getatt"></a>
The current status of the document classification job. If the status is `FAILED`, the `Message` field shows the reason for the failure.

`SubmitTime`  <a name="SubmitTime-fn::getatt"></a>
The time that the document classification job was submitted for processing.
