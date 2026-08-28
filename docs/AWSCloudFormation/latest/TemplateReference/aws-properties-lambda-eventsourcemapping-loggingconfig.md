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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
