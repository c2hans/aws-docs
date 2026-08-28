---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-s3destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor S3Destination
<a name="aws-properties-rekognition-streamprocessor-s3destination"></a>

The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation. These results include the name of the stream processor resource, the session ID of the stream processing session, and labeled timestamps and bounding boxes for detected labels. For more information, see [S3Destination](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_S3Destination).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-s3destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-s3destination-syntax.json"></a>

```
{
  "[BucketName](#cfn-rekognition-streamprocessor-s3destination-bucketname)" : {{String}},
  "[ObjectKeyPrefix](#cfn-rekognition-streamprocessor-s3destination-objectkeyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-s3destination-syntax.yaml"></a>

```
  [BucketName](#cfn-rekognition-streamprocessor-s3destination-bucketname): {{String}}
  [ObjectKeyPrefix](#cfn-rekognition-streamprocessor-s3destination-objectkeyprefix): {{String}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-s3destination-properties"></a>

`BucketName`  <a name="cfn-rekognition-streamprocessor-s3destination-bucketname"></a>
Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name of a stream processor's exports.
*Required*: Yes
*Type*: String
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectKeyPrefix`  <a name="cfn-rekognition-streamprocessor-s3destination-objectkeyprefix"></a>
Describes the destination Amazon Simple Storage Service (Amazon S3) object keys of a stream processor's exports.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
