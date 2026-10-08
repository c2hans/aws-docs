---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergtableinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergTableInput
<a name="aws-properties-glue-table-icebergtableinput"></a>

<a name="aws-properties-glue-table-icebergtableinput-description"></a>The `IcebergTableInput` property type specifies Property description not available. for an [AWS::Glue::Table](aws-resource-glue-table.md).

## Syntax
<a name="aws-properties-glue-table-icebergtableinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergtableinput-syntax.json"></a>

```
{
  "[Location](#cfn-glue-table-icebergtableinput-location)" : {{String}},
  "[PartitionSpec](#cfn-glue-table-icebergtableinput-partitionspec)" : {{IcebergPartitionSpec}},
  "[Properties](#cfn-glue-table-icebergtableinput-properties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Schema](#cfn-glue-table-icebergtableinput-schema)" : {{IcebergSchema}},
  "[WriteOrder](#cfn-glue-table-icebergtableinput-writeorder)" : {{IcebergSortOrder}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergtableinput-syntax.yaml"></a>

```
  [Location](#cfn-glue-table-icebergtableinput-location): {{String}}
  [PartitionSpec](#cfn-glue-table-icebergtableinput-partitionspec): {{
    IcebergPartitionSpec}}
  [Properties](#cfn-glue-table-icebergtableinput-properties): {{
    {{Key}}: {{Value}}}}
  [Schema](#cfn-glue-table-icebergtableinput-schema): {{
    IcebergSchema}}
  [WriteOrder](#cfn-glue-table-icebergtableinput-writeorder): {{
    IcebergSortOrder}}
```

## Properties
<a name="aws-properties-glue-table-icebergtableinput-properties"></a>

`Location`  <a name="cfn-glue-table-icebergtableinput-location"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionSpec`  <a name="cfn-glue-table-icebergtableinput-partitionspec"></a>
Property description not available.
*Required*: No
*Type*: [IcebergPartitionSpec](aws-properties-glue-table-icebergpartitionspec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-glue-table-icebergtableinput-properties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-glue-table-icebergtableinput-schema"></a>
Property description not available.
*Required*: Yes
*Type*: [IcebergSchema](aws-properties-glue-table-icebergschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteOrder`  <a name="cfn-glue-table-icebergtableinput-writeorder"></a>
Property description not available.
*Required*: No
*Type*: [IcebergSortOrder](aws-properties-glue-table-icebergsortorder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
