---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Vehicle StateTemplateUpdateStrategy
<a name="aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy"></a>

The update strategy for the state template. Vehicles associated with the state template can stream telemetry data with either an `onChange` or `periodic` update strategy.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy-syntax.json"></a>

```
{
  "[OnChange](#cfn-iotfleetwise-vehicle-statetemplateupdatestrategy-onchange)" : {{Json}},
  "[Periodic](#cfn-iotfleetwise-vehicle-statetemplateupdatestrategy-periodic)" : {{PeriodicStateTemplateUpdateStrategy}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy-syntax.yaml"></a>

```
  [OnChange](#cfn-iotfleetwise-vehicle-statetemplateupdatestrategy-onchange): {{Json}}
  [Periodic](#cfn-iotfleetwise-vehicle-statetemplateupdatestrategy-periodic): {{
    PeriodicStateTemplateUpdateStrategy}}
```

## Properties
<a name="aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy-properties"></a>

`OnChange`  <a name="cfn-iotfleetwise-vehicle-statetemplateupdatestrategy-onchange"></a>
Property description not available.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Periodic`  <a name="cfn-iotfleetwise-vehicle-statetemplateupdatestrategy-periodic"></a>
Property description not available.
*Required*: No
*Type*: [PeriodicStateTemplateUpdateStrategy](aws-properties-iotfleetwise-vehicle-periodicstatetemplateupdatestrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
