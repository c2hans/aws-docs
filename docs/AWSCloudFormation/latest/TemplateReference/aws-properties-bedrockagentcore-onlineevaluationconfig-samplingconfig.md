---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig SamplingConfig
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig"></a>

 The sampling configuration that determines what percentage of agent traces to evaluate.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig-syntax.json"></a>

```
{
  "[SamplingPercentage](#cfn-bedrockagentcore-onlineevaluationconfig-samplingconfig-samplingpercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig-syntax.yaml"></a>

```
  [SamplingPercentage](#cfn-bedrockagentcore-onlineevaluationconfig-samplingconfig-samplingpercentage): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig-properties"></a>

`SamplingPercentage`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-samplingconfig-samplingpercentage"></a>
 The percentage of agent traces to sample for evaluation, ranging from 0.01% to 100%.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
