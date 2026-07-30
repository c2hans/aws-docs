---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig CloudWatchLogsInputConfig
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig"></a>

 The CloudWatch logs configuration for reading agent traces from log groups.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-syntax.json"></a>

```
{
  "[LogGroupNames](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-loggroupnames)" : {{[ String, ... ]}},
  "[ServiceNames](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-servicenames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-syntax.yaml"></a>

```
  [LogGroupNames](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-loggroupnames): {{
    - String}}
  [ServiceNames](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-servicenames): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-properties"></a>

`LogGroupNames`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-loggroupnames"></a>
 The list of CloudWatch log group names to monitor for agent traces.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `512 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNames`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-servicenames"></a>
 The list of service names to filter traces within the specified log groups. Used to identify relevant agent sessions.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
