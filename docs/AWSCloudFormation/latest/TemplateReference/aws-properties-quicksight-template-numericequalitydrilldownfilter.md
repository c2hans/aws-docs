---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-numericequalitydrilldownfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template NumericEqualityDrillDownFilter
<a name="aws-properties-quicksight-template-numericequalitydrilldownfilter"></a>

The numeric equality type drill down filter.

## Syntax
<a name="aws-properties-quicksight-template-numericequalitydrilldownfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-numericequalitydrilldownfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-template-numericequalitydrilldownfilter-column)" : {{ColumnIdentifier}},
  "[Value](#cfn-quicksight-template-numericequalitydrilldownfilter-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-numericequalitydrilldownfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-template-numericequalitydrilldownfilter-column): {{
    ColumnIdentifier}}
  [Value](#cfn-quicksight-template-numericequalitydrilldownfilter-value): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-numericequalitydrilldownfilter-properties"></a>

`Column`  <a name="cfn-quicksight-template-numericequalitydrilldownfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-template-numericequalitydrilldownfilter-value"></a>
The value of the double input numeric drill down filter.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
