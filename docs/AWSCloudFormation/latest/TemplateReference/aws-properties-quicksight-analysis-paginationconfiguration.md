---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-paginationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PaginationConfiguration
<a name="aws-properties-quicksight-analysis-paginationconfiguration"></a>

The pagination configuration for a table visual or boxplot.

## Syntax
<a name="aws-properties-quicksight-analysis-paginationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-paginationconfiguration-syntax.json"></a>

```
{
  "[PageNumber](#cfn-quicksight-analysis-paginationconfiguration-pagenumber)" : {{Number}},
  "[PageSize](#cfn-quicksight-analysis-paginationconfiguration-pagesize)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-paginationconfiguration-syntax.yaml"></a>

```
  [PageNumber](#cfn-quicksight-analysis-paginationconfiguration-pagenumber): {{
    Number}}
  [PageSize](#cfn-quicksight-analysis-paginationconfiguration-pagesize): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-paginationconfiguration-properties"></a>

`PageNumber`  <a name="cfn-quicksight-analysis-paginationconfiguration-pagenumber"></a>
Indicates the page number.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageSize`  <a name="cfn-quicksight-analysis-paginationconfiguration-pagesize"></a>
Indicates how many items render in one page.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
