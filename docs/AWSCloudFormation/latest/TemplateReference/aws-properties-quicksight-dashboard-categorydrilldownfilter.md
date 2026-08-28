---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-categorydrilldownfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CategoryDrillDownFilter
<a name="aws-properties-quicksight-dashboard-categorydrilldownfilter"></a>

The category drill down filter.

## Syntax
<a name="aws-properties-quicksight-dashboard-categorydrilldownfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-categorydrilldownfilter-syntax.json"></a>

```
{
  "[CategoryValues](#cfn-quicksight-dashboard-categorydrilldownfilter-categoryvalues)" : {{[ String, ... ]}},
  "[Column](#cfn-quicksight-dashboard-categorydrilldownfilter-column)" : {{ColumnIdentifier}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-categorydrilldownfilter-syntax.yaml"></a>

```
  [CategoryValues](#cfn-quicksight-dashboard-categorydrilldownfilter-categoryvalues): {{
    - String}}
  [Column](#cfn-quicksight-dashboard-categorydrilldownfilter-column): {{
    ColumnIdentifier}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-categorydrilldownfilter-properties"></a>

`CategoryValues`  <a name="cfn-quicksight-dashboard-categorydrilldownfilter-categoryvalues"></a>
A list of the string inputs that are the values of the category drill down filter.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Column`  <a name="cfn-quicksight-dashboard-categorydrilldownfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
