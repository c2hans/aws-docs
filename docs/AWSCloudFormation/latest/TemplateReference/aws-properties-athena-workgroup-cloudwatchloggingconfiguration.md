---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-cloudwatchloggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup CloudWatchLoggingConfiguration
<a name="aws-properties-athena-workgroup-cloudwatchloggingconfiguration"></a>

Configuration settings for delivering logs to Amazon CloudWatch log groups.

## Syntax
<a name="aws-properties-athena-workgroup-cloudwatchloggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-cloudwatchloggingconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-athena-workgroup-cloudwatchloggingconfiguration-enabled)" : {{Boolean}},
  "[LogGroup](#cfn-athena-workgroup-cloudwatchloggingconfiguration-loggroup)" : {{String}},
  "[LogStreamNamePrefix](#cfn-athena-workgroup-cloudwatchloggingconfiguration-logstreamnameprefix)" : {{String}},
  "[LogTypes](#cfn-athena-workgroup-cloudwatchloggingconfiguration-logtypes)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-cloudwatchloggingconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-athena-workgroup-cloudwatchloggingconfiguration-enabled): {{Boolean}}
  [LogGroup](#cfn-athena-workgroup-cloudwatchloggingconfiguration-loggroup): {{String}}
  [LogStreamNamePrefix](#cfn-athena-workgroup-cloudwatchloggingconfiguration-logstreamnameprefix): {{String}}
  [LogTypes](#cfn-athena-workgroup-cloudwatchloggingconfiguration-logtypes): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-athena-workgroup-cloudwatchloggingconfiguration-properties"></a>

`Enabled`  <a name="cfn-athena-workgroup-cloudwatchloggingconfiguration-enabled"></a>
Enables CloudWatch logging.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroup`  <a name="cfn-athena-workgroup-cloudwatchloggingconfiguration-loggroup"></a>
The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._/-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogStreamNamePrefix`  <a name="cfn-athena-workgroup-cloudwatchloggingconfiguration-logstreamnameprefix"></a>
Prefix for the CloudWatch log stream name.
*Required*: No
*Type*: String
*Pattern*: `^[^:*]*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogTypes`  <a name="cfn-athena-workgroup-cloudwatchloggingconfiguration-logtypes"></a>
The types of logs that you want to publish to CloudWatch.
*Required*: No
*Type*: Object of Array
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
