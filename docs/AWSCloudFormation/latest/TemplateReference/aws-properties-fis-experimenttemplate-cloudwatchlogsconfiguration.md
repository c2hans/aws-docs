---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate CloudWatchLogsConfiguration
<a name="aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration"></a>

Specifies the configuration for experiment logging to CloudWatch Logs.

## Syntax
<a name="aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration-syntax.json"></a>

```
{
  "[LogGroupArn](#cfn-fis-experimenttemplate-cloudwatchlogsconfiguration-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration-syntax.yaml"></a>

```
  [LogGroupArn](#cfn-fis-experimenttemplate-cloudwatchlogsconfiguration-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration-properties"></a>

`LogGroupArn`  <a name="cfn-fis-experimenttemplate-cloudwatchlogsconfiguration-loggrouparn"></a>
The Amazon Resource Name (ARN) of the destination Amazon CloudWatch Logs log group.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
