---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-databarsoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataBarsOptions
<a name="aws-properties-quicksight-template-databarsoptions"></a>

The options for data bars.

## Syntax
<a name="aws-properties-quicksight-template-databarsoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-databarsoptions-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-template-databarsoptions-fieldid)" : {{String}},
  "[NegativeColor](#cfn-quicksight-template-databarsoptions-negativecolor)" : {{String}},
  "[PositiveColor](#cfn-quicksight-template-databarsoptions-positivecolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-databarsoptions-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-template-databarsoptions-fieldid): {{String}}
  [NegativeColor](#cfn-quicksight-template-databarsoptions-negativecolor): {{String}}
  [PositiveColor](#cfn-quicksight-template-databarsoptions-positivecolor): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-databarsoptions-properties"></a>

`FieldId`  <a name="cfn-quicksight-template-databarsoptions-fieldid"></a>
The field ID for the data bars options.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NegativeColor`  <a name="cfn-quicksight-template-databarsoptions-negativecolor"></a>
The color of the negative data bar.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PositiveColor`  <a name="cfn-quicksight-template-databarsoptions-positivecolor"></a>
The color of the positive data bar.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
