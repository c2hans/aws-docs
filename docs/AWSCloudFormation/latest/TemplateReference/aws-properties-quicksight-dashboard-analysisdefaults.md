---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-analysisdefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard AnalysisDefaults
<a name="aws-properties-quicksight-dashboard-analysisdefaults"></a>

The configuration for default analysis settings.

## Syntax
<a name="aws-properties-quicksight-dashboard-analysisdefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-analysisdefaults-syntax.json"></a>

```
{
  "[DefaultNewSheetConfiguration](#cfn-quicksight-dashboard-analysisdefaults-defaultnewsheetconfiguration)" : {{DefaultNewSheetConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-analysisdefaults-syntax.yaml"></a>

```
  [DefaultNewSheetConfiguration](#cfn-quicksight-dashboard-analysisdefaults-defaultnewsheetconfiguration): {{
    DefaultNewSheetConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-analysisdefaults-properties"></a>

`DefaultNewSheetConfiguration`  <a name="cfn-quicksight-dashboard-analysisdefaults-defaultnewsheetconfiguration"></a>
The configuration for default new sheet settings.
*Required*: Yes
*Type*: [DefaultNewSheetConfiguration](aws-properties-quicksight-dashboard-defaultnewsheetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
