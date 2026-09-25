---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-topicidentifierdeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TopicIdentifierDeclaration
<a name="aws-properties-quicksight-dashboard-topicidentifierdeclaration"></a>

A topic.

## Syntax
<a name="aws-properties-quicksight-dashboard-topicidentifierdeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-topicidentifierdeclaration-syntax.json"></a>

```
{
  "[Identifier](#cfn-quicksight-dashboard-topicidentifierdeclaration-identifier)" : {{String}},
  "[TopicArn](#cfn-quicksight-dashboard-topicidentifierdeclaration-topicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-topicidentifierdeclaration-syntax.yaml"></a>

```
  [Identifier](#cfn-quicksight-dashboard-topicidentifierdeclaration-identifier): {{String}}
  [TopicArn](#cfn-quicksight-dashboard-topicidentifierdeclaration-topicarn): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-topicidentifierdeclaration-properties"></a>

`Identifier`  <a name="cfn-quicksight-dashboard-topicidentifierdeclaration-identifier"></a>
The identifier of the topic, typically the topic's name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-quicksight-dashboard-topicidentifierdeclaration-topicarn"></a>
The Amazon Resource Name (ARN) of the topic.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
