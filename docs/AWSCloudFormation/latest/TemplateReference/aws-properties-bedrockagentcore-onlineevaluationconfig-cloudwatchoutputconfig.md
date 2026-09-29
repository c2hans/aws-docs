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
  "[LogGroupName](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname)" : {{String}},
  "[MetricsNamespace](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-metricsnamespace)" : {{String}},
  "[ResultDestination](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-resultdestination)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-syntax.yaml"></a>

```
  [LogGroupName](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname): {{String}}
  [MetricsNamespace](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-metricsnamespace): {{String}}
  [ResultDestination](#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-resultdestination): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-properties"></a>

`LogGroupName`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname"></a>
 The name of the CloudWatch log group where evaluation results will be written. The log group will be created if it doesn't exist.
*Required*: No
*Type*: String
*Pattern*: `^[.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricsNamespace`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-metricsnamespace"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._#/:-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultDestination`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-resultdestination"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `DEDICATED_LOG_GROUP | SOURCE_LOG_GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
