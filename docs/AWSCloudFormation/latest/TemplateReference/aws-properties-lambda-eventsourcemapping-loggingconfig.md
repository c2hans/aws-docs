---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping LoggingConfig
<a name="aws-properties-lambda-eventsourcemapping-loggingconfig"></a>

The function's Amazon CloudWatch Logs configuration settings.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-loggingconfig-syntax.json"></a>

```
{
  "[SystemLogLevel](#cfn-lambda-eventsourcemapping-loggingconfig-systemloglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-loggingconfig-syntax.yaml"></a>

```
  [SystemLogLevel](#cfn-lambda-eventsourcemapping-loggingconfig-systemloglevel): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-loggingconfig-properties"></a>

`SystemLogLevel`  <a name="cfn-lambda-eventsourcemapping-loggingconfig-systemloglevel"></a>
Set this property to filter the system logs for your function that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest.
*Required*: No
*Type*: String
*Allowed values*: `DEBUG | INFO | WARN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
