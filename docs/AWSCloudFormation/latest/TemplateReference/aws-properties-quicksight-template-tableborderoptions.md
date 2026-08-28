---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tableborderoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableBorderOptions
<a name="aws-properties-quicksight-template-tableborderoptions"></a>

The border options for a table border.

## Syntax
<a name="aws-properties-quicksight-template-tableborderoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tableborderoptions-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-tableborderoptions-color)" : {{String}},
  "[Style](#cfn-quicksight-template-tableborderoptions-style)" : {{String}},
  "[Thickness](#cfn-quicksight-template-tableborderoptions-thickness)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tableborderoptions-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-tableborderoptions-color): {{String}}
  [Style](#cfn-quicksight-template-tableborderoptions-style): {{String}}
  [Thickness](#cfn-quicksight-template-tableborderoptions-thickness): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-tableborderoptions-properties"></a>

`Color`  <a name="cfn-quicksight-template-tableborderoptions-color"></a>
The color of a table border.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Style`  <a name="cfn-quicksight-template-tableborderoptions-style"></a>
The style (none, solid) of a table border.
*Required*: No
*Type*: String
*Allowed values*: `NONE | SOLID`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Thickness`  <a name="cfn-quicksight-template-tableborderoptions-thickness"></a>
The thickness of a table border.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
