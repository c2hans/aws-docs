---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion LoopControllerFlowNodeConfiguration
<a name="aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration"></a>

Contains configurations for the controller node of a DoWhile loop in the flow.

## Syntax
<a name="aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration-syntax.json"></a>

```
{
  "[ContinueCondition](#cfn-bedrock-flowversion-loopcontrollerflownodeconfiguration-continuecondition)" : {{FlowCondition}},
  "[MaxIterations](#cfn-bedrock-flowversion-loopcontrollerflownodeconfiguration-maxiterations)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration-syntax.yaml"></a>

```
  [ContinueCondition](#cfn-bedrock-flowversion-loopcontrollerflownodeconfiguration-continuecondition): {{
    FlowCondition}}
  [MaxIterations](#cfn-bedrock-flowversion-loopcontrollerflownodeconfiguration-maxiterations): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-loopcontrollerflownodeconfiguration-properties"></a>

`ContinueCondition`  <a name="cfn-bedrock-flowversion-loopcontrollerflownodeconfiguration-continuecondition"></a>
Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.
*Required*: Yes
*Type*: [FlowCondition](aws-properties-bedrock-flowversion-flowcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxIterations`  <a name="cfn-bedrock-flowversion-loopcontrollerflownodeconfiguration-maxiterations"></a>
Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
