---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-cloudwatchlogslogdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe CloudwatchLogsLogDestination
<a name="aws-properties-pipes-pipe-cloudwatchlogslogdestination"></a>

Represents the Amazon CloudWatch Logs logging configuration settings for the pipe.

## Syntax
<a name="aws-properties-pipes-pipe-cloudwatchlogslogdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-cloudwatchlogslogdestination-syntax.json"></a>

```
{
  "[LogGroupArn](#cfn-pipes-pipe-cloudwatchlogslogdestination-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-cloudwatchlogslogdestination-syntax.yaml"></a>

```
  [LogGroupArn](#cfn-pipes-pipe-cloudwatchlogslogdestination-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-cloudwatchlogslogdestination-properties"></a>

`LogGroupArn`  <a name="cfn-pipes-pipe-cloudwatchlogslogdestination-loggrouparn"></a>
The AWS Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:logs:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):log-group:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
