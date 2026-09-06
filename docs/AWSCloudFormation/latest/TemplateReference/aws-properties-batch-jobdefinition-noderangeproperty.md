---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-noderangeproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition NodeRangeProperty
<a name="aws-properties-batch-jobdefinition-noderangeproperty"></a>

This is an object that represents the properties of the node range for a multi-node parallel job.

## Syntax
<a name="aws-properties-batch-jobdefinition-noderangeproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-noderangeproperty-syntax.json"></a>

```
{
  "[ConsumableResourceProperties](#cfn-batch-jobdefinition-noderangeproperty-consumableresourceproperties)" : {{ConsumableResourceProperties}},
  "[Container](#cfn-batch-jobdefinition-noderangeproperty-container)" : {{MultiNodeContainerProperties}},
  "[EcsProperties](#cfn-batch-jobdefinition-noderangeproperty-ecsproperties)" : {{MultiNodeEcsProperties}},
  "[EksProperties](#cfn-batch-jobdefinition-noderangeproperty-eksproperties)" : {{EksProperties}},
  "[InstanceTypes](#cfn-batch-jobdefinition-noderangeproperty-instancetypes)" : {{[ String, ... ]}},
  "[TargetNodes](#cfn-batch-jobdefinition-noderangeproperty-targetnodes)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-noderangeproperty-syntax.yaml"></a>

```
  [ConsumableResourceProperties](#cfn-batch-jobdefinition-noderangeproperty-consumableresourceproperties): {{
    ConsumableResourceProperties}}
  [Container](#cfn-batch-jobdefinition-noderangeproperty-container): {{
    MultiNodeContainerProperties}}
  [EcsProperties](#cfn-batch-jobdefinition-noderangeproperty-ecsproperties): {{
    MultiNodeEcsProperties}}
  [EksProperties](#cfn-batch-jobdefinition-noderangeproperty-eksproperties): {{
    EksProperties}}
  [InstanceTypes](#cfn-batch-jobdefinition-noderangeproperty-instancetypes): {{
    - String}}
  [TargetNodes](#cfn-batch-jobdefinition-noderangeproperty-targetnodes): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-noderangeproperty-properties"></a>

`ConsumableResourceProperties`  <a name="cfn-batch-jobdefinition-noderangeproperty-consumableresourceproperties"></a>
Contains a list of consumable resources required by a job.
*Required*: No
*Type*: [ConsumableResourceProperties](aws-properties-batch-jobdefinition-consumableresourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Container`  <a name="cfn-batch-jobdefinition-noderangeproperty-container"></a>
The container details for the node range.
*Required*: No
*Type*: [MultiNodeContainerProperties](aws-properties-batch-jobdefinition-multinodecontainerproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EcsProperties`  <a name="cfn-batch-jobdefinition-noderangeproperty-ecsproperties"></a>
This is an object that represents the properties of the node range for a multi-node parallel job.
*Required*: No
*Type*: [MultiNodeEcsProperties](aws-properties-batch-jobdefinition-multinodeecsproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EksProperties`  <a name="cfn-batch-jobdefinition-noderangeproperty-eksproperties"></a>
This is an object that represents the properties of the node range for a multi-node parallel job.
*Required*: No
*Type*: [EksProperties](aws-properties-batch-jobdefinition-eksproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceTypes`  <a name="cfn-batch-jobdefinition-noderangeproperty-instancetypes"></a>
The instance types of the underlying host infrastructure of a multi-node parallel job.
This parameter isn't applicable to jobs that are running on Fargate resources.
In addition, this list object is currently limited to one element.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetNodes`  <a name="cfn-batch-jobdefinition-noderangeproperty-targetnodes"></a>
The range of nodes, using node index values. A range of `0:3` indicates nodes with index values of `0` through `3`. If the starting range value is omitted (`:n`), then `0` is used to start the range. If the ending range value is omitted (`n:`), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (`0:n`). You can nest node ranges (for example, `0:10` and `4:5`). In this case, the `4:5` range properties override the `0:10` properties.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-batch-jobdefinition-noderangeproperty--seealso"></a>
+ [Multi-node Parallel Jobs](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html) in the * AWS Batch User Guide *.
