---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sectionstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SectionStyle
<a name="aws-properties-quicksight-template-sectionstyle"></a>

The options that style a section.

## Syntax
<a name="aws-properties-quicksight-template-sectionstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sectionstyle-syntax.json"></a>

```
{
  "[Height](#cfn-quicksight-template-sectionstyle-height)" : {{String}},
  "[Padding](#cfn-quicksight-template-sectionstyle-padding)" : {{Spacing}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sectionstyle-syntax.yaml"></a>

```
  [Height](#cfn-quicksight-template-sectionstyle-height): {{String}}
  [Padding](#cfn-quicksight-template-sectionstyle-padding): {{
    Spacing}}
```

## Properties
<a name="aws-properties-quicksight-template-sectionstyle-properties"></a>

`Height`  <a name="cfn-quicksight-template-sectionstyle-height"></a>
The height of a section.
Heights can only be defined for header and footer sections. The default height margin is 0.5 inches.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Padding`  <a name="cfn-quicksight-template-sectionstyle-padding"></a>
The spacing between section content and its top, bottom, left, and right edges.
There is no padding by default.
*Required*: No
*Type*: [Spacing](aws-properties-quicksight-template-spacing.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
