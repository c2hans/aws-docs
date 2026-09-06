---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-aggregateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume AggregateConfiguration
<a name="aws-properties-fsx-volume-aggregateconfiguration"></a>

Use to specify configuration options for a volume’s storage aggregate or aggregates.

## Syntax
<a name="aws-properties-fsx-volume-aggregateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-aggregateconfiguration-syntax.json"></a>

```
{
  "[Aggregates](#cfn-fsx-volume-aggregateconfiguration-aggregates)" : {{[ String, ... ]}},
  "[ConstituentsPerAggregate](#cfn-fsx-volume-aggregateconfiguration-constituentsperaggregate)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-fsx-volume-aggregateconfiguration-syntax.yaml"></a>

```
  [Aggregates](#cfn-fsx-volume-aggregateconfiguration-aggregates): {{
    - String}}
  [ConstituentsPerAggregate](#cfn-fsx-volume-aggregateconfiguration-constituentsperaggregate): {{Integer}}
```

## Properties
<a name="aws-properties-fsx-volume-aggregateconfiguration-properties"></a>

`Aggregates`  <a name="cfn-fsx-volume-aggregateconfiguration-aggregates"></a>
The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:
+ The strings in the value of `Aggregates` are not are not formatted as `aggrX`, where X is a number between 1 and 12.
+ The value of `Aggregates` contains aggregates that are not present.
+ One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.
*Required*: No
*Type*: Array of String
*Maximum*: `6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConstituentsPerAggregate`  <a name="cfn-fsx-volume-aggregateconfiguration-constituentsperaggregate"></a>
Used to explicitly set the number of constituents within the FlexGroup per storage aggregate. This field is optional when creating a FlexGroup volume. If unspecified, the default value will be 8. This field cannot be provided when creating a FlexVol volume.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
