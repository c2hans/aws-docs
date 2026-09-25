---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-topicreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TopicReference
<a name="aws-properties-quicksight-dashboard-topicreference"></a>

Topic reference.

## Syntax
<a name="aws-properties-quicksight-dashboard-topicreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-topicreference-syntax.json"></a>

```
{
  "[TopicArn](#cfn-quicksight-dashboard-topicreference-topicarn)" : {{String}},
  "[TopicPlaceholder](#cfn-quicksight-dashboard-topicreference-topicplaceholder)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-topicreference-syntax.yaml"></a>

```
  [TopicArn](#cfn-quicksight-dashboard-topicreference-topicarn): {{String}}
  [TopicPlaceholder](#cfn-quicksight-dashboard-topicreference-topicplaceholder): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-topicreference-properties"></a>

`TopicArn`  <a name="cfn-quicksight-dashboard-topicreference-topicarn"></a>
Topic Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicPlaceholder`  <a name="cfn-quicksight-dashboard-topicreference-topicplaceholder"></a>
Topic placeholder.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
