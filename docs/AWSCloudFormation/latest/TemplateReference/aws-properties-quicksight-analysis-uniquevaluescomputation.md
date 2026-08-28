---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-uniquevaluescomputation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis UniqueValuesComputation
<a name="aws-properties-quicksight-analysis-uniquevaluescomputation"></a>

The unique values computation configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-uniquevaluescomputation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-uniquevaluescomputation-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-analysis-uniquevaluescomputation-category)" : {{DimensionField}},
  "[ComputationId](#cfn-quicksight-analysis-uniquevaluescomputation-computationid)" : {{String}},
  "[Name](#cfn-quicksight-analysis-uniquevaluescomputation-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-uniquevaluescomputation-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-analysis-uniquevaluescomputation-category): {{
    DimensionField}}
  [ComputationId](#cfn-quicksight-analysis-uniquevaluescomputation-computationid): {{String}}
  [Name](#cfn-quicksight-analysis-uniquevaluescomputation-name): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-uniquevaluescomputation-properties"></a>

`Category`  <a name="cfn-quicksight-analysis-uniquevaluescomputation-category"></a>
The category field that is used in a computation.
*Required*: No
*Type*: [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationId`  <a name="cfn-quicksight-analysis-uniquevaluescomputation-computationid"></a>
The ID for a computation.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-uniquevaluescomputation-name"></a>
The name of a computation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
