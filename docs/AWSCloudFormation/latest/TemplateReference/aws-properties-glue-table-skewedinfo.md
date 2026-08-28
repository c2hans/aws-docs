---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-skewedinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table SkewedInfo
<a name="aws-properties-glue-table-skewedinfo"></a>

Specifies skewed values in a table. Skewed values are those that occur with very high frequency.

## Syntax
<a name="aws-properties-glue-table-skewedinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-skewedinfo-syntax.json"></a>

```
{
  "[SkewedColumnNames](#cfn-glue-table-skewedinfo-skewedcolumnnames)" : {{[ String, ... ]}},
  "[SkewedColumnValueLocationMaps](#cfn-glue-table-skewedinfo-skewedcolumnvaluelocationmaps)" : {{Json}},
  "[SkewedColumnValues](#cfn-glue-table-skewedinfo-skewedcolumnvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-table-skewedinfo-syntax.yaml"></a>

```
  [SkewedColumnNames](#cfn-glue-table-skewedinfo-skewedcolumnnames): {{
    - String}}
  [SkewedColumnValueLocationMaps](#cfn-glue-table-skewedinfo-skewedcolumnvaluelocationmaps): {{Json}}
  [SkewedColumnValues](#cfn-glue-table-skewedinfo-skewedcolumnvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-table-skewedinfo-properties"></a>

`SkewedColumnNames`  <a name="cfn-glue-table-skewedinfo-skewedcolumnnames"></a>
A list of names of columns that contain skewed values.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkewedColumnValueLocationMaps`  <a name="cfn-glue-table-skewedinfo-skewedcolumnvaluelocationmaps"></a>
A mapping of skewed values to the columns that contain them.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkewedColumnValues`  <a name="cfn-glue-table-skewedinfo-skewedcolumnvalues"></a>
A list of values that appear so frequently as to be considered skewed.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
