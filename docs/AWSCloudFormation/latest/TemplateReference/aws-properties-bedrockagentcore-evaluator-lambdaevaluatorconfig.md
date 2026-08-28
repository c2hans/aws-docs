---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator LambdaEvaluatorConfig
<a name="aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig"></a>

<a name="aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig-description"></a>The `LambdaEvaluatorConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Evaluator](aws-resource-bedrockagentcore-evaluator.md).

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig-syntax.json"></a>

```
{
  "[LambdaArn](#cfn-bedrockagentcore-evaluator-lambdaevaluatorconfig-lambdaarn)" : {{String}},
  "[LambdaTimeoutInSeconds](#cfn-bedrockagentcore-evaluator-lambdaevaluatorconfig-lambdatimeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig-syntax.yaml"></a>

```
  [LambdaArn](#cfn-bedrockagentcore-evaluator-lambdaevaluatorconfig-lambdaarn): {{String}}
  [LambdaTimeoutInSeconds](#cfn-bedrockagentcore-evaluator-lambdaevaluatorconfig-lambdatimeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-lambdaevaluatorconfig-properties"></a>

`LambdaArn`  <a name="cfn-bedrockagentcore-evaluator-lambdaevaluatorconfig-lambdaarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaTimeoutInSeconds`  <a name="cfn-bedrockagentcore-evaluator-lambdaevaluatorconfig-lambdatimeoutinseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
