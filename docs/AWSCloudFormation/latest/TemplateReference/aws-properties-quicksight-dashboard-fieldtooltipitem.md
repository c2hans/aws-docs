---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-fieldtooltipitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FieldTooltipItem
<a name="aws-properties-quicksight-dashboard-fieldtooltipitem"></a>

The tooltip item for the fields.

## Syntax
<a name="aws-properties-quicksight-dashboard-fieldtooltipitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-fieldtooltipitem-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-dashboard-fieldtooltipitem-fieldid)" : {{String}},
  "[Label](#cfn-quicksight-dashboard-fieldtooltipitem-label)" : {{String}},
  "[TooltipTarget](#cfn-quicksight-dashboard-fieldtooltipitem-tooltiptarget)" : {{String}},
  "[Visibility](#cfn-quicksight-dashboard-fieldtooltipitem-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-fieldtooltipitem-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-dashboard-fieldtooltipitem-fieldid): {{String}}
  [Label](#cfn-quicksight-dashboard-fieldtooltipitem-label): {{String}}
  [TooltipTarget](#cfn-quicksight-dashboard-fieldtooltipitem-tooltiptarget): {{String}}
  [Visibility](#cfn-quicksight-dashboard-fieldtooltipitem-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-fieldtooltipitem-properties"></a>

`FieldId`  <a name="cfn-quicksight-dashboard-fieldtooltipitem-fieldid"></a>
The unique ID of the field that is targeted by the tooltip.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-quicksight-dashboard-fieldtooltipitem-label"></a>
The label of the tooltip item.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipTarget`  <a name="cfn-quicksight-dashboard-fieldtooltipitem-tooltiptarget"></a>
Determines the target of the field tooltip item in a combo chart visual.
*Required*: No
*Type*: String
*Allowed values*: `BOTH | BAR | LINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-fieldtooltipitem-visibility"></a>
The visibility of the tooltip item.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
