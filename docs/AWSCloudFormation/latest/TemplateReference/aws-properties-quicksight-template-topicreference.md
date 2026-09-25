---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-topicreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TopicReference
<a name="aws-properties-quicksight-template-topicreference"></a>

Topic reference.

## Syntax
<a name="aws-properties-quicksight-template-topicreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-topicreference-syntax.json"></a>

```
{
  "[TopicArn](#cfn-quicksight-template-topicreference-topicarn)" : {{String}},
  "[TopicPlaceholder](#cfn-quicksight-template-topicreference-topicplaceholder)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-topicreference-syntax.yaml"></a>

```
  [TopicArn](#cfn-quicksight-template-topicreference-topicarn): {{String}}
  [TopicPlaceholder](#cfn-quicksight-template-topicreference-topicplaceholder): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-topicreference-properties"></a>

`TopicArn`  <a name="cfn-quicksight-template-topicreference-topicarn"></a>
Topic Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicPlaceholder`  <a name="cfn-quicksight-template-topicreference-topicplaceholder"></a>
Topic placeholder.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
