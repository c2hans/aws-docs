---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVSChat::LoggingConfiguration CloudWatchLogsDestinationConfiguration
<a name="aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration"></a>

The CloudWatchLogsDestinationConfiguration property type specifies a CloudWatch Logs location where chat logs will be stored.

## Syntax
<a name="aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-loggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-loggroupname): {{String}}
```

## Properties
<a name="aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-loggroupname"></a>
Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.
*Required*: Yes
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
