---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-numericrangefiltervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis NumericRangeFilterValue
<a name="aws-properties-quicksight-analysis-numericrangefiltervalue"></a>

The value input pf the numeric range filter.

## Syntax
<a name="aws-properties-quicksight-analysis-numericrangefiltervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-numericrangefiltervalue-syntax.json"></a>

```
{
  "[Parameter](#cfn-quicksight-analysis-numericrangefiltervalue-parameter)" : {{String}},
  "[StaticValue](#cfn-quicksight-analysis-numericrangefiltervalue-staticvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-numericrangefiltervalue-syntax.yaml"></a>

```
  [Parameter](#cfn-quicksight-analysis-numericrangefiltervalue-parameter): {{String}}
  [StaticValue](#cfn-quicksight-analysis-numericrangefiltervalue-staticvalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-numericrangefiltervalue-properties"></a>

`Parameter`  <a name="cfn-quicksight-analysis-numericrangefiltervalue-parameter"></a>
The parameter that is used in the numeric range.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValue`  <a name="cfn-quicksight-analysis-numericrangefiltervalue-staticvalue"></a>
The static value of the numeric range filter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
