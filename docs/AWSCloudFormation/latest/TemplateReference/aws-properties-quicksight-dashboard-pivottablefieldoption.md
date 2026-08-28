---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-pivottablefieldoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard PivotTableFieldOption
<a name="aws-properties-quicksight-dashboard-pivottablefieldoption"></a>

The selected field options for the pivot table field options.

## Syntax
<a name="aws-properties-quicksight-dashboard-pivottablefieldoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-pivottablefieldoption-syntax.json"></a>

```
{
  "[CustomLabel](#cfn-quicksight-dashboard-pivottablefieldoption-customlabel)" : {{String}},
  "[FieldId](#cfn-quicksight-dashboard-pivottablefieldoption-fieldid)" : {{String}},
  "[Visibility](#cfn-quicksight-dashboard-pivottablefieldoption-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-pivottablefieldoption-syntax.yaml"></a>

```
  [CustomLabel](#cfn-quicksight-dashboard-pivottablefieldoption-customlabel): {{String}}
  [FieldId](#cfn-quicksight-dashboard-pivottablefieldoption-fieldid): {{String}}
  [Visibility](#cfn-quicksight-dashboard-pivottablefieldoption-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-pivottablefieldoption-properties"></a>

`CustomLabel`  <a name="cfn-quicksight-dashboard-pivottablefieldoption-customlabel"></a>
The custom label of the pivot table field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-dashboard-pivottablefieldoption-fieldid"></a>
The field ID of the pivot table field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-pivottablefieldoption-visibility"></a>
The visibility of the pivot table field.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
