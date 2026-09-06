---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-conditionalformattingcustomiconoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ConditionalFormattingCustomIconOptions
<a name="aws-properties-quicksight-analysis-conditionalformattingcustomiconoptions"></a>

Custom icon options for an icon set.

## Syntax
<a name="aws-properties-quicksight-analysis-conditionalformattingcustomiconoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-conditionalformattingcustomiconoptions-syntax.json"></a>

```
{
  "[Icon](#cfn-quicksight-analysis-conditionalformattingcustomiconoptions-icon)" : {{String}},
  "[UnicodeIcon](#cfn-quicksight-analysis-conditionalformattingcustomiconoptions-unicodeicon)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-conditionalformattingcustomiconoptions-syntax.yaml"></a>

```
  [Icon](#cfn-quicksight-analysis-conditionalformattingcustomiconoptions-icon): {{String}}
  [UnicodeIcon](#cfn-quicksight-analysis-conditionalformattingcustomiconoptions-unicodeicon): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-conditionalformattingcustomiconoptions-properties"></a>

`Icon`  <a name="cfn-quicksight-analysis-conditionalformattingcustomiconoptions-icon"></a>
Determines the type of icon.
*Required*: No
*Type*: String
*Allowed values*: `CARET_UP | CARET_DOWN | PLUS | MINUS | ARROW_UP | ARROW_DOWN | ARROW_LEFT | ARROW_UP_LEFT | ARROW_DOWN_LEFT | ARROW_RIGHT | ARROW_UP_RIGHT | ARROW_DOWN_RIGHT | FACE_UP | FACE_DOWN | FACE_FLAT | ONE_BAR | TWO_BAR | THREE_BAR | CIRCLE | TRIANGLE | SQUARE | FLAG | THUMBS_UP | THUMBS_DOWN | CHECKMARK | X`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnicodeIcon`  <a name="cfn-quicksight-analysis-conditionalformattingcustomiconoptions-unicodeicon"></a>
Determines the Unicode icon type.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u00FF]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
