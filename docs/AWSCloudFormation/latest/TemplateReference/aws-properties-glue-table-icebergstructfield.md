---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-icebergstructfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergStructField
<a name="aws-properties-glue-table-icebergstructfield"></a>

Defines a single field within an Iceberg table schema, including its identifier, name, data type, nullability, and documentation.

## Syntax
<a name="aws-properties-glue-table-icebergstructfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-icebergstructfield-syntax.json"></a>

```
{
  "[Doc](#cfn-glue-table-icebergstructfield-doc)" : {{String}},
  "[Id](#cfn-glue-table-icebergstructfield-id)" : {{Integer}},
  "[Name](#cfn-glue-table-icebergstructfield-name)" : {{String}},
  "[Required](#cfn-glue-table-icebergstructfield-required)" : {{Boolean}},
  "[Type](#cfn-glue-table-icebergstructfield-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-icebergstructfield-syntax.yaml"></a>

```
  [Doc](#cfn-glue-table-icebergstructfield-doc): {{String}}
  [Id](#cfn-glue-table-icebergstructfield-id): {{Integer}}
  [Name](#cfn-glue-table-icebergstructfield-name): {{String}}
  [Required](#cfn-glue-table-icebergstructfield-required): {{Boolean}}
  [Type](#cfn-glue-table-icebergstructfield-type): {{String}}
```

## Properties
<a name="aws-properties-glue-table-icebergstructfield-properties"></a>

`Doc`  <a name="cfn-glue-table-icebergstructfield-doc"></a>
Optional documentation or description text that provides additional context about the purpose and usage of this field.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-glue-table-icebergstructfield-id"></a>
The unique identifier assigned to this field within the Iceberg table schema, used for schema evolution and field tracking.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-table-icebergstructfield-name"></a>
The name of the field as it appears in the table schema and query operations.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Required`  <a name="cfn-glue-table-icebergstructfield-required"></a>
Indicates whether this field is required (non-nullable) or optional (nullable) in the table schema.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-glue-table-icebergstructfield-type"></a>
The data type definition for this field, specifying the structure and format of the data it contains.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
