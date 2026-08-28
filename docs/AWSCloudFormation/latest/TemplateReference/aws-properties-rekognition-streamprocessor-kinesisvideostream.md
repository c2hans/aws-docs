---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-kinesisvideostream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor KinesisVideoStream
<a name="aws-properties-rekognition-streamprocessor-kinesisvideostream"></a>

The Kinesis video stream that provides the source of the streaming video for an Amazon Rekognition Video stream processor. For more information, see [KinesisVideoStream](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisVideoStream).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-kinesisvideostream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-kinesisvideostream-syntax.json"></a>

```
{
  "[Arn](#cfn-rekognition-streamprocessor-kinesisvideostream-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-kinesisvideostream-syntax.yaml"></a>

```
  [Arn](#cfn-rekognition-streamprocessor-kinesisvideostream-arn): {{String}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-kinesisvideostream-properties"></a>

`Arn`  <a name="cfn-rekognition-streamprocessor-kinesisvideostream-arn"></a>
ARN of the Kinesis video stream stream that streams the source video.
*Required*: Yes
*Type*: String
*Pattern*: `(^arn:([a-z\d-]+):kinesisvideo:([a-z\d-]+):\d{12}:.+$)`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
