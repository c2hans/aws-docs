---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-decimalplacesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DecimalPlacesConfiguration
<a name="aws-properties-quicksight-dashboard-decimalplacesconfiguration"></a>

The option that determines the decimal places configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-decimalplacesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-decimalplacesconfiguration-syntax.json"></a>

```
{
  "[DecimalPlaces](#cfn-quicksight-dashboard-decimalplacesconfiguration-decimalplaces)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-decimalplacesconfiguration-syntax.yaml"></a>

```
  [DecimalPlaces](#cfn-quicksight-dashboard-decimalplacesconfiguration-decimalplaces): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-decimalplacesconfiguration-properties"></a>

`DecimalPlaces`  <a name="cfn-quicksight-dashboard-decimalplacesconfiguration-decimalplaces"></a>
The values of the decimal places.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
