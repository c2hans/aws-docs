---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-partition-partitioninput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Partition PartitionInput
<a name="aws-properties-glue-partition-partitioninput"></a>

The structure used to create and update a partition.

## Syntax
<a name="aws-properties-glue-partition-partitioninput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-partition-partitioninput-syntax.json"></a>

```
{
  "[Parameters](#cfn-glue-partition-partitioninput-parameters)" : {{Json}},
  "[StorageDescriptor](#cfn-glue-partition-partitioninput-storagedescriptor)" : {{StorageDescriptor}},
  "[Values](#cfn-glue-partition-partitioninput-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-partition-partitioninput-syntax.yaml"></a>

```
  [Parameters](#cfn-glue-partition-partitioninput-parameters): {{Json}}
  [StorageDescriptor](#cfn-glue-partition-partitioninput-storagedescriptor): {{
    StorageDescriptor}}
  [Values](#cfn-glue-partition-partitioninput-values): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-partition-partitioninput-properties"></a>

`Parameters`  <a name="cfn-glue-partition-partitioninput-parameters"></a>
These key-value pairs define partition parameters.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageDescriptor`  <a name="cfn-glue-partition-partitioninput-storagedescriptor"></a>
Provides information about the physical location where the partition is stored.
*Required*: No
*Type*: [StorageDescriptor](aws-properties-glue-partition-storagedescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-glue-partition-partitioninput-values"></a>
The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.
The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-glue-partition-partitioninput--seealso"></a>
+ [PartitionInput](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-PartitionInput) in the *AWS Glue Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
