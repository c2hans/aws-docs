---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-categoryinnerfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CategoryInnerFilter
<a name="aws-properties-quicksight-dashboard-categoryinnerfilter"></a>

A `CategoryInnerFilter` filters text values for the `NestedFilter`.

## Syntax
<a name="aws-properties-quicksight-dashboard-categoryinnerfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-categoryinnerfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-dashboard-categoryinnerfilter-column)" : {{ColumnIdentifier}},
  "[Configuration](#cfn-quicksight-dashboard-categoryinnerfilter-configuration)" : {{CategoryFilterConfiguration}},
  "[DefaultFilterControlConfiguration](#cfn-quicksight-dashboard-categoryinnerfilter-defaultfiltercontrolconfiguration)" : {{DefaultFilterControlConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-categoryinnerfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-dashboard-categoryinnerfilter-column): {{
    ColumnIdentifier}}
  [Configuration](#cfn-quicksight-dashboard-categoryinnerfilter-configuration): {{
    CategoryFilterConfiguration}}
  [DefaultFilterControlConfiguration](#cfn-quicksight-dashboard-categoryinnerfilter-defaultfiltercontrolconfiguration): {{
    DefaultFilterControlConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-categoryinnerfilter-properties"></a>

`Column`  <a name="cfn-quicksight-dashboard-categoryinnerfilter-column"></a>
Property description not available.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-quicksight-dashboard-categoryinnerfilter-configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [CategoryFilterConfiguration](aws-properties-quicksight-dashboard-categoryfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFilterControlConfiguration`  <a name="cfn-quicksight-dashboard-categoryinnerfilter-defaultfiltercontrolconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [DefaultFilterControlConfiguration](aws-properties-quicksight-dashboard-defaultfiltercontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
