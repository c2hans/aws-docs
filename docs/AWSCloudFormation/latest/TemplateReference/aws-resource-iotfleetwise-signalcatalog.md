---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotfleetwise-signalcatalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::SignalCatalog
<a name="aws-resource-iotfleetwise-signalcatalog"></a>

Creates a collection of standardized signals that can be reused to create vehicle models.

For more information, see [Signal catalogs](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/signal-catalogs.html) in the *AWS IoT FleetWise Developer Guide*.

## Syntax
<a name="aws-resource-iotfleetwise-signalcatalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotfleetwise-signalcatalog-syntax.json"></a>

```
{
  "Type" : "AWS::IoTFleetWise::SignalCatalog",
  "Properties" : {
      "[Description](#cfn-iotfleetwise-signalcatalog-description)" : {{String}},
      "[Name](#cfn-iotfleetwise-signalcatalog-name)" : {{String}},
      "[NodeCounts](#cfn-iotfleetwise-signalcatalog-nodecounts)" : {{NodeCounts}},
      "[Nodes](#cfn-iotfleetwise-signalcatalog-nodes)" : {{[ Node, ... ]}},
      "[Tags](#cfn-iotfleetwise-signalcatalog-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotfleetwise-signalcatalog-syntax.yaml"></a>

```
Type: AWS::IoTFleetWise::SignalCatalog
Properties:
  [Description](#cfn-iotfleetwise-signalcatalog-description): {{String}}
  [Name](#cfn-iotfleetwise-signalcatalog-name): {{String}}
  [NodeCounts](#cfn-iotfleetwise-signalcatalog-nodecounts): {{
    NodeCounts}}
  [Nodes](#cfn-iotfleetwise-signalcatalog-nodes): {{
    - Node}}
  [Tags](#cfn-iotfleetwise-signalcatalog-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotfleetwise-signalcatalog-properties"></a>

`Description`  <a name="cfn-iotfleetwise-signalcatalog-description"></a>
 A brief description of the signal catalog.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotfleetwise-signalcatalog-name"></a>
 The name of the signal catalog.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z\d\-_:]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NodeCounts`  <a name="cfn-iotfleetwise-signalcatalog-nodecounts"></a>
 Information about the number of nodes and node types in a vehicle network.
*Required*: No
*Type*: [NodeCounts](aws-properties-iotfleetwise-signalcatalog-nodecounts.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Nodes`  <a name="cfn-iotfleetwise-signalcatalog-nodes"></a>
 A list of information about nodes, which are a general abstraction of signals.
*Required*: No
*Type*: Array of [Node](aws-properties-iotfleetwise-signalcatalog-node.md)
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotfleetwise-signalcatalog-tags"></a>
 Metadata that can be used to manage the signal catalog.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotfleetwise-signalcatalog-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotfleetwise-signalcatalog-return-values"></a>

### Ref
<a name="aws-resource-iotfleetwise-signalcatalog-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iotfleetwise-signalcatalog-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotfleetwise-signalcatalog-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the signal catalog.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time).

`LastModificationTime`  <a name="LastModificationTime-fn::getatt"></a>
The time the signal catalog was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).

`NodeCounts.TotalActuators`  <a name="NodeCounts.TotalActuators-fn::getatt"></a>
The total number of nodes in a vehicle network that represent actuators.

`NodeCounts.TotalAttributes`  <a name="NodeCounts.TotalAttributes-fn::getatt"></a>
The total number of nodes in a vehicle network that represent attributes.

`NodeCounts.TotalBranches`  <a name="NodeCounts.TotalBranches-fn::getatt"></a>
The total number of nodes in a vehicle network that represent branches.

`NodeCounts.TotalNodes`  <a name="NodeCounts.TotalNodes-fn::getatt"></a>
The total number of nodes in a vehicle network.

`NodeCounts.TotalSensors`  <a name="NodeCounts.TotalSensors-fn::getatt"></a>
The total number of nodes in a vehicle network that represent sensors.
