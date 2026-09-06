---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-thousandseparatoroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ThousandSeparatorOptions
<a name="aws-properties-quicksight-analysis-thousandseparatoroptions"></a>

The options that determine the thousands separator configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-thousandseparatoroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-thousandseparatoroptions-syntax.json"></a>

```
{
  "[GroupingStyle](#cfn-quicksight-analysis-thousandseparatoroptions-groupingstyle)" : {{String}},
  "[Symbol](#cfn-quicksight-analysis-thousandseparatoroptions-symbol)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-thousandseparatoroptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-thousandseparatoroptions-syntax.yaml"></a>

```
  [GroupingStyle](#cfn-quicksight-analysis-thousandseparatoroptions-groupingstyle): {{String}}
  [Symbol](#cfn-quicksight-analysis-thousandseparatoroptions-symbol): {{String}}
  [Visibility](#cfn-quicksight-analysis-thousandseparatoroptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-thousandseparatoroptions-properties"></a>

`GroupingStyle`  <a name="cfn-quicksight-analysis-thousandseparatoroptions-groupingstyle"></a>
Determines the way numbers are styled to accommodate different readability standards. The `DEFAULT` value uses the standard international grouping system and groups numbers by the thousands. The `LAKHS` value uses the Indian numbering system and groups numbers by lakhs and crores.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | LAKHS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Symbol`  <a name="cfn-quicksight-analysis-thousandseparatoroptions-symbol"></a>
Determines the thousands separator symbol.
*Required*: No
*Type*: String
*Allowed values*: `COMMA | DOT | SPACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-thousandseparatoroptions-visibility"></a>
Determines the visibility of the thousands separator.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
