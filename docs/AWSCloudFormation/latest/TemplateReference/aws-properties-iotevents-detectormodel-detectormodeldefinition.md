---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-detectormodeldefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel DetectorModelDefinition
<a name="aws-properties-iotevents-detectormodel-detectormodeldefinition"></a>

Information that defines how a detector operates.

## Syntax
<a name="aws-properties-iotevents-detectormodel-detectormodeldefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-detectormodeldefinition-syntax.json"></a>

```
{
  "[InitialStateName](#cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename)" : {{String}},
  "[States](#cfn-iotevents-detectormodel-detectormodeldefinition-states)" : {{[ State, ... ]}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-detectormodeldefinition-syntax.yaml"></a>

```
  [InitialStateName](#cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename): {{String}}
  [States](#cfn-iotevents-detectormodel-detectormodeldefinition-states): {{
    - State}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-detectormodeldefinition-properties"></a>

`InitialStateName`  <a name="cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename"></a>
The state that is entered at the creation of each detector (instance).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`States`  <a name="cfn-iotevents-detectormodel-detectormodeldefinition-states"></a>
Information about the states of the detector.
*Required*: Yes
*Type*: Array of [State](aws-properties-iotevents-detectormodel-state.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
