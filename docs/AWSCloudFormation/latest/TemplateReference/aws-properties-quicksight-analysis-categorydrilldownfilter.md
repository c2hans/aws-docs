---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-categorydrilldownfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CategoryDrillDownFilter
<a name="aws-properties-quicksight-analysis-categorydrilldownfilter"></a>

The category drill down filter.

## Syntax
<a name="aws-properties-quicksight-analysis-categorydrilldownfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-categorydrilldownfilter-syntax.json"></a>

```
{
  "[CategoryValues](#cfn-quicksight-analysis-categorydrilldownfilter-categoryvalues)" : {{[ String, ... ]}},
  "[Column](#cfn-quicksight-analysis-categorydrilldownfilter-column)" : {{ColumnIdentifier}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-categorydrilldownfilter-syntax.yaml"></a>

```
  [CategoryValues](#cfn-quicksight-analysis-categorydrilldownfilter-categoryvalues): {{
    - String}}
  [Column](#cfn-quicksight-analysis-categorydrilldownfilter-column): {{
    ColumnIdentifier}}
```

## Properties
<a name="aws-properties-quicksight-analysis-categorydrilldownfilter-properties"></a>

`CategoryValues`  <a name="cfn-quicksight-analysis-categorydrilldownfilter-categoryvalues"></a>
A list of the string inputs that are the values of the category drill down filter.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Column`  <a name="cfn-quicksight-analysis-categorydrilldownfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
