---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotfleetwise-fleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Fleet
<a name="aws-resource-iotfleetwise-fleet"></a>

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Creates a fleet that represents a group of vehicles.

**Note**
You must create both a signal catalog and vehicles before you can create a fleet.

For more information, see [Fleets](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html) in the *AWS IoT FleetWise Developer Guide*.

## Syntax
<a name="aws-resource-iotfleetwise-fleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotfleetwise-fleet-syntax.json"></a>

```
{
  "Type" : "AWS::IoTFleetWise::Fleet",
  "Properties" : {
      "[Description](#cfn-iotfleetwise-fleet-description)" : {{String}},
      "[Id](#cfn-iotfleetwise-fleet-id)" : {{String}},
      "[SignalCatalogArn](#cfn-iotfleetwise-fleet-signalcatalogarn)" : {{String}},
      "[Tags](#cfn-iotfleetwise-fleet-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotfleetwise-fleet-syntax.yaml"></a>

```
Type: AWS::IoTFleetWise::Fleet
Properties:
  [Description](#cfn-iotfleetwise-fleet-description): {{String}}
  [Id](#cfn-iotfleetwise-fleet-id): {{String}}
  [SignalCatalogArn](#cfn-iotfleetwise-fleet-signalcatalogarn): {{String}}
  [Tags](#cfn-iotfleetwise-fleet-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotfleetwise-fleet-properties"></a>

`Description`  <a name="cfn-iotfleetwise-fleet-description"></a>
 A brief description of the fleet.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotfleetwise-fleet-id"></a>
The unique ID of the fleet.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SignalCatalogArn`  <a name="cfn-iotfleetwise-fleet-signalcatalogarn"></a>
The ARN of the signal catalog associated with the fleet.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotfleetwise-fleet-tags"></a>
 Metadata that can be used to manage the fleet.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotfleetwise-fleet-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotfleetwise-fleet-return-values"></a>

### Ref
<a name="aws-resource-iotfleetwise-fleet-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Id.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iotfleetwise-fleet-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotfleetwise-fleet-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the created fleet.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
 The time the fleet was created in seconds since epoch (January 1, 1970 at midnight UTC time).

`LastModificationTime`  <a name="LastModificationTime-fn::getatt"></a>
 The time the fleet was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).
