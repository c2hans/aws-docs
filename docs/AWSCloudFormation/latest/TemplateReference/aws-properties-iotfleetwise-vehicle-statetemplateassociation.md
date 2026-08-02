---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-vehicle-statetemplateassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Vehicle StateTemplateAssociation
<a name="aws-properties-iotfleetwise-vehicle-statetemplateassociation"></a>

The state template associated with a vehicle. State templates contain state properties, which are signals that belong to a signal catalog that is synchronized between the AWS IoT FleetWise Edge and the AWS Cloud.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-vehicle-statetemplateassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-vehicle-statetemplateassociation-syntax.json"></a>

```
{
  "[Identifier](#cfn-iotfleetwise-vehicle-statetemplateassociation-identifier)" : {{String}},
  "[StateTemplateUpdateStrategy](#cfn-iotfleetwise-vehicle-statetemplateassociation-statetemplateupdatestrategy)" : {{StateTemplateUpdateStrategy}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-vehicle-statetemplateassociation-syntax.yaml"></a>

```
  [Identifier](#cfn-iotfleetwise-vehicle-statetemplateassociation-identifier): {{String}}
  [StateTemplateUpdateStrategy](#cfn-iotfleetwise-vehicle-statetemplateassociation-statetemplateupdatestrategy): {{
    StateTemplateUpdateStrategy}}
```

## Properties
<a name="aws-properties-iotfleetwise-vehicle-statetemplateassociation-properties"></a>

`Identifier`  <a name="cfn-iotfleetwise-vehicle-statetemplateassociation-identifier"></a>
The unique ID of the state template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StateTemplateUpdateStrategy`  <a name="cfn-iotfleetwise-vehicle-statetemplateassociation-statetemplateupdatestrategy"></a>
Property description not available.
*Required*: Yes
*Type*: [StateTemplateUpdateStrategy](aws-properties-iotfleetwise-vehicle-statetemplateupdatestrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
