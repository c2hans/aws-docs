---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-placementgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::PlacementGroup
<a name="aws-resource-ec2-placementgroup"></a>

Specifies a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group.

A `cluster` placement group is a logical grouping of instances within a single Availability Zone that benefit from low network latency, high network throughput. A `spread` placement group places instances on distinct hardware. A `partition` placement group places groups of instances in different partitions, where instances in one partition do not share the same hardware with instances in another partition.

For more information, see [Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.

You can optionally specify the `GroupName` property in your template to create a placement group with a specific name. If you don't specify a name, CloudFormation generates a unique name. Updating the `GroupName` value requires replacement of the placement group.

## Syntax
<a name="aws-resource-ec2-placementgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-placementgroup-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::PlacementGroup",
  "Properties" : {
      "[ParentGroupId](#cfn-ec2-placementgroup-parentgroupid)" : {{String}},
      "[PartitionCount](#cfn-ec2-placementgroup-partitioncount)" : {{Integer}},
      "[SpreadLevel](#cfn-ec2-placementgroup-spreadlevel)" : {{String}},
      "[Strategy](#cfn-ec2-placementgroup-strategy)" : {{String}},
      "[Tags](#cfn-ec2-placementgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-placementgroup-syntax.yaml"></a>

```
Type: AWS::EC2::PlacementGroup
Properties:
  [ParentGroupId](#cfn-ec2-placementgroup-parentgroupid): {{String}}
  [PartitionCount](#cfn-ec2-placementgroup-partitioncount): {{Integer}}
  [SpreadLevel](#cfn-ec2-placementgroup-spreadlevel): {{String}}
  [Strategy](#cfn-ec2-placementgroup-strategy): {{String}}
  [Tags](#cfn-ec2-placementgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-placementgroup-properties"></a>

`ParentGroupId`  <a name="cfn-ec2-placementgroup-parentgroupid"></a>
The ID of the parent placement group.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartitionCount`  <a name="cfn-ec2-placementgroup-partitioncount"></a>
The number of partitions. Valid only when **Strategy** is set to `partition`.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpreadLevel`  <a name="cfn-ec2-placementgroup-spreadlevel"></a>
Determines how placement groups spread instances.
+ Host – You can use `host` only with Outpost placement groups.
+ Rack – No usage restrictions.
*Required*: No
*Type*: String
*Allowed values*: `host | rack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Strategy`  <a name="cfn-ec2-placementgroup-strategy"></a>
The placement strategy.
*Required*: No
*Type*: String
*Allowed values*: `cluster | spread | partition | precision-time`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-placementgroup-tags"></a>
The tags to apply to the new placement group.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-placementgroup-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-placementgroup-return-values"></a>

### Ref
<a name="aws-resource-ec2-placementgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the placement group.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-placementgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-placementgroup-return-values-fn--getatt-fn--getatt"></a>

`GroupId`  <a name="GroupId-fn::getatt"></a>
The ID of the placement group.

`GroupName`  <a name="GroupName-fn::getatt"></a>
The name of the placement group.
You can also specify `GroupName` in your template's `Properties` section to create a placement group with a specific name. If you don't specify a name, CloudFormation generates a unique name. Updating `GroupName` requires replacement of the placement group.

## Examples
<a name="aws-resource-ec2-placementgroup--examples"></a>

**Topics**
+ [Create a placement group](#aws-resource-ec2-placementgroup--examples--Create_a_placement_group)
+ [Create a spread placement group with a specific name](#aws-resource-ec2-placementgroup--examples--Create_a_spread_placement_group_with_a_specific_name)
+ [Create a partition placement group with a specific name](#aws-resource-ec2-placementgroup--examples--Create_a_partition_placement_group_with_a_specific_name)

### Create a placement group
<a name="aws-resource-ec2-placementgroup--examples--Create_a_placement_group"></a>

The following example declares a placement group with a cluster placement strategy.

#### JSON
<a name="aws-resource-ec2-placementgroup--examples--Create_a_placement_group--json"></a>

```
"PlacementGroup" : {
   "Type" : "AWS::EC2::PlacementGroup",
   "Properties" : {
      "Strategy" : "cluster"
   }
}
```

#### YAML
<a name="aws-resource-ec2-placementgroup--examples--Create_a_placement_group--yaml"></a>

```
PlacementGroup:
  Type: AWS::EC2::PlacementGroup
   Properties:
     Strategy: cluster
```

### Create a spread placement group with a specific name
<a name="aws-resource-ec2-placementgroup--examples--Create_a_spread_placement_group_with_a_specific_name"></a>

The following example declares a placement group with a spread placement strategy and a specific name. The placement group is created with the name `MySpreadGroup` and spreads instances across distinct racks.

#### JSON
<a name="aws-resource-ec2-placementgroup--examples--Create_a_spread_placement_group_with_a_specific_name--json"></a>

```
"PlacementGroup" : {
   "Type" : "AWS::EC2::PlacementGroup",
   "Properties" : {
      "GroupName" : "MySpreadGroup",
      "SpreadLevel" : "rack",
      "Strategy" : "spread"
   }
}
```

#### YAML
<a name="aws-resource-ec2-placementgroup--examples--Create_a_spread_placement_group_with_a_specific_name--yaml"></a>

```
PlacementGroup:
  Type: AWS::EC2::PlacementGroup
  Properties:
    GroupName: MySpreadGroup
    SpreadLevel: rack
    Strategy: spread
```

### Create a partition placement group with a specific name
<a name="aws-resource-ec2-placementgroup--examples--Create_a_partition_placement_group_with_a_specific_name"></a>

The following example declares a placement group with a partition placement strategy, three partitions, and a specific name.

#### JSON
<a name="aws-resource-ec2-placementgroup--examples--Create_a_partition_placement_group_with_a_specific_name--json"></a>

```
"PlacementGroup" : {
   "Type" : "AWS::EC2::PlacementGroup",
   "Properties" : {
      "GroupName" : "MyPartitionGroup",
      "PartitionCount" : 3,
      "Strategy" : "partition"
   }
}
```

#### YAML
<a name="aws-resource-ec2-placementgroup--examples--Create_a_partition_placement_group_with_a_specific_name--yaml"></a>

```
PlacementGroup:
  Type: AWS::EC2::PlacementGroup
  Properties:
    GroupName: MyPartitionGroup
    PartitionCount: 3
    Strategy: partition
```
