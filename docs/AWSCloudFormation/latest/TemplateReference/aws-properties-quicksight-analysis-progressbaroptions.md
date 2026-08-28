---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-progressbaroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ProgressBarOptions
<a name="aws-properties-quicksight-analysis-progressbaroptions"></a>

The options that determine the presentation of the progress bar of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-analysis-progressbaroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-progressbaroptions-syntax.json"></a>

```
{
  "[Visibility](#cfn-quicksight-analysis-progressbaroptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-progressbaroptions-syntax.yaml"></a>

```
  [Visibility](#cfn-quicksight-analysis-progressbaroptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-progressbaroptions-properties"></a>

`Visibility`  <a name="cfn-quicksight-analysis-progressbaroptions-visibility"></a>
The visibility of the progress bar.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
