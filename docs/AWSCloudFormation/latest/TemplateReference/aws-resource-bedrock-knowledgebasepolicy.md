---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-knowledgebasepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBasePolicy
<a name="aws-resource-bedrock-knowledgebasepolicy"></a>

<a name="aws-resource-bedrock-knowledgebasepolicy-description"></a>The `AWS::Bedrock::KnowledgeBasePolicy` resource Property description not available. for Bedrock.

## Syntax
<a name="aws-resource-bedrock-knowledgebasepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-knowledgebasepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::KnowledgeBasePolicy",
  "Properties" : {
      "[KnowledgeBaseId](#cfn-bedrock-knowledgebasepolicy-knowledgebaseid)" : {{String}},
      "[PolicyDocument](#cfn-bedrock-knowledgebasepolicy-policydocument)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-knowledgebasepolicy-syntax.yaml"></a>

```
Type: AWS::Bedrock::KnowledgeBasePolicy
Properties:
  [KnowledgeBaseId](#cfn-bedrock-knowledgebasepolicy-knowledgebaseid): {{String}}
  [PolicyDocument](#cfn-bedrock-knowledgebasepolicy-policydocument): {{Json}}
```

## Properties
<a name="aws-resource-bedrock-knowledgebasepolicy-properties"></a>

`KnowledgeBaseId`  <a name="cfn-bedrock-knowledgebasepolicy-knowledgebaseid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]+$`
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDocument`  <a name="cfn-bedrock-knowledgebasepolicy-policydocument"></a>
Property description not available.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-knowledgebasepolicy-return-values"></a>

### Ref
<a name="aws-resource-bedrock-knowledgebasepolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-knowledgebasepolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-knowledgebasepolicy-return-values-fn--getatt-fn--getatt"></a>

`RevisionId`  <a name="RevisionId-fn::getatt"></a>
Property description not available.
