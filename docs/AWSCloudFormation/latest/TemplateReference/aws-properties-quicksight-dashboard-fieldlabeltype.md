---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-fieldlabeltype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FieldLabelType
<a name="aws-properties-quicksight-dashboard-fieldlabeltype"></a>

The field label type.

## Syntax
<a name="aws-properties-quicksight-dashboard-fieldlabeltype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-fieldlabeltype-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-dashboard-fieldlabeltype-fieldid)" : {{String}},
  "[Visibility](#cfn-quicksight-dashboard-fieldlabeltype-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-fieldlabeltype-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-dashboard-fieldlabeltype-fieldid): {{String}}
  [Visibility](#cfn-quicksight-dashboard-fieldlabeltype-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-fieldlabeltype-properties"></a>

`FieldId`  <a name="cfn-quicksight-dashboard-fieldlabeltype-fieldid"></a>
Indicates the field that is targeted by the field label.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-fieldlabeltype-visibility"></a>
The visibility of the field label.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
