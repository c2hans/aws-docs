---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-fieldtooltipitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FieldTooltipItem
<a name="aws-properties-quicksight-template-fieldtooltipitem"></a>

The tooltip item for the fields.

## Syntax
<a name="aws-properties-quicksight-template-fieldtooltipitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-fieldtooltipitem-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-template-fieldtooltipitem-fieldid)" : {{String}},
  "[Label](#cfn-quicksight-template-fieldtooltipitem-label)" : {{String}},
  "[TooltipTarget](#cfn-quicksight-template-fieldtooltipitem-tooltiptarget)" : {{String}},
  "[Visibility](#cfn-quicksight-template-fieldtooltipitem-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-fieldtooltipitem-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-template-fieldtooltipitem-fieldid): {{String}}
  [Label](#cfn-quicksight-template-fieldtooltipitem-label): {{String}}
  [TooltipTarget](#cfn-quicksight-template-fieldtooltipitem-tooltiptarget): {{String}}
  [Visibility](#cfn-quicksight-template-fieldtooltipitem-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-fieldtooltipitem-properties"></a>

`FieldId`  <a name="cfn-quicksight-template-fieldtooltipitem-fieldid"></a>
The unique ID of the field that is targeted by the tooltip.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-template-fieldtooltipitem-label"></a>
The label of the tooltip item.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipTarget`  <a name="cfn-quicksight-template-fieldtooltipitem-tooltiptarget"></a>
Determines the target of the field tooltip item in a combo chart visual.
*Required*: No
*Type*: String
*Allowed values*: `BOTH | BAR | LINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-fieldtooltipitem-visibility"></a>
The visibility of the tooltip item.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
