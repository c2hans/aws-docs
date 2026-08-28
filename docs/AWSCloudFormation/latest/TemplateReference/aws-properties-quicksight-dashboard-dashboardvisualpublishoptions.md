---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dashboardvisualpublishoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DashboardVisualPublishOptions
<a name="aws-properties-quicksight-dashboard-dashboardvisualpublishoptions"></a>

The visual publish options of a visual in a dashboard

## Syntax
<a name="aws-properties-quicksight-dashboard-dashboardvisualpublishoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dashboardvisualpublishoptions-syntax.json"></a>

```
{
  "[ExportHiddenFieldsOption](#cfn-quicksight-dashboard-dashboardvisualpublishoptions-exporthiddenfieldsoption)" : {{ExportHiddenFieldsOption}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dashboardvisualpublishoptions-syntax.yaml"></a>

```
  [ExportHiddenFieldsOption](#cfn-quicksight-dashboard-dashboardvisualpublishoptions-exporthiddenfieldsoption): {{
    ExportHiddenFieldsOption}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dashboardvisualpublishoptions-properties"></a>

`ExportHiddenFieldsOption`  <a name="cfn-quicksight-dashboard-dashboardvisualpublishoptions-exporthiddenfieldsoption"></a>
Determines if hidden fields are included in an exported dashboard.
*Required*: No
*Type*: [ExportHiddenFieldsOption](aws-properties-quicksight-dashboard-exporthiddenfieldsoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
