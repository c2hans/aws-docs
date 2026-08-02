---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sns-topic-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SNS::Topic LoggingConfig
<a name="aws-properties-sns-topic-loggingconfig"></a>

The `LoggingConfig` property type specifies the `Delivery` status logging configuration for an [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html).

## Syntax
<a name="aws-properties-sns-topic-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sns-topic-loggingconfig-syntax.json"></a>

```
{
  "[FailureFeedbackRoleArn](#cfn-sns-topic-loggingconfig-failurefeedbackrolearn)" : {{String}},
  "[Protocol](#cfn-sns-topic-loggingconfig-protocol)" : {{String}},
  "[SuccessFeedbackRoleArn](#cfn-sns-topic-loggingconfig-successfeedbackrolearn)" : {{String}},
  "[SuccessFeedbackSampleRate](#cfn-sns-topic-loggingconfig-successfeedbacksamplerate)" : {{String}}
}
```

### YAML
<a name="aws-properties-sns-topic-loggingconfig-syntax.yaml"></a>

```
  [FailureFeedbackRoleArn](#cfn-sns-topic-loggingconfig-failurefeedbackrolearn): {{String}}
  [Protocol](#cfn-sns-topic-loggingconfig-protocol): {{String}}
  [SuccessFeedbackRoleArn](#cfn-sns-topic-loggingconfig-successfeedbackrolearn): {{String}}
  [SuccessFeedbackSampleRate](#cfn-sns-topic-loggingconfig-successfeedbacksamplerate): {{String}}
```

## Properties
<a name="aws-properties-sns-topic-loggingconfig-properties"></a>

`FailureFeedbackRoleArn`  <a name="cfn-sns-topic-loggingconfig-failurefeedbackrolearn"></a>
The IAM role ARN to be used when logging failed message deliveries in Amazon CloudWatch.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-sns-topic-loggingconfig-protocol"></a>
Indicates one of the supported protocols for the Amazon SNS topic.
At least one of the other three `LoggingConfig` properties is recommend along with `Protocol`.
*Required*: Yes
*Type*: String
*Allowed values*: `http/s | sqs | lambda | firehose | application`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessFeedbackRoleArn`  <a name="cfn-sns-topic-loggingconfig-successfeedbackrolearn"></a>
The IAM role ARN to be used when logging successful message deliveries in Amazon CloudWatch.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessFeedbackSampleRate`  <a name="cfn-sns-topic-loggingconfig-successfeedbacksamplerate"></a>
The percentage of successful message deliveries to be logged in Amazon CloudWatch. Valid percentage values range from 0 to 100.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
