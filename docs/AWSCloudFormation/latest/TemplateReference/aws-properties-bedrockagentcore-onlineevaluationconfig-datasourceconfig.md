---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig DataSourceConfig
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig"></a>

 The data source configuration specifying CloudWatch log groups and service names to monitor.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig-cloudwatchlogs)" : {{CloudWatchLogsInputConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig-cloudwatchlogs): {{
    CloudWatchLogsInputConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig-properties"></a>

`CloudWatchLogs`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig-cloudwatchlogs"></a>
 The CloudWatch logs configuration for reading agent traces from log groups.
*Required*: Yes
*Type*: [CloudWatchLogsInputConfig](aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
