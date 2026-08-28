---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-shortformattext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ShortFormatText
<a name="aws-properties-quicksight-dashboard-shortformattext"></a>

The text format for the title.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-dashboard-shortformattext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-shortformattext-syntax.json"></a>

```
{
  "[PlainText](#cfn-quicksight-dashboard-shortformattext-plaintext)" : {{String}},
  "[RichText](#cfn-quicksight-dashboard-shortformattext-richtext)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-shortformattext-syntax.yaml"></a>

```
  [PlainText](#cfn-quicksight-dashboard-shortformattext-plaintext): {{String}}
  [RichText](#cfn-quicksight-dashboard-shortformattext-richtext): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-shortformattext-properties"></a>

`PlainText`  <a name="cfn-quicksight-dashboard-shortformattext-plaintext"></a>
Plain text format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RichText`  <a name="cfn-quicksight-dashboard-shortformattext-richtext"></a>
Rich text. Examples of rich text include bold, underline, and italics.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
