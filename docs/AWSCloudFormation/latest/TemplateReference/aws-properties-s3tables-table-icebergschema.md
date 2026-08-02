---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergSchema
<a name="aws-properties-s3tables-table-icebergschema"></a>

Contains details about the schema for an Iceberg table.

## Syntax
<a name="aws-properties-s3tables-table-icebergschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergschema-syntax.json"></a>

```
{
  "[SchemaFieldList](#cfn-s3tables-table-icebergschema-schemafieldlist)" : {{[ SchemaField, ... ]}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergschema-syntax.yaml"></a>

```
  [SchemaFieldList](#cfn-s3tables-table-icebergschema-schemafieldlist): {{
    - SchemaField}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergschema-properties"></a>

`SchemaFieldList`  <a name="cfn-s3tables-table-icebergschema-schemafieldlist"></a>
The schema fields for the table
*Required*: Yes
*Type*: Array of [SchemaField](aws-properties-s3tables-table-schemafield.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
