---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-mappeddatasetparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard MappedDataSetParameter
<a name="aws-properties-quicksight-dashboard-mappeddatasetparameter"></a>

A dataset parameter that is mapped to an analysis parameter.

## Syntax
<a name="aws-properties-quicksight-dashboard-mappeddatasetparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-mappeddatasetparameter-syntax.json"></a>

```
{
  "[DataSetIdentifier](#cfn-quicksight-dashboard-mappeddatasetparameter-datasetidentifier)" : {{String}},
  "[DataSetParameterName](#cfn-quicksight-dashboard-mappeddatasetparameter-datasetparametername)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-mappeddatasetparameter-syntax.yaml"></a>

```
  [DataSetIdentifier](#cfn-quicksight-dashboard-mappeddatasetparameter-datasetidentifier): {{String}}
  [DataSetParameterName](#cfn-quicksight-dashboard-mappeddatasetparameter-datasetparametername): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-mappeddatasetparameter-properties"></a>

`DataSetIdentifier`  <a name="cfn-quicksight-dashboard-mappeddatasetparameter-datasetidentifier"></a>
A unique name that identifies a dataset within the analysis or dashboard.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetParameterName`  <a name="cfn-quicksight-dashboard-mappeddatasetparameter-datasetparametername"></a>
The name of the dataset parameter.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
