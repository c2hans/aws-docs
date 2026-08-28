---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-transitionevent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel TransitionEvent
<a name="aws-properties-iotevents-detectormodel-transitionevent"></a>

Specifies the actions performed and the next state entered when a `condition` evaluates to TRUE.

## Syntax
<a name="aws-properties-iotevents-detectormodel-transitionevent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-transitionevent-syntax.json"></a>

```
{
  "[Actions](#cfn-iotevents-detectormodel-transitionevent-actions)" : {{[ Action, ... ]}},
  "[Condition](#cfn-iotevents-detectormodel-transitionevent-condition)" : {{String}},
  "[EventName](#cfn-iotevents-detectormodel-transitionevent-eventname)" : {{String}},
  "[NextState](#cfn-iotevents-detectormodel-transitionevent-nextstate)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-transitionevent-syntax.yaml"></a>

```
  [Actions](#cfn-iotevents-detectormodel-transitionevent-actions): {{
    - Action}}
  [Condition](#cfn-iotevents-detectormodel-transitionevent-condition): {{String}}
  [EventName](#cfn-iotevents-detectormodel-transitionevent-eventname): {{String}}
  [NextState](#cfn-iotevents-detectormodel-transitionevent-nextstate): {{String}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-transitionevent-properties"></a>

`Actions`  <a name="cfn-iotevents-detectormodel-transitionevent-actions"></a>
The actions to be performed.
*Required*: No
*Type*: Array of [Action](aws-properties-iotevents-detectormodel-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Condition`  <a name="cfn-iotevents-detectormodel-transitionevent-condition"></a>
Required. A Boolean expression that when TRUE causes the actions to be performed and the `nextState` to be entered.
*Required*: Yes
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventName`  <a name="cfn-iotevents-detectormodel-transitionevent-eventname"></a>
The name of the transition event.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NextState`  <a name="cfn-iotevents-detectormodel-transitionevent-nextstate"></a>
The next state to enter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
