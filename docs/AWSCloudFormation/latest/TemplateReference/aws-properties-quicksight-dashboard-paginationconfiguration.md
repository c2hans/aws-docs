---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-paginationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard PaginationConfiguration
<a name="aws-properties-quicksight-dashboard-paginationconfiguration"></a>

The pagination configuration for a table visual or boxplot.

## Syntax
<a name="aws-properties-quicksight-dashboard-paginationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-paginationconfiguration-syntax.json"></a>

```
{
  "[PageNumber](#cfn-quicksight-dashboard-paginationconfiguration-pagenumber)" : {{Number}},
  "[PageSize](#cfn-quicksight-dashboard-paginationconfiguration-pagesize)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-paginationconfiguration-syntax.yaml"></a>

```
  [PageNumber](#cfn-quicksight-dashboard-paginationconfiguration-pagenumber): {{
    Number}}
  [PageSize](#cfn-quicksight-dashboard-paginationconfiguration-pagesize): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-paginationconfiguration-properties"></a>

`PageNumber`  <a name="cfn-quicksight-dashboard-paginationconfiguration-pagenumber"></a>
Indicates the page number.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageSize`  <a name="cfn-quicksight-dashboard-paginationconfiguration-pagesize"></a>
Indicates how many items render in one page.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
