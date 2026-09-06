---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption CloudWatchLoggingOption
<a name="aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption"></a>

Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-syntax.json"></a>

```
{
  "[LogStreamARN](#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-syntax.yaml"></a>

```
  [LogStreamARN](#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-properties"></a>

`LogStreamARN`  <a name="cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn"></a>
The ARN of the CloudWatch log to receive application messages.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption--seealso"></a>
+ [CloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CloudWatchLoggingOption.html) in the *Amazon Kinesis Data Analytics API Reference*
