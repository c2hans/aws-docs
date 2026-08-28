---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-signalfetchconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign SignalFetchConfig
<a name="aws-properties-iotfleetwise-campaign-signalfetchconfig"></a>

The configuration of the signal fetch operation.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-signalfetchconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-signalfetchconfig-syntax.json"></a>

```
{
  "[ConditionBased](#cfn-iotfleetwise-campaign-signalfetchconfig-conditionbased)" : {{ConditionBasedSignalFetchConfig}},
  "[TimeBased](#cfn-iotfleetwise-campaign-signalfetchconfig-timebased)" : {{TimeBasedSignalFetchConfig}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-signalfetchconfig-syntax.yaml"></a>

```
  [ConditionBased](#cfn-iotfleetwise-campaign-signalfetchconfig-conditionbased): {{
    ConditionBasedSignalFetchConfig}}
  [TimeBased](#cfn-iotfleetwise-campaign-signalfetchconfig-timebased): {{
    TimeBasedSignalFetchConfig}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-signalfetchconfig-properties"></a>

`ConditionBased`  <a name="cfn-iotfleetwise-campaign-signalfetchconfig-conditionbased"></a>
The configuration of a condition-based signal fetch operation.
*Required*: No
*Type*: [ConditionBasedSignalFetchConfig](aws-properties-iotfleetwise-campaign-conditionbasedsignalfetchconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeBased`  <a name="cfn-iotfleetwise-campaign-signalfetchconfig-timebased"></a>
The configuration of a time-based signal fetch operation.
*Required*: No
*Type*: [TimeBasedSignalFetchConfig](aws-properties-iotfleetwise-campaign-timebasedsignalfetchconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
