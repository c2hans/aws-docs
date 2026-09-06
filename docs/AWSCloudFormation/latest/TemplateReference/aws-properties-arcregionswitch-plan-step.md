---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-step.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Step
<a name="aws-properties-arcregionswitch-plan-step"></a>

Represents a step in a Region switch plan workflow. Each step performs a specific action during the Region switch process.

## Syntax
<a name="aws-properties-arcregionswitch-plan-step-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-step-syntax.json"></a>

```
{
  "[Description](#cfn-arcregionswitch-plan-step-description)" : {{String}},
  "[ExecutionBlockConfiguration](#cfn-arcregionswitch-plan-step-executionblockconfiguration)" : {{ExecutionBlockConfiguration}},
  "[ExecutionBlockType](#cfn-arcregionswitch-plan-step-executionblocktype)" : {{String}},
  "[Name](#cfn-arcregionswitch-plan-step-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-step-syntax.yaml"></a>

```
  [Description](#cfn-arcregionswitch-plan-step-description): {{String}}
  [ExecutionBlockConfiguration](#cfn-arcregionswitch-plan-step-executionblockconfiguration): {{
    ExecutionBlockConfiguration}}
  [ExecutionBlockType](#cfn-arcregionswitch-plan-step-executionblocktype): {{String}}
  [Name](#cfn-arcregionswitch-plan-step-name): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-step-properties"></a>

`Description`  <a name="cfn-arcregionswitch-plan-step-description"></a>
The description of a step in a workflow.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionBlockConfiguration`  <a name="cfn-arcregionswitch-plan-step-executionblockconfiguration"></a>
The configuration for an execution block in a workflow.
*Required*: Yes
*Type*: [ExecutionBlockConfiguration](aws-properties-arcregionswitch-plan-executionblockconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionBlockType`  <a name="cfn-arcregionswitch-plan-step-executionblocktype"></a>
The type of an execution block in a workflow.
*Required*: Yes
*Type*: String
*Allowed values*: `ARCRegionSwitchPlan | ARCRoutingControl | AuroraGlobalDatabase | AuroraProvisionedScaling | AuroraServerlessScaling | CustomActionLambda | DocumentDb | EC2AutoScaling | ECSServiceScaling | EKSResourceScaling | LambdaEventSourceMapping | ManualApproval | NeptuneGlobalDatabase | Parallel | RdsCreateCrossRegionReplica | RdsPromoteReadReplica | RdsSwitchoverReadReplica | Route53HealthCheck`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-arcregionswitch-plan-step-name"></a>
The name of a step in a workflow.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
