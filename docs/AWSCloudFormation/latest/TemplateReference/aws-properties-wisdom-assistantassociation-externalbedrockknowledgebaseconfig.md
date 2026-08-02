---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AssistantAssociation ExternalBedrockKnowledgeBaseConfig
<a name="aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig"></a>

Configuration for an external Bedrock knowledge base.

## Syntax
<a name="aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-syntax.json"></a>

```
{
  "[AccessRoleArn](#cfn-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-accessrolearn)" : {{String}},
  "[BedrockKnowledgeBaseArn](#cfn-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-bedrockknowledgebasearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-syntax.yaml"></a>

```
  [AccessRoleArn](#cfn-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-accessrolearn): {{String}}
  [BedrockKnowledgeBaseArn](#cfn-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-bedrockknowledgebasearn): {{String}}
```

## Properties
<a name="aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-properties"></a>

`AccessRoleArn`  <a name="cfn-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-accessrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role used to access the external Bedrock knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:iam::[0-9]{12}:role/(?:service-role/)?[a-zA-Z0-9_+=,.@-]{1,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BedrockKnowledgeBaseArn`  <a name="cfn-wisdom-assistantassociation-externalbedrockknowledgebaseconfig-bedrockknowledgebasearn"></a>
The Amazon Resource Name (ARN) of the external Bedrock knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
