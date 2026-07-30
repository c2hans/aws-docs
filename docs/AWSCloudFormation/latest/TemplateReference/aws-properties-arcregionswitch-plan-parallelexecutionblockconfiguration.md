---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan ParallelExecutionBlockConfiguration
<a name="aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration"></a>

Configuration for steps that should be executed in parallel during a Region switch.

## Syntax
<a name="aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration-syntax.json"></a>

```
{
  "[Steps](#cfn-arcregionswitch-plan-parallelexecutionblockconfiguration-steps)" : {{[ Step, ... ]}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration-syntax.yaml"></a>

```
  [Steps](#cfn-arcregionswitch-plan-parallelexecutionblockconfiguration-steps): {{
    - Step}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration-properties"></a>

`Steps`  <a name="cfn-arcregionswitch-plan-parallelexecutionblockconfiguration-steps"></a>
The steps for a parallel execution block.
*Required*: Yes
*Type*: Array of [Step](aws-properties-arcregionswitch-plan-step.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
