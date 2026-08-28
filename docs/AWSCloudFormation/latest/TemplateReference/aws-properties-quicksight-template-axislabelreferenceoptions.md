---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-axislabelreferenceoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template AxisLabelReferenceOptions
<a name="aws-properties-quicksight-template-axislabelreferenceoptions"></a>

The reference that specifies where the axis label is applied to.

## Syntax
<a name="aws-properties-quicksight-template-axislabelreferenceoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-axislabelreferenceoptions-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-template-axislabelreferenceoptions-column)" : {{ColumnIdentifier}},
  "[FieldId](#cfn-quicksight-template-axislabelreferenceoptions-fieldid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-axislabelreferenceoptions-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-template-axislabelreferenceoptions-column): {{
    ColumnIdentifier}}
  [FieldId](#cfn-quicksight-template-axislabelreferenceoptions-fieldid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-axislabelreferenceoptions-properties"></a>

`Column`  <a name="cfn-quicksight-template-axislabelreferenceoptions-column"></a>
The column that the axis label is targeted to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-template-axislabelreferenceoptions-fieldid"></a>
The field that the axis label is targeted to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
