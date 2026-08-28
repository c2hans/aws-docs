---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-onenter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel OnEnter
<a name="aws-properties-iotevents-detectormodel-onenter"></a>

When entering this state, perform these `actions` if the `condition` is TRUE.

## Syntax
<a name="aws-properties-iotevents-detectormodel-onenter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-onenter-syntax.json"></a>

```
{
  "[Events](#cfn-iotevents-detectormodel-onenter-events)" : {{[ Event, ... ]}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-onenter-syntax.yaml"></a>

```
  [Events](#cfn-iotevents-detectormodel-onenter-events): {{
    - Event}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-onenter-properties"></a>

`Events`  <a name="cfn-iotevents-detectormodel-onenter-events"></a>
Specifies the actions that are performed when the state is entered and the `condition` is `TRUE`.
*Required*: No
*Type*: Array of [Event](aws-properties-iotevents-detectormodel-event.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
