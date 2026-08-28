---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablefieldoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableFieldOption
<a name="aws-properties-quicksight-template-tablefieldoption"></a>

The options for a table field.

## Syntax
<a name="aws-properties-quicksight-template-tablefieldoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablefieldoption-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-template-tablefieldoption-customlabel)" : {{String}},
  "[FieldId](#cfn-quicksight-template-tablefieldoption-fieldid)" : {{String}},
  "[URLStyling](#cfn-quicksight-template-tablefieldoption-urlstyling)" : {{TableFieldURLConfiguration}},
  "[Visibility](#cfn-quicksight-template-tablefieldoption-visibility)" : {{String}},
  "[Width](#cfn-quicksight-template-tablefieldoption-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablefieldoption-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-template-tablefieldoption-customlabel): {{String}}
  [FieldId](#cfn-quicksight-template-tablefieldoption-fieldid): {{String}}
  [URLStyling](#cfn-quicksight-template-tablefieldoption-urlstyling): {{
    TableFieldURLConfiguration}}
  [Visibility](#cfn-quicksight-template-tablefieldoption-visibility): {{String}}
  [Width](#cfn-quicksight-template-tablefieldoption-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-tablefieldoption-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-template-tablefieldoption-customlabel"></a>
The custom label for a table field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-template-tablefieldoption-fieldid"></a>
The field ID for a table field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URLStyling`  <a name="cfn-quicksight-template-tablefieldoption-urlstyling"></a>
The URL configuration for a table field.
*Required*: No
*Type*: [TableFieldURLConfiguration](aws-properties-quicksight-template-tablefieldurlconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-tablefieldoption-visibility"></a>
The visibility of a table field.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-template-tablefieldoption-width"></a>
The width for a table field.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
