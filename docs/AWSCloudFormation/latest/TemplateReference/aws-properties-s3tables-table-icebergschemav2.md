---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-icebergschemav2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table IcebergSchemaV2
<a name="aws-properties-s3tables-table-icebergschemav2"></a>

Contains details about the schema version 2 (V2) for an Iceberg table that supports [Apache Iceberg Nested Types](https://iceberg.apache.org/spec/#nested-types). Nested data type support includes struct, list and map. Primitive types are also supported.

## Syntax
<a name="aws-properties-s3tables-table-icebergschemav2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-icebergschemav2-syntax.json"></a>

```
{
  "[IdentifierFieldIds](#cfn-s3tables-table-icebergschemav2-identifierfieldids)" : {{[ Integer, ... ]}},
  "[SchemaId](#cfn-s3tables-table-icebergschemav2-schemaid)" : {{Integer}},
  "[SchemaV2FieldList](#cfn-s3tables-table-icebergschemav2-schemav2fieldlist)" : {{[ SchemaV2Field, ... ]}},
  "[SchemaV2FieldType](#cfn-s3tables-table-icebergschemav2-schemav2fieldtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-table-icebergschemav2-syntax.yaml"></a>

```
  [IdentifierFieldIds](#cfn-s3tables-table-icebergschemav2-identifierfieldids): {{
    - Integer}}
  [SchemaId](#cfn-s3tables-table-icebergschemav2-schemaid): {{Integer}}
  [SchemaV2FieldList](#cfn-s3tables-table-icebergschemav2-schemav2fieldlist): {{
    - SchemaV2Field}}
  [SchemaV2FieldType](#cfn-s3tables-table-icebergschemav2-schemav2fieldtype): {{String}}
```

## Properties
<a name="aws-properties-s3tables-table-icebergschemav2-properties"></a>

`IdentifierFieldIds`  <a name="cfn-s3tables-table-icebergschemav2-identifierfieldids"></a>
A list of field IDs that are used as the identifier fields for the table. Identifier fields uniquely identify a row in the table.
*Required*: No
*Type*: Array of Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaId`  <a name="cfn-s3tables-table-icebergschemav2-schemaid"></a>
An optional unique identifier for the schema.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaV2FieldList`  <a name="cfn-s3tables-table-icebergschemav2-schemav2fieldlist"></a>
The schema fields for the table.
*Required*: Yes
*Type*: Array of [SchemaV2Field](aws-properties-s3tables-table-schemav2field.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaV2FieldType`  <a name="cfn-s3tables-table-icebergschemav2-schemav2fieldtype"></a>
The type of the top-level schema, which is always a struct type.
*Required*: Yes
*Type*: String
*Allowed values*: `struct`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
