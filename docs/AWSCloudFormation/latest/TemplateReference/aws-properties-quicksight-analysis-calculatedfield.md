---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-calculatedfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CalculatedField
<a name="aws-properties-quicksight-analysis-calculatedfield"></a>

The calculated field of an analysis.

## Syntax
<a name="aws-properties-quicksight-analysis-calculatedfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-calculatedfield-syntax.json"></a>

```
{
  "[DataSetIdentifier](#cfn-quicksight-analysis-calculatedfield-datasetidentifier)" : {{String}},
  "[Expression](#cfn-quicksight-analysis-calculatedfield-expression)" : {{String}},
  "[Name](#cfn-quicksight-analysis-calculatedfield-name)" : {{String}},
  "[TopicIdentifier](#cfn-quicksight-analysis-calculatedfield-topicidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-calculatedfield-syntax.yaml"></a>

```
  [DataSetIdentifier](#cfn-quicksight-analysis-calculatedfield-datasetidentifier): {{String}}
  [Expression](#cfn-quicksight-analysis-calculatedfield-expression): {{String}}
  [Name](#cfn-quicksight-analysis-calculatedfield-name): {{String}}
  [TopicIdentifier](#cfn-quicksight-analysis-calculatedfield-topicidentifier): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-calculatedfield-properties"></a>

`DataSetIdentifier`  <a name="cfn-quicksight-analysis-calculatedfield-datasetidentifier"></a>
The data set that is used in this calculated field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-analysis-calculatedfield-expression"></a>
The expression of the calculated field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-analysis-calculatedfield-name"></a>
The name of the calculated field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicIdentifier`  <a name="cfn-quicksight-analysis-calculatedfield-topicidentifier"></a>
The topic that is used in this calculated field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
