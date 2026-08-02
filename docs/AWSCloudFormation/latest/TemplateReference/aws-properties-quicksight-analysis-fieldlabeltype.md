---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-fieldlabeltype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FieldLabelType
<a name="aws-properties-quicksight-analysis-fieldlabeltype"></a>

The field label type.

## Syntax
<a name="aws-properties-quicksight-analysis-fieldlabeltype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-fieldlabeltype-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-analysis-fieldlabeltype-fieldid)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-fieldlabeltype-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-fieldlabeltype-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-analysis-fieldlabeltype-fieldid): {{String}}
  [Visibility](#cfn-quicksight-analysis-fieldlabeltype-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-fieldlabeltype-properties"></a>

`FieldId`  <a name="cfn-quicksight-analysis-fieldlabeltype-fieldid"></a>
Indicates the field that is targeted by the field label.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-fieldlabeltype-visibility"></a>
The visibility of the field label.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
