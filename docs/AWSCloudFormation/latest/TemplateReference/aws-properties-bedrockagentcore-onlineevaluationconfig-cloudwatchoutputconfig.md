---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig CloudWatchOutputConfig
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig"></a>

 The CloudWatch configuration for writing evaluation results to CloudWatch logs with embedded metric format.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-syntax.yaml"></a>

```
  [LogGroupName](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-properties"></a>

`LogGroupName`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname"></a>
 The name of the CloudWatch log group where evaluation results will be written. The log group will be created if it doesn't exist.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
