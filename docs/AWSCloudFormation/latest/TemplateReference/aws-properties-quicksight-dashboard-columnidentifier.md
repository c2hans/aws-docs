---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-columnidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ColumnIdentifier
<a name="aws-properties-quicksight-dashboard-columnidentifier"></a>

A column of a data set.

## Syntax
<a name="aws-properties-quicksight-dashboard-columnidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-columnidentifier-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dashboard-columnidentifier-columnname)" : {{String}},
  "[DataSetIdentifier](#cfn-quicksight-dashboard-columnidentifier-datasetidentifier)" : {{String}},
  "[TopicIdentifier](#cfn-quicksight-dashboard-columnidentifier-topicidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-columnidentifier-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dashboard-columnidentifier-columnname): {{String}}
  [DataSetIdentifier](#cfn-quicksight-dashboard-columnidentifier-datasetidentifier): {{String}}
  [TopicIdentifier](#cfn-quicksight-dashboard-columnidentifier-topicidentifier): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-columnidentifier-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dashboard-columnidentifier-columnname"></a>
The name of the column.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-dashboard-columnidentifier-datasetidentifier"></a>
The data set that the column belongs to.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicIdentifier`  <a name="cfn-quicksight-dashboard-columnidentifier-topicidentifier"></a>
The topic that the column belongs to.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
