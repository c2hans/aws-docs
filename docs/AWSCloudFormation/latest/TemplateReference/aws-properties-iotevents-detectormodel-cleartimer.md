---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-cleartimer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel ClearTimer
<a name="aws-properties-iotevents-detectormodel-cleartimer"></a>

Information needed to clear the timer.

## Syntax
<a name="aws-properties-iotevents-detectormodel-cleartimer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-cleartimer-syntax.json"></a>

```
{
  "[TimerName](#cfn-iotevents-detectormodel-cleartimer-timername)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-cleartimer-syntax.yaml"></a>

```
  [TimerName](#cfn-iotevents-detectormodel-cleartimer-timername): {{String}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-cleartimer-properties"></a>

`TimerName`  <a name="cfn-iotevents-detectormodel-cleartimer-timername"></a>
The name of the timer to clear.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
