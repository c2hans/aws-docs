---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cloudwatchlogging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage CloudWatchLogging
<a name="aws-properties-lambda-microvmimage-cloudwatchlogging"></a>

Configuration for Amazon CloudWatch Logs logging.

## Syntax
<a name="aws-properties-lambda-microvmimage-cloudwatchlogging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-cloudwatchlogging-syntax.json"></a>

```
{
  "[LogGroup](#cfn-lambda-microvmimage-cloudwatchlogging-loggroup)" : {{String}},
  "[LogStream](#cfn-lambda-microvmimage-cloudwatchlogging-logstream)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-cloudwatchlogging-syntax.yaml"></a>

```
  [LogGroup](#cfn-lambda-microvmimage-cloudwatchlogging-loggroup): {{String}}
  [LogStream](#cfn-lambda-microvmimage-cloudwatchlogging-logstream): {{String}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-cloudwatchlogging-properties"></a>

`LogGroup`  <a name="cfn-lambda-microvmimage-cloudwatchlogging-loggroup"></a>
The name of the CloudWatch Logs log group to send logs to.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/.#]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogStream`  <a name="cfn-lambda-microvmimage-cloudwatchlogging-logstream"></a>
The name of the CloudWatch Logs log stream within the log group.
*Required*: No
*Type*: String
*Pattern*: `^[^:*]*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
