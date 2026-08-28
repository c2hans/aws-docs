---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-freeformlayoutelementbackgroundstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FreeFormLayoutElementBackgroundStyle
<a name="aws-properties-quicksight-template-freeformlayoutelementbackgroundstyle"></a>

The background style configuration of a free-form layout element.

## Syntax
<a name="aws-properties-quicksight-template-freeformlayoutelementbackgroundstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-freeformlayoutelementbackgroundstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-freeformlayoutelementbackgroundstyle-color)" : {{String}},
  "[Visibility](#cfn-quicksight-template-freeformlayoutelementbackgroundstyle-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-freeformlayoutelementbackgroundstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-freeformlayoutelementbackgroundstyle-color): {{String}}
  [Visibility](#cfn-quicksight-template-freeformlayoutelementbackgroundstyle-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-freeformlayoutelementbackgroundstyle-properties"></a>

`Color`  <a name="cfn-quicksight-template-freeformlayoutelementbackgroundstyle-color"></a>
The background color of a free-form layout element.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-freeformlayoutelementbackgroundstyle-visibility"></a>
The background visibility of a free-form layout element.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
