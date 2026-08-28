---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-detectormodel-resettimer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::DetectorModel ResetTimer
<a name="aws-properties-iotevents-detectormodel-resettimer"></a>

Information required to reset the timer. The timer is reset to the previously evaluated result of the duration. The duration expression isn't reevaluated when you reset the timer.

## Syntax
<a name="aws-properties-iotevents-detectormodel-resettimer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-detectormodel-resettimer-syntax.json"></a>

```
{
  "[TimerName](#cfn-iotevents-detectormodel-resettimer-timername)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotevents-detectormodel-resettimer-syntax.yaml"></a>

```
  [TimerName](#cfn-iotevents-detectormodel-resettimer-timername): {{String}}
```

## Properties
<a name="aws-properties-iotevents-detectormodel-resettimer-properties"></a>

`TimerName`  <a name="cfn-iotevents-detectormodel-resettimer-timername"></a>
The name of the timer to reset.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
