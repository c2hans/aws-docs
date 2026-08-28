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
  "[Properties](#cfn-glue-table-icebergtableinput-properties)" : {{Json}},
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
  [Properties](#cfn-glue-table-icebergtableinput-properties): {{Json}}
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
*Type*: Json
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
