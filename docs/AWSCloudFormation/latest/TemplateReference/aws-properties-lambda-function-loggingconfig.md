---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-loggingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function LoggingConfig
<a name="aws-properties-lambda-function-loggingconfig"></a>

The function's Amazon CloudWatch Logs configuration settings.

## Syntax
<a name="aws-properties-lambda-function-loggingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-loggingconfig-syntax.json"></a>

```
{
  "[ApplicationLogLevel](#cfn-lambda-function-loggingconfig-applicationloglevel)" : {{String}},
  "[LogFormat](#cfn-lambda-function-loggingconfig-logformat)" : {{String}},
  "[LogGroup](#cfn-lambda-function-loggingconfig-loggroup)" : {{String}},
  "[SystemLogLevel](#cfn-lambda-function-loggingconfig-systemloglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-loggingconfig-syntax.yaml"></a>

```
  [ApplicationLogLevel](#cfn-lambda-function-loggingconfig-applicationloglevel): {{String}}
  [LogFormat](#cfn-lambda-function-loggingconfig-logformat): {{String}}
  [LogGroup](#cfn-lambda-function-loggingconfig-loggroup): {{String}}
  [SystemLogLevel](#cfn-lambda-function-loggingconfig-systemloglevel): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-loggingconfig-properties"></a>

`ApplicationLogLevel`  <a name="cfn-lambda-function-loggingconfig-applicationloglevel"></a>
Set this property to filter the application logs for your function that Lambda sends to CloudWatch. Lambda only sends application logs at the selected level of detail and lower, where `TRACE` is the highest level and `FATAL` is the lowest.
*Required*: No
*Type*: String
*Allowed values*: `TRACE | DEBUG | INFO | WARN | ERROR | FATAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogFormat`  <a name="cfn-lambda-function-loggingconfig-logformat"></a>
The format in which Lambda sends your function's application and system logs to CloudWatch. Select between plain text and structured JSON.
*Required*: No
*Type*: String
*Allowed values*: `Text | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroup`  <a name="cfn-lambda-function-loggingconfig-loggroup"></a>
The name of the Amazon CloudWatch log group the function sends logs to. By default, Lambda functions send logs to a default log group named `/aws/lambda/<function name>`. To use a different log group, enter an existing log group or enter a new log group name.
*Required*: No
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemLogLevel`  <a name="cfn-lambda-function-loggingconfig-systemloglevel"></a>
Set this property to filter the system logs for your function that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest.
*Required*: No
*Type*: String
*Allowed values*: `DEBUG | INFO | WARN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
