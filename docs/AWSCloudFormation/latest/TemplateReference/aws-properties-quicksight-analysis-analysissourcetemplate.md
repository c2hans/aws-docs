---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-analysissourcetemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis AnalysisSourceTemplate
<a name="aws-properties-quicksight-analysis-analysissourcetemplate"></a>

The source template of an analysis.

## Syntax
<a name="aws-properties-quicksight-analysis-analysissourcetemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-analysissourcetemplate-syntax.json"></a>

```
{
  "[Arn](#cfn-quicksight-analysis-analysissourcetemplate-arn)" : {{String}},
  "[DataSetReferences](#cfn-quicksight-analysis-analysissourcetemplate-datasetreferences)" : {{[ DataSetReference, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-analysissourcetemplate-syntax.yaml"></a>

```
  [Arn](#cfn-quicksight-analysis-analysissourcetemplate-arn): {{String}}
  [DataSetReferences](#cfn-quicksight-analysis-analysissourcetemplate-datasetreferences): {{
    - DataSetReference}}
```

## Properties
<a name="aws-properties-quicksight-analysis-analysissourcetemplate-properties"></a>

`Arn`  <a name="cfn-quicksight-analysis-analysissourcetemplate-arn"></a>
The Amazon Resource Name (ARN) of the source template of an analysis.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetReferences`  <a name="cfn-quicksight-analysis-analysissourcetemplate-datasetreferences"></a>
The dataset references of the source template of an analysis.
*Required*: Yes
*Type*: Array of [DataSetReference](aws-properties-quicksight-analysis-datasetreference.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
