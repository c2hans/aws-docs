---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-loopcontrollerflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow LoopControllerFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-loopcontrollerflownodeconfiguration"></a>

Contains configurations for the controller node of a DoWhile loop in the flow.

## Syntax
<a name="aws-properties-bedrock-flow-loopcontrollerflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-loopcontrollerflownodeconfiguration-syntax.json"></a>

```
{
  "[ContinueCondition](#cfn-bedrock-flow-loopcontrollerflownodeconfiguration-continuecondition)" : {{FlowCondition}},
  "[MaxIterations](#cfn-bedrock-flow-loopcontrollerflownodeconfiguration-maxiterations)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-loopcontrollerflownodeconfiguration-syntax.yaml"></a>

```
  [ContinueCondition](#cfn-bedrock-flow-loopcontrollerflownodeconfiguration-continuecondition): {{
    FlowCondition}}
  [MaxIterations](#cfn-bedrock-flow-loopcontrollerflownodeconfiguration-maxiterations): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-flow-loopcontrollerflownodeconfiguration-properties"></a>

`ContinueCondition`  <a name="cfn-bedrock-flow-loopcontrollerflownodeconfiguration-continuecondition"></a>
Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.
*Required*: Yes
*Type*: [FlowCondition](aws-properties-bedrock-flow-flowcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxIterations`  <a name="cfn-bedrock-flow-loopcontrollerflownodeconfiguration-maxiterations"></a>
Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
