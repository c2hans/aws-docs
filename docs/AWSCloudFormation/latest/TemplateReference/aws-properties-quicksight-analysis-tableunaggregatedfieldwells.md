---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-tableunaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TableUnaggregatedFieldWells
<a name="aws-properties-quicksight-analysis-tableunaggregatedfieldwells"></a>

The unaggregated field well for the table.

## Syntax
<a name="aws-properties-quicksight-analysis-tableunaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-tableunaggregatedfieldwells-syntax.json"></a>

```
{
  "[Values](#cfn-quicksight-analysis-tableunaggregatedfieldwells-values)" : {{[ UnaggregatedField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-tableunaggregatedfieldwells-syntax.yaml"></a>

```
  [Values](#cfn-quicksight-analysis-tableunaggregatedfieldwells-values): {{
    - UnaggregatedField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-tableunaggregatedfieldwells-properties"></a>

`Values`  <a name="cfn-quicksight-analysis-tableunaggregatedfieldwells-values"></a>
The values field well for a pivot table. Values are unaggregated for an unaggregated table.
*Required*: No
*Type*: Array of [UnaggregatedField](aws-properties-quicksight-analysis-unaggregatedfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
