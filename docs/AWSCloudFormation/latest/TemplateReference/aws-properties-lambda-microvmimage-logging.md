---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage Logging
<a name="aws-properties-lambda-microvmimage-logging"></a>

Configuration for MicroVM logging output. Specify exactly one: cloudWatch to enable CloudWatch logging, or disabled to turn off logging.

## Syntax
<a name="aws-properties-lambda-microvmimage-logging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-logging-syntax.json"></a>

```
{
  "[CloudWatch](#cfn-lambda-microvmimage-logging-cloudwatch)" : {{CloudWatchLogging}},
  "[Disabled](#cfn-lambda-microvmimage-logging-disabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-logging-syntax.yaml"></a>

```
  [CloudWatch](#cfn-lambda-microvmimage-logging-cloudwatch): {{
    CloudWatchLogging}}
  [Disabled](#cfn-lambda-microvmimage-logging-disabled): {{Boolean}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-logging-properties"></a>

`CloudWatch`  <a name="cfn-lambda-microvmimage-logging-cloudwatch"></a>
Configuration for sending logs to Amazon CloudWatch Logs.
*Required*: No
*Type*: [CloudWatchLogging](aws-properties-lambda-microvmimage-cloudwatchlogging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Disabled`  <a name="cfn-lambda-microvmimage-logging-disabled"></a>
Specifies that logging is disabled for the MicroVM.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
