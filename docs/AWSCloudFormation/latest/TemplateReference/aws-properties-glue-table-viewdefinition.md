---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-viewdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table ViewDefinition
<a name="aws-properties-glue-table-viewdefinition"></a>

A structure containing details for representations.

## Syntax
<a name="aws-properties-glue-table-viewdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-viewdefinition-syntax.json"></a>

```
{
  "[Definer](#cfn-glue-table-viewdefinition-definer)" : {{String}},
  "[IsProtected](#cfn-glue-table-viewdefinition-isprotected)" : {{Boolean}},
  "[Representations](#cfn-glue-table-viewdefinition-representations)" : {{[ ViewRepresentation, ... ]}},
  "[SubObjects](#cfn-glue-table-viewdefinition-subobjects)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-table-viewdefinition-syntax.yaml"></a>

```
  [Definer](#cfn-glue-table-viewdefinition-definer): {{String}}
  [IsProtected](#cfn-glue-table-viewdefinition-isprotected): {{Boolean}}
  [Representations](#cfn-glue-table-viewdefinition-representations): {{
    - ViewRepresentation}}
  [SubObjects](#cfn-glue-table-viewdefinition-subobjects): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-table-viewdefinition-properties"></a>

`Definer`  <a name="cfn-glue-table-viewdefinition-definer"></a>
The definer of a view in SQL.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsProtected`  <a name="cfn-glue-table-viewdefinition-isprotected"></a>
You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engine's documentation to understand the guarantees provided, if any.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Representations`  <a name="cfn-glue-table-viewdefinition-representations"></a>
A list of representations.
*Required*: No
*Type*: Array of [ViewRepresentation](aws-properties-glue-table-viewrepresentation.md)
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubObjects`  <a name="cfn-glue-table-viewdefinition-subobjects"></a>
A list of table Amazon Resource Names (ARNs).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
