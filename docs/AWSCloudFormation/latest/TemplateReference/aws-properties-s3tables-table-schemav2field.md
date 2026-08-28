---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-schemav2field.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table SchemaV2Field
<a name="aws-properties-s3tables-table-schemav2field"></a>

Contains details about a schema field version 2 (V2) that supports [Apache Iceberg Nested Types](https://iceberg.apache.org/spec/#nested-types). Nested data type support includes struct, list and map. Primitive types are also supported.

**Important**
`IcebergSchemaV2` is mutually exclusive with `IcebergSchema`. Specify `IcebergSchema` for flat schemas with primitive types only, or `IcebergSchemaV2` for schemas that include nested types (struct, list, map). You cannot specify both.

**Note**
Top-level CloudFormation properties use PascalCase (`Id`, `Name`, `Type`, `Required`, `Doc`). When specifying nested type objects inside `Type`, use lowercase keys (`type`, `fields`, `id`, `name`, `required`, `element-id`, `element`, `element-required`, `key-id`, `key`, `value-id`, `value`, `value-required`) as these follow the Apache Iceberg specification format.

## Syntax
<a name="aws-properties-s3tables-table-schemav2field-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-schemav2field-syntax.json"></a>

```
{
  "[Doc](#cfn-s3tables-table-schemav2field-doc)" : {{String}},
  "[Id](#cfn-s3tables-table-schemav2field-id)" : {{Integer}},
  "[Name](#cfn-s3tables-table-schemav2field-name)" : {{String}},
  "[Required](#cfn-s3tables-table-schemav2field-required)" : {{Boolean}},
  "[Type](#cfn-s3tables-table-schemav2field-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-table-schemav2field-syntax.yaml"></a>

```
  [Doc](#cfn-s3tables-table-schemav2field-doc): {{String}}
  [Id](#cfn-s3tables-table-schemav2field-id): {{Integer}}
  [Name](#cfn-s3tables-table-schemav2field-name): {{String}}
  [Required](#cfn-s3tables-table-schemav2field-required): {{Boolean}}
  [Type](#cfn-s3tables-table-schemav2field-type): {{String}}
```

## Properties
<a name="aws-properties-s3tables-table-schemav2field-properties"></a>

`Doc`  <a name="cfn-s3tables-table-schemav2field-doc"></a>
An optional description of the field.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Id`  <a name="cfn-s3tables-table-schemav2field-id"></a>
A unique identifier for the schema field V2. Field IDs are used by Apache Iceberg to track schema evolution and maintain compatibility across schema changes.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-s3tables-table-schemav2field-name"></a>
The name of the field.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Required`  <a name="cfn-s3tables-table-schemav2field-required"></a>
A Boolean value that specifies whether values are required for each row in this field. If this is `true` the field does not allow null values.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-s3tables-table-schemav2field-type"></a>
The field type. S3 Tables supports all Apache Iceberg primitive types and nested types. For more information, see the [Apache Iceberg documentation](https://iceberg.apache.org/spec/#schemas-and-data-types).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
