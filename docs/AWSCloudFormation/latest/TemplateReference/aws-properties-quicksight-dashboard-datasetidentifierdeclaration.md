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
