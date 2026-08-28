---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-themeerror.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme ThemeError
<a name="aws-properties-quicksight-theme-themeerror"></a>

Theme error.

## Syntax
<a name="aws-properties-quicksight-theme-themeerror-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-themeerror-syntax.json"></a>

```
{
  "[Message](#cfn-quicksight-theme-themeerror-message)" : {{String}},
  "[Type](#cfn-quicksight-theme-themeerror-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-themeerror-syntax.yaml"></a>

```
  [Message](#cfn-quicksight-theme-themeerror-message): {{String}}
  [Type](#cfn-quicksight-theme-themeerror-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-theme-themeerror-properties"></a>

`Message`  <a name="cfn-quicksight-theme-themeerror-message"></a>
The error message.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-theme-themeerror-type"></a>
The type of error.
*Required*: No
*Type*: String
*Allowed values*: `INTERNAL_FAILURE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
