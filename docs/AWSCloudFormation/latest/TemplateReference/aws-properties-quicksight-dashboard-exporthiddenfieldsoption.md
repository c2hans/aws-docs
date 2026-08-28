---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-exporthiddenfieldsoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ExportHiddenFieldsOption
<a name="aws-properties-quicksight-dashboard-exporthiddenfieldsoption"></a>

Determines if hidden fields are included in an exported dashboard.

## Syntax
<a name="aws-properties-quicksight-dashboard-exporthiddenfieldsoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-exporthiddenfieldsoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-dashboard-exporthiddenfieldsoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-exporthiddenfieldsoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-dashboard-exporthiddenfieldsoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-exporthiddenfieldsoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-dashboard-exporthiddenfieldsoption-availabilitystatus"></a>
The status of the export hidden fields options of a dashbaord.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
