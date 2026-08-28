---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topicv2-datasetrelationendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::TopicV2 DataSetRelationEndpoint
<a name="aws-properties-quicksight-topicv2-datasetrelationendpoint"></a>

<a name="aws-properties-quicksight-topicv2-datasetrelationendpoint-description"></a>The `DataSetRelationEndpoint` property type specifies Property description not available. for an [AWS::QuickSight::TopicV2](aws-resource-quicksight-topicv2.md).

## Syntax
<a name="aws-properties-quicksight-topicv2-datasetrelationendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topicv2-datasetrelationendpoint-syntax.json"></a>

```
{
  "[ColumnNames](#cfn-quicksight-topicv2-datasetrelationendpoint-columnnames)" : {{[ String, ... ]}},
  "[DataSetArn](#cfn-quicksight-topicv2-datasetrelationendpoint-datasetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topicv2-datasetrelationendpoint-syntax.yaml"></a>

```
  [ColumnNames](#cfn-quicksight-topicv2-datasetrelationendpoint-columnnames): {{
    - String}}
  [DataSetArn](#cfn-quicksight-topicv2-datasetrelationendpoint-datasetarn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topicv2-datasetrelationendpoint-properties"></a>

`ColumnNames`  <a name="cfn-quicksight-topicv2-datasetrelationendpoint-columnnames"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetArn`  <a name="cfn-quicksight-topicv2-datasetrelationendpoint-datasetarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
