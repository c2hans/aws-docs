---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase KendraKnowledgeBaseConfiguration
<a name="aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration"></a>

Settings for an Amazon Kendra knowledge base.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration-syntax.json"></a>

```
{
  "[KendraIndexArn](#cfn-bedrock-knowledgebase-kendraknowledgebaseconfiguration-kendraindexarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration-syntax.yaml"></a>

```
  [KendraIndexArn](#cfn-bedrock-knowledgebase-kendraknowledgebaseconfiguration-kendraindexarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration-properties"></a>

`KendraIndexArn`  <a name="cfn-bedrock-knowledgebase-kendraknowledgebaseconfiguration-kendraindexarn"></a>
The ARN of the Amazon Kendra index.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kendra:[a-z0-9-]{1,20}:([0-9]{12}|):index/([a-zA-Z0-9][a-zA-Z0-9-]{35}|[a-zA-Z0-9][a-zA-Z0-9-]{35}-[a-zA-Z0-9][a-zA-Z0-9-]{35})$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
