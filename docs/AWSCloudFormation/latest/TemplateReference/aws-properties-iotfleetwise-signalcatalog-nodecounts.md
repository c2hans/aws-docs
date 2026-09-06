---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-signalcatalog-nodecounts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::SignalCatalog NodeCounts
<a name="aws-properties-iotfleetwise-signalcatalog-nodecounts"></a>

Information about the number of nodes and node types in a vehicle network.

## Syntax
<a name="aws-properties-iotfleetwise-signalcatalog-nodecounts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-signalcatalog-nodecounts-syntax.json"></a>

```
{
  "[TotalActuators](#cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators)" : {{Number}},
  "[TotalAttributes](#cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes)" : {{Number}},
  "[TotalBranches](#cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches)" : {{Number}},
  "[TotalNodes](#cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes)" : {{Number}},
  "[TotalSensors](#cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors)" : {{Number}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-signalcatalog-nodecounts-syntax.yaml"></a>

```
  [TotalActuators](#cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators): {{Number}}
  [TotalAttributes](#cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes): {{Number}}
  [TotalBranches](#cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches): {{Number}}
  [TotalNodes](#cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes): {{Number}}
  [TotalSensors](#cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors): {{Number}}
```

## Properties
<a name="aws-properties-iotfleetwise-signalcatalog-nodecounts-properties"></a>

`TotalActuators`  <a name="cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators"></a>
 The total number of nodes in a vehicle network that represent actuators.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAttributes`  <a name="cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes"></a>
 The total number of nodes in a vehicle network that represent attributes.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalBranches`  <a name="cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches"></a>
 The total number of nodes in a vehicle network that represent branches.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalNodes`  <a name="cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes"></a>
 The total number of nodes in a vehicle network.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalSensors`  <a name="cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors"></a>
 The total number of nodes in a vehicle network that represent sensors.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
