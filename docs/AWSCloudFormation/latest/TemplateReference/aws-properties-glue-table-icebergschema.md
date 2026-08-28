---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergSchema
<a name="aws-properties-glue-table-icebergschema"></a>

Defines the schema structure for an Iceberg table, including field definitions, data types, and schema metadata.

## Syntax
<a name="aws-properties-glue-table-icebergschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergschema-syntax.json"></a>

```
{
  "[Fields](#cfn-glue-table-icebergschema-fields)" : {{[ IcebergStructField, ... ]}},
  "[IdentifierFieldIds](#cfn-glue-table-icebergschema-identifierfieldids)" : {{[ Integer, ... ]}},
  "[SchemaId](#cfn-glue-table-icebergschema-schemaid)" : {{Integer}},
  "[Type](#cfn-glue-table-icebergschema-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergschema-syntax.yaml"></a>

```
  [Fields](#cfn-glue-table-icebergschema-fields): {{
    - IcebergStructField}}
  [IdentifierFieldIds](#cfn-glue-table-icebergschema-identifierfieldids): {{
    - Integer}}
  [SchemaId](#cfn-glue-table-icebergschema-schemaid): {{Integer}}
  [Type](#cfn-glue-table-icebergschema-type): {{String}}
```

## Properties
<a name="aws-properties-glue-table-icebergschema-properties"></a>

`Fields`  <a name="cfn-glue-table-icebergschema-fields"></a>
The list of field definitions that make up the table schema, including field names, types, and metadata.
*Required*: Yes
*Type*: Array of [IcebergStructField](aws-properties-glue-table-icebergstructfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentifierFieldIds`  <a name="cfn-glue-table-icebergschema-identifierfieldids"></a>
The list of field identifiers that uniquely identify records in the table, used for row-level operations and deduplication.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaId`  <a name="cfn-glue-table-icebergschema-schemaid"></a>
The unique identifier for this schema version within the Iceberg table's schema evolution history.
*Required*: No
*Type*: [Integer](aws-properties-glue-table-schemaid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-glue-table-icebergschema-type"></a>
The root type of the schema structure, typically "struct" for Iceberg table schemas.
*Required*: No
*Type*: String
*Allowed values*: `struct`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
