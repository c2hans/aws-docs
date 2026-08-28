---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-workflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Workflow
<a name="aws-properties-arcregionswitch-plan-workflow"></a>

Represents a workflow in a Region switch plan. A workflow defines a sequence of steps to execute during a Region switch.

## Syntax
<a name="aws-properties-arcregionswitch-plan-workflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-workflow-syntax.json"></a>

```
{
  "[Steps](#cfn-arcregionswitch-plan-workflow-steps)" : {{[ Step, ... ]}},
  "[WorkflowDescription](#cfn-arcregionswitch-plan-workflow-workflowdescription)" : {{String}},
  "[WorkflowTargetAction](#cfn-arcregionswitch-plan-workflow-workflowtargetaction)" : {{String}},
  "[WorkflowTargetRegion](#cfn-arcregionswitch-plan-workflow-workflowtargetregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-workflow-syntax.yaml"></a>

```
  [Steps](#cfn-arcregionswitch-plan-workflow-steps): {{
    - Step}}
  [WorkflowDescription](#cfn-arcregionswitch-plan-workflow-workflowdescription): {{String}}
  [WorkflowTargetAction](#cfn-arcregionswitch-plan-workflow-workflowtargetaction): {{String}}
  [WorkflowTargetRegion](#cfn-arcregionswitch-plan-workflow-workflowtargetregion): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-workflow-properties"></a>

`Steps`  <a name="cfn-arcregionswitch-plan-workflow-steps"></a>
The steps that make up the workflow.
*Required*: No
*Type*: Array of [Step](aws-properties-arcregionswitch-plan-step.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowDescription`  <a name="cfn-arcregionswitch-plan-workflow-workflowdescription"></a>
The description of the workflow.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowTargetAction`  <a name="cfn-arcregionswitch-plan-workflow-workflowtargetaction"></a>
The action that the workflow performs. Valid values include `activate` and `deactivate`.
*Required*: Yes
*Type*: String
*Allowed values*: `activate | deactivate | postRecovery`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowTargetRegion`  <a name="cfn-arcregionswitch-plan-workflow-workflowtargetregion"></a>
The AWS Region that the workflow targets.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
