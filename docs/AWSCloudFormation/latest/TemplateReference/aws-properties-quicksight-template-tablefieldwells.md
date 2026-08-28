---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablefieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableFieldWells
<a name="aws-properties-quicksight-template-tablefieldwells"></a>

The field wells for a table visual.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-tablefieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablefieldwells-syntax.json"></a>

```
{
  "[TableAggregatedFieldWells](#cfn-quicksight-template-tablefieldwells-tableaggregatedfieldwells)" : {{TableAggregatedFieldWells}},
  "[TableUnaggregatedFieldWells](#cfn-quicksight-template-tablefieldwells-tableunaggregatedfieldwells)" : {{TableUnaggregatedFieldWells}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablefieldwells-syntax.yaml"></a>

```
  [TableAggregatedFieldWells](#cfn-quicksight-template-tablefieldwells-tableaggregatedfieldwells): {{
    TableAggregatedFieldWells}}
  [TableUnaggregatedFieldWells](#cfn-quicksight-template-tablefieldwells-tableunaggregatedfieldwells): {{
    TableUnaggregatedFieldWells}}
```

## Properties
<a name="aws-properties-quicksight-template-tablefieldwells-properties"></a>

`TableAggregatedFieldWells`  <a name="cfn-quicksight-template-tablefieldwells-tableaggregatedfieldwells"></a>
The aggregated field well for the table.
*Required*: No
*Type*: [TableAggregatedFieldWells](aws-properties-quicksight-template-tableaggregatedfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableUnaggregatedFieldWells`  <a name="cfn-quicksight-template-tablefieldwells-tableunaggregatedfieldwells"></a>
The unaggregated field well for the table.
*Required*: No
*Type*: [TableUnaggregatedFieldWells](aws-properties-quicksight-template-tableunaggregatedfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
