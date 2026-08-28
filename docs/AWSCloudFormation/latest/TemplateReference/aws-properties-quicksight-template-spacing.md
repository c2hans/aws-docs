---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-spacing.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template Spacing
<a name="aws-properties-quicksight-template-spacing"></a>

The configuration of spacing (often a margin or padding).

## Syntax
<a name="aws-properties-quicksight-template-spacing-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-spacing-syntax.json"></a>

```
{
  "[Bottom](#cfn-quicksight-template-spacing-bottom)" : {{String}},
  "[Left](#cfn-quicksight-template-spacing-left)" : {{String}},
  "[Right](#cfn-quicksight-template-spacing-right)" : {{String}},
  "[Top](#cfn-quicksight-template-spacing-top)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-spacing-syntax.yaml"></a>

```
  [Bottom](#cfn-quicksight-template-spacing-bottom): {{String}}
  [Left](#cfn-quicksight-template-spacing-left): {{String}}
  [Right](#cfn-quicksight-template-spacing-right): {{String}}
  [Top](#cfn-quicksight-template-spacing-top): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-spacing-properties"></a>

`Bottom`  <a name="cfn-quicksight-template-spacing-bottom"></a>
Define the bottom spacing.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Left`  <a name="cfn-quicksight-template-spacing-left"></a>
Define the left spacing.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Right`  <a name="cfn-quicksight-template-spacing-right"></a>
Define the right spacing.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Top`  <a name="cfn-quicksight-template-spacing-top"></a>
Define the top spacing.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
