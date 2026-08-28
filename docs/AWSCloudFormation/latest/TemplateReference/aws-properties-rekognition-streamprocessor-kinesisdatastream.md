---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-kinesisdatastream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor KinesisDataStream
<a name="aws-properties-rekognition-streamprocessor-kinesisdatastream"></a>

 Amazon Rekognition Video Stream Processor take as input a Kinesis video stream (Input) and a Kinesis data stream (Output). This is the Amazon Kinesis Data Streams instance to which the Amazon Rekognition stream processor streams the analysis results. This must be created within the constraints specified at [KinesisDataStream](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisDataStream).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-kinesisdatastream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-kinesisdatastream-syntax.json"></a>

```
{
  "[Arn](#cfn-rekognition-streamprocessor-kinesisdatastream-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-kinesisdatastream-syntax.yaml"></a>

```
  [Arn](#cfn-rekognition-streamprocessor-kinesisdatastream-arn): {{String}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-kinesisdatastream-properties"></a>

`Arn`  <a name="cfn-rekognition-streamprocessor-kinesisdatastream-arn"></a>
ARN of the output Amazon Kinesis Data Streams stream.
*Required*: Yes
*Type*: String
*Pattern*: `(^arn:([a-z\d-]+):kinesis:([a-z\d-]+):\d{12}:.+$)`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
