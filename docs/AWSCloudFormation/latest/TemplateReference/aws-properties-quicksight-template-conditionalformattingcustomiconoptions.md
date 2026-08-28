---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-conditionalformattingcustomiconoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ConditionalFormattingCustomIconOptions
<a name="aws-properties-quicksight-template-conditionalformattingcustomiconoptions"></a>

Custom icon options for an icon set.

## Syntax
<a name="aws-properties-quicksight-template-conditionalformattingcustomiconoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-conditionalformattingcustomiconoptions-syntax.json"></a>

```
{
  "[Icon](#cfn-quicksight-template-conditionalformattingcustomiconoptions-icon)" : {{String}},
  "[UnicodeIcon](#cfn-quicksight-template-conditionalformattingcustomiconoptions-unicodeicon)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-conditionalformattingcustomiconoptions-syntax.yaml"></a>

```
  [Icon](#cfn-quicksight-template-conditionalformattingcustomiconoptions-icon): {{String}}
  [UnicodeIcon](#cfn-quicksight-template-conditionalformattingcustomiconoptions-unicodeicon): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-conditionalformattingcustomiconoptions-properties"></a>

`Icon`  <a name="cfn-quicksight-template-conditionalformattingcustomiconoptions-icon"></a>
Determines the type of icon.
*Required*: No
*Type*: String
*Allowed values*: `CARET_UP | CARET_DOWN | PLUS | MINUS | ARROW_UP | ARROW_DOWN | ARROW_LEFT | ARROW_UP_LEFT | ARROW_DOWN_LEFT | ARROW_RIGHT | ARROW_UP_RIGHT | ARROW_DOWN_RIGHT | FACE_UP | FACE_DOWN | FACE_FLAT | ONE_BAR | TWO_BAR | THREE_BAR | CIRCLE | TRIANGLE | SQUARE | FLAG | THUMBS_UP | THUMBS_DOWN | CHECKMARK | X`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnicodeIcon`  <a name="cfn-quicksight-template-conditionalformattingcustomiconoptions-unicodeicon"></a>
Determines the Unicode icon type.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u00FF]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
