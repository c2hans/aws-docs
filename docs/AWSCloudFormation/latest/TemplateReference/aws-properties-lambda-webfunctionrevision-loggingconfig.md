---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision LoggingConfig
<a name="aws-properties-lambda-webfunctionrevision-loggingconfig"></a>

The function's Amazon CloudWatch Logs configuration settings.

## Syntax
<a name="aws-properties-lambda-webfunctionrevision-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionrevision-loggingconfig-syntax.json"></a>

```
{
  "[ApplicationLogLevel](#cfn-lambda-webfunctionrevision-loggingconfig-applicationloglevel)" : {{String}},
  "[LogGroup](#cfn-lambda-webfunctionrevision-loggingconfig-loggroup)" : {{String}},
  "[SystemLogLevel](#cfn-lambda-webfunctionrevision-loggingconfig-systemloglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionrevision-loggingconfig-syntax.yaml"></a>

```
  [ApplicationLogLevel](#cfn-lambda-webfunctionrevision-loggingconfig-applicationloglevel): {{String}}
  [LogGroup](#cfn-lambda-webfunctionrevision-loggingconfig-loggroup): {{String}}
  [SystemLogLevel](#cfn-lambda-webfunctionrevision-loggingconfig-systemloglevel): {{String}}
```

## Properties
<a name="aws-properties-lambda-webfunctionrevision-loggingconfig-properties"></a>

`ApplicationLogLevel`  <a name="cfn-lambda-webfunctionrevision-loggingconfig-applicationloglevel"></a>
Set this property to filter the application logs for your function that Lambda sends to CloudWatch. Lambda only sends application logs at the selected level of detail and lower, where `TRACE` is the highest level and `FATAL` is the lowest.
*Required*: No
*Type*: String
*Allowed values*: `TRACE | DEBUG | INFO | WARN | ERROR | FATAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogGroup`  <a name="cfn-lambda-webfunctionrevision-loggingconfig-loggroup"></a>
The name of the Amazon CloudWatch log group the function sends logs to. By default, Lambda functions send logs to a default log group named `/aws/lambda/<function name>`. To use a different log group, enter an existing log group or enter a new log group name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\.\-_/#]+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SystemLogLevel`  <a name="cfn-lambda-webfunctionrevision-loggingconfig-systemloglevel"></a>
Set this property to filter the system logs for your function that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest.
*Required*: No
*Type*: String
*Allowed values*: `DEBUG | INFO | WARN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
