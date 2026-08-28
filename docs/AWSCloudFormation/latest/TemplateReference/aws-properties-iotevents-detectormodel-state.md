---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-state.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel State
<a name="aws-properties-iotevents-detectormodel-state"></a>

Information that defines a state of a detector.

## Syntax
<a name="aws-properties-iotevents-detectormodel-state-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-state-syntax.json"></a>

```
{
  "[OnEnter](#cfn-iotevents-detectormodel-state-onenter)" : {{OnEnter}},
  "[OnExit](#cfn-iotevents-detectormodel-state-onexit)" : {{OnExit}},
  "[OnInput](#cfn-iotevents-detectormodel-state-oninput)" : {{OnInput}},
  "[StateName](#cfn-iotevents-detectormodel-state-statename)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-state-syntax.yaml"></a>

```
  [OnEnter](#cfn-iotevents-detectormodel-state-onenter): {{
    OnEnter}}
  [OnExit](#cfn-iotevents-detectormodel-state-onexit): {{
    OnExit}}
  [OnInput](#cfn-iotevents-detectormodel-state-oninput): {{
    OnInput}}
  [StateName](#cfn-iotevents-detectormodel-state-statename): {{String}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-state-properties"></a>

`OnEnter`  <a name="cfn-iotevents-detectormodel-state-onenter"></a>
When entering this state, perform these `actions` if the `condition` is TRUE.
*Required*: No
*Type*: [OnEnter](aws-properties-iotevents-detectormodel-onenter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnExit`  <a name="cfn-iotevents-detectormodel-state-onexit"></a>
When exiting this state, perform these `actions` if the specified `condition` is `TRUE`.
*Required*: No
*Type*: [OnExit](aws-properties-iotevents-detectormodel-onexit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnInput`  <a name="cfn-iotevents-detectormodel-state-oninput"></a>
When an input is received and the `condition` is TRUE, perform the specified `actions`.
*Required*: No
*Type*: [OnInput](aws-properties-iotevents-detectormodel-oninput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StateName`  <a name="cfn-iotevents-detectormodel-state-statename"></a>
The name of the state.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
