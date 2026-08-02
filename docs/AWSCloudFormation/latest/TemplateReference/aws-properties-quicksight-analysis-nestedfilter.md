---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-nestedfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis NestedFilter
<a name="aws-properties-quicksight-analysis-nestedfilter"></a>

A `NestedFilter` filters data with a subset of data that is defined by the nested inner filter.

## Syntax
<a name="aws-properties-quicksight-analysis-nestedfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-nestedfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-nestedfilter-column)" : {{ColumnIdentifier}},
  "[FilterId](#cfn-quicksight-analysis-nestedfilter-filterid)" : {{String}},
  "[IncludeInnerSet](#cfn-quicksight-analysis-nestedfilter-includeinnerset)" : {{Boolean}},
  "[InnerFilter](#cfn-quicksight-analysis-nestedfilter-innerfilter)" : {{InnerFilter}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-nestedfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-nestedfilter-column): {{
    ColumnIdentifier}}
  [FilterId](#cfn-quicksight-analysis-nestedfilter-filterid): {{String}}
  [IncludeInnerSet](#cfn-quicksight-analysis-nestedfilter-includeinnerset): {{Boolean}}
  [InnerFilter](#cfn-quicksight-analysis-nestedfilter-innerfilter): {{
    InnerFilter}}
```

## Properties
<a name="aws-properties-quicksight-analysis-nestedfilter-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-nestedfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterId`  <a name="cfn-quicksight-analysis-nestedfilter-filterid"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeInnerSet`  <a name="cfn-quicksight-analysis-nestedfilter-includeinnerset"></a>
A boolean condition to include or exclude the subset that is defined by the values of the nested inner filter.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InnerFilter`  <a name="cfn-quicksight-analysis-nestedfilter-innerfilter"></a>
The `InnerFilter` defines the subset of data to be used with the `NestedFilter`.
*Required*: Yes
*Type*: [InnerFilter](aws-properties-quicksight-analysis-innerfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
