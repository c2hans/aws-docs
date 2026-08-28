---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergMetadata
<a name="aws-properties-s3tables-table-icebergmetadata"></a>

Contains details about the metadata for an Iceberg table.

## Syntax
<a name="aws-properties-s3tables-table-icebergmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergmetadata-syntax.json"></a>

```
{
  "[IcebergPartitionSpec](#cfn-s3tables-table-icebergmetadata-icebergpartitionspec)" : {{IcebergPartitionSpec}},
  "[IcebergSchema](#cfn-s3tables-table-icebergmetadata-icebergschema)" : {{IcebergSchema}},
  "[IcebergSchemaV2](#cfn-s3tables-table-icebergmetadata-icebergschemav2)" : {{IcebergSchemaV2}},
  "[IcebergSortOrder](#cfn-s3tables-table-icebergmetadata-icebergsortorder)" : {{IcebergSortOrder}},
  "[TableProperties](#cfn-s3tables-table-icebergmetadata-tableproperties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergmetadata-syntax.yaml"></a>

```
  [IcebergPartitionSpec](#cfn-s3tables-table-icebergmetadata-icebergpartitionspec): {{
    IcebergPartitionSpec}}
  [IcebergSchema](#cfn-s3tables-table-icebergmetadata-icebergschema): {{
    IcebergSchema}}
  [IcebergSchemaV2](#cfn-s3tables-table-icebergmetadata-icebergschemav2): {{
    IcebergSchemaV2}}
  [IcebergSortOrder](#cfn-s3tables-table-icebergmetadata-icebergsortorder): {{
    IcebergSortOrder}}
  [TableProperties](#cfn-s3tables-table-icebergmetadata-tableproperties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergmetadata-properties"></a>

`IcebergPartitionSpec`  <a name="cfn-s3tables-table-icebergmetadata-icebergpartitionspec"></a>
Property description not available.
*Required*: No
*Type*: [IcebergPartitionSpec](aws-properties-s3tables-table-icebergpartitionspec.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IcebergSchema`  <a name="cfn-s3tables-table-icebergmetadata-icebergschema"></a>
The schema for an Iceberg table. Use this property to define table schemas with primitive types only. For schemas that include nested or complex types such as `struct`, `list`, or `map`, use `schemaV2` instead.
*Required*: No
*Type*: [IcebergSchema](aws-properties-s3tables-table-icebergschema.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IcebergSchemaV2`  <a name="cfn-s3tables-table-icebergmetadata-icebergschemav2"></a>
The schema for an Iceberg table using the V2 format. Use this property to define table schemas that include nested or complex data types such as `struct`, `list`, or `map`, in addition to primitive types. For schemas with only primitive types, you can use either `schema` or `schemaV2`.
*Required*: No
*Type*: [IcebergSchemaV2](aws-properties-s3tables-table-icebergschemav2.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IcebergSortOrder`  <a name="cfn-s3tables-table-icebergmetadata-icebergsortorder"></a>
Property description not available.
*Required*: No
*Type*: [IcebergSortOrder](aws-properties-s3tables-table-icebergsortorder.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableProperties`  <a name="cfn-s3tables-table-icebergmetadata-tableproperties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
