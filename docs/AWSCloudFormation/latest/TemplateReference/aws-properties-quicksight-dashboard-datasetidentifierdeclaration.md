---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-datasetidentifierdeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DataSetIdentifierDeclaration
<a name="aws-properties-quicksight-dashboard-datasetidentifierdeclaration"></a>

A data set.

## Syntax
<a name="aws-properties-quicksight-dashboard-datasetidentifierdeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-datasetidentifierdeclaration-syntax.json"></a>

```
{
  "[DataSetArn](#cfn-quicksight-dashboard-datasetidentifierdeclaration-datasetarn)" : {{String}},
  "[Identifier](#cfn-quicksight-dashboard-datasetidentifierdeclaration-identifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-datasetidentifierdeclaration-syntax.yaml"></a>

```
  [DataSetArn](#cfn-quicksight-dashboard-datasetidentifierdeclaration-datasetarn): {{String}}
  [Identifier](#cfn-quicksight-dashboard-datasetidentifierdeclaration-identifier): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-datasetidentifierdeclaration-properties"></a>

`DataSetArn`  <a name="cfn-quicksight-dashboard-datasetidentifierdeclaration-datasetarn"></a>
The Amazon Resource Name (ARN) of the data set.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identifier`  <a name="cfn-quicksight-dashboard-datasetidentifierdeclaration-identifier"></a>
The identifier of the data set, typically the data set's name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
