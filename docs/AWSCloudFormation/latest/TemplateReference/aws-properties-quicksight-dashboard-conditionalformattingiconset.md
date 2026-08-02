---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-conditionalformattingiconset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ConditionalFormattingIconSet
<a name="aws-properties-quicksight-dashboard-conditionalformattingiconset"></a>

Formatting configuration for icon set.

## Syntax
<a name="aws-properties-quicksight-dashboard-conditionalformattingiconset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-conditionalformattingiconset-syntax.json"></a>

```
{
  "[Expression](#cfn-quicksight-dashboard-conditionalformattingiconset-expression)" : {{String}},
  "[IconSetType](#cfn-quicksight-dashboard-conditionalformattingiconset-iconsettype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-conditionalformattingiconset-syntax.yaml"></a>

```
  [Expression](#cfn-quicksight-dashboard-conditionalformattingiconset-expression): {{String}}
  [IconSetType](#cfn-quicksight-dashboard-conditionalformattingiconset-iconsettype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-conditionalformattingiconset-properties"></a>

`Expression`  <a name="cfn-quicksight-dashboard-conditionalformattingiconset-expression"></a>
The expression that determines the formatting configuration for the icon set.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IconSetType`  <a name="cfn-quicksight-dashboard-conditionalformattingiconset-iconsettype"></a>
Determines the icon set type.
*Required*: No
*Type*: String
*Allowed values*: `PLUS_MINUS | CHECK_X | THREE_COLOR_ARROW | THREE_GRAY_ARROW | CARET_UP_MINUS_DOWN | THREE_SHAPE | THREE_CIRCLE | FLAGS | BARS | FOUR_COLOR_ARROW | FOUR_GRAY_ARROW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
