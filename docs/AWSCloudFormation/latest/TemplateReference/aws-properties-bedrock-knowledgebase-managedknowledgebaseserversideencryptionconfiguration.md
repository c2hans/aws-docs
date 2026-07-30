---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase ManagedKnowledgeBaseServerSideEncryptionConfiguration
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration"></a>

<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-description"></a>The `ManagedKnowledgeBaseServerSideEncryptionConfiguration` property type specifies Property description not available. for an [AWS::Bedrock::KnowledgeBase](aws-resource-bedrock-knowledgebase.md).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-bedrock-knowledgebase-managedknowledgebaseserversideencryptionconfiguration-kmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
