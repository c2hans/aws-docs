---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-table-schema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::Table Schema
<a name="aws-properties-timestream-table-schema"></a>

 A Schema specifies the expected data model of the table.

## Syntax
<a name="aws-properties-timestream-table-schema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-table-schema-syntax.json"></a>

```
{
  "[CompositePartitionKey](#cfn-timestream-table-schema-compositepartitionkey)" : {{[ PartitionKey, ... ]}}
}
```

### YAML
<a name="aws-properties-timestream-table-schema-syntax.yaml"></a>

```
  [CompositePartitionKey](#cfn-timestream-table-schema-compositepartitionkey): {{
    - PartitionKey}}
```

## Properties
<a name="aws-properties-timestream-table-schema-properties"></a>

`CompositePartitionKey`  <a name="cfn-timestream-table-schema-compositepartitionkey"></a>
A non-empty list of partition keys defining the attributes used to partition the table data. The order of the list determines the partition hierarchy. The name and type of each partition key as well as the partition key order cannot be changed after the table is created. However, the enforcement level of each partition key can be changed.
*Required*: No
*Type*: Array of [PartitionKey](aws-properties-timestream-table-partitionkey.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
