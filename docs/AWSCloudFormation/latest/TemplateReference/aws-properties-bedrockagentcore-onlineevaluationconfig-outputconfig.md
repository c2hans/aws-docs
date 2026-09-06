---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig OutputConfig
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig"></a>

 The output configuration specifying where evaluation results are written.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig-syntax.json"></a>

```
{
  "[CloudWatchConfig](#cfn-bedrockagentcore-onlineevaluationconfig-outputconfig-cloudwatchconfig)" : {{CloudWatchOutputConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig-syntax.yaml"></a>

```
  [CloudWatchConfig](#cfn-bedrockagentcore-onlineevaluationconfig-outputconfig-cloudwatchconfig): {{
    CloudWatchOutputConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig-properties"></a>

`CloudWatchConfig`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-outputconfig-cloudwatchconfig"></a>
 The CloudWatch configuration for writing evaluation results to CloudWatch logs with embedded metric format.
*Required*: No
*Type*: [CloudWatchOutputConfig](aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
