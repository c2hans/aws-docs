---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-donutcenteroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DonutCenterOptions
<a name="aws-properties-quicksight-template-donutcenteroptions"></a>

The label options of the label that is displayed in the center of a donut chart. This option isn't available for pie charts.

## Syntax
<a name="aws-properties-quicksight-template-donutcenteroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-donutcenteroptions-syntax.json"></a>

```
{
  "[LabelVisibility](#cfn-quicksight-template-donutcenteroptions-labelvisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-donutcenteroptions-syntax.yaml"></a>

```
  [LabelVisibility](#cfn-quicksight-template-donutcenteroptions-labelvisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-donutcenteroptions-properties"></a>

`LabelVisibility`  <a name="cfn-quicksight-template-donutcenteroptions-labelvisibility"></a>
Determines the visibility of the label in a donut chart. In the Quick Sight console, this option is called `'Show total'`.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
