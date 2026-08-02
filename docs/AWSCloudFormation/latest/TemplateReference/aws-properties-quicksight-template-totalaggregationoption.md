---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-totalaggregationoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TotalAggregationOption
<a name="aws-properties-quicksight-template-totalaggregationoption"></a>

The total aggregation settings map of a field id.

## Syntax
<a name="aws-properties-quicksight-template-totalaggregationoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-totalaggregationoption-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-template-totalaggregationoption-fieldid)" : {{String}},
  "[TotalAggregationFunction](#cfn-quicksight-template-totalaggregationoption-totalaggregationfunction)" : {{TotalAggregationFunction}}
}
```

### YAML
<a name="aws-properties-quicksight-template-totalaggregationoption-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-template-totalaggregationoption-fieldid): {{String}}
  [TotalAggregationFunction](#cfn-quicksight-template-totalaggregationoption-totalaggregationfunction): {{
    TotalAggregationFunction}}
```

## Properties
<a name="aws-properties-quicksight-template-totalaggregationoption-properties"></a>

`FieldId`  <a name="cfn-quicksight-template-totalaggregationoption-fieldid"></a>
The field id that's associated with the total aggregation option.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAggregationFunction`  <a name="cfn-quicksight-template-totalaggregationoption-totalaggregationfunction"></a>
The total aggregation function that you want to set for a specified field id.
*Required*: Yes
*Type*: [TotalAggregationFunction](aws-properties-quicksight-template-totalaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
