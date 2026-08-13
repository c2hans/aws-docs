---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-onlineevaluationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig"></a>

Specifies an online evaluation configuration for Amazon Bedrock AgentCore. An online evaluation configuration enables continuous monitoring and assessment of agent performance in production.

For more information, see [Monitor agent performance with Amazon Bedrock AgentCore online evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/online-evaluation.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::OnlineEvaluationConfig",
  "Properties" : {
      "[ClusteringConfig](#cfn-bedrockagentcore-onlineevaluationconfig-clusteringconfig)" : {{ClusteringConfig}},
      "[DataSourceConfig](#cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig)" : {{DataSourceConfig}},
      "[Description](#cfn-bedrockagentcore-onlineevaluationconfig-description)" : {{String}},
      "[EvaluationExecutionRoleArn](#cfn-bedrockagentcore-onlineevaluationconfig-evaluationexecutionrolearn)" : {{String}},
      "[Evaluators](#cfn-bedrockagentcore-onlineevaluationconfig-evaluators)" : {{[ EvaluatorReference, ... ]}},
      "[ExecutionStatus](#cfn-bedrockagentcore-onlineevaluationconfig-executionstatus)" : {{String}},
      "[Insights](#cfn-bedrockagentcore-onlineevaluationconfig-insights)" : {{[ Insight, ... ]}},
      "[OnlineEvaluationConfigName](#cfn-bedrockagentcore-onlineevaluationconfig-onlineevaluationconfigname)" : {{String}},
      "[Rule](#cfn-bedrockagentcore-onlineevaluationconfig-rule)" : {{Rule}},
      "[Tags](#cfn-bedrockagentcore-onlineevaluationconfig-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::OnlineEvaluationConfig
Properties:
  [ClusteringConfig](#cfn-bedrockagentcore-onlineevaluationconfig-clusteringconfig): {{
    ClusteringConfig}}
  [DataSourceConfig](#cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig): {{
    DataSourceConfig}}
  [Description](#cfn-bedrockagentcore-onlineevaluationconfig-description): {{String}}
  [EvaluationExecutionRoleArn](#cfn-bedrockagentcore-onlineevaluationconfig-evaluationexecutionrolearn): {{String}}
  [Evaluators](#cfn-bedrockagentcore-onlineevaluationconfig-evaluators): {{
    - EvaluatorReference}}
  [ExecutionStatus](#cfn-bedrockagentcore-onlineevaluationconfig-executionstatus): {{String}}
  [Insights](#cfn-bedrockagentcore-onlineevaluationconfig-insights): {{
    - Insight}}
  [OnlineEvaluationConfigName](#cfn-bedrockagentcore-onlineevaluationconfig-onlineevaluationconfigname): {{String}}
  [Rule](#cfn-bedrockagentcore-onlineevaluationconfig-rule): {{
    Rule}}
  [Tags](#cfn-bedrockagentcore-onlineevaluationconfig-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-properties"></a>

`ClusteringConfig`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-clusteringconfig"></a>
The clustering configuration for periodic batch evaluation.
*Required*: No
*Type*: [ClusteringConfig](aws-properties-bedrockagentcore-onlineevaluationconfig-clusteringconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceConfig`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig"></a>
 The data source configuration specifying CloudWatch log groups and service names to monitor.
*Required*: Yes
*Type*: [DataSourceConfig](aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-description"></a>
 The description of the online evaluation configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationExecutionRoleArn`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-evaluationexecutionrolearn"></a>
 The Amazon Resource Name (ARN) of the IAM role used for evaluation execution.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Evaluators`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-evaluators"></a>
 The list of evaluators applied during online evaluation.
*Required*: No
*Type*: Array of [EvaluatorReference](aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionStatus`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-executionstatus"></a>
 The execution status indicating whether the online evaluation is currently running.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Insights`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-insights"></a>
The list of insight types configured for this evaluation.
*Required*: No
*Type*: Array of [Insight](aws-properties-bedrockagentcore-onlineevaluationconfig-insight.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnlineEvaluationConfigName`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-onlineevaluationconfigname"></a>
 The name of the online evaluation configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Rule`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-rule"></a>
 The evaluation rule containing sampling configuration, filters, and session settings.
*Required*: Yes
*Type*: [Rule](aws-properties-bedrockagentcore-onlineevaluationconfig-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-tags"></a>
The tags for the online evaluation configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-onlineevaluationconfig-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the online evaluation configuration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-onlineevaluationconfig-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the online evaluation configuration was created.

`OnlineEvaluationConfigArn`  <a name="OnlineEvaluationConfigArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the online evaluation configuration.

`OnlineEvaluationConfigId`  <a name="OnlineEvaluationConfigId-fn::getatt"></a>
The unique identifier of the online evaluation configuration.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the online evaluation configuration.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the online evaluation configuration was last updated.
