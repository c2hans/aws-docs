---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-event.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel Event
<a name="aws-properties-iotevents-detectormodel-event"></a>

Specifies the `actions` to be performed when the `condition` evaluates to TRUE.

## Syntax
<a name="aws-properties-iotevents-detectormodel-event-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-event-syntax.json"></a>

```
{
  "[Actions](#cfn-iotevents-detectormodel-event-actions)" : {{[ Action, ... ]}},
  "[Condition](#cfn-iotevents-detectormodel-event-condition)" : {{String}},
  "[EventName](#cfn-iotevents-detectormodel-event-eventname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-event-syntax.yaml"></a>

```
  [Actions](#cfn-iotevents-detectormodel-event-actions): {{
    - Action}}
  [Condition](#cfn-iotevents-detectormodel-event-condition): {{String}}
  [EventName](#cfn-iotevents-detectormodel-event-eventname): {{String}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-event-properties"></a>

`Actions`  <a name="cfn-iotevents-detectormodel-event-actions"></a>
The actions to be performed.
*Required*: No
*Type*: Array of [Action](aws-properties-iotevents-detectormodel-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Condition`  <a name="cfn-iotevents-detectormodel-event-condition"></a>
Optional. The Boolean expression that, when TRUE, causes the `actions` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventName`  <a name="cfn-iotevents-detectormodel-event-eventname"></a>
The name of the event.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
