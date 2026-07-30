---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-fieldforreranking.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FieldForReranking
<a name="aws-properties-bedrock-flowversion-fieldforreranking"></a>

Specifies a field to be used during the reranking process in a Knowledge Base vector search. This structure identifies metadata fields that should be considered when reordering search results to improve relevance.

## Syntax
<a name="aws-properties-bedrock-flowversion-fieldforreranking-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-fieldforreranking-syntax.json"></a>

```
{
  "[FieldName](#cfn-bedrock-flowversion-fieldforreranking-fieldname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-fieldforreranking-syntax.yaml"></a>

```
  [FieldName](#cfn-bedrock-flowversion-fieldforreranking-fieldname): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-fieldforreranking-properties"></a>

`FieldName`  <a name="cfn-bedrock-flowversion-fieldforreranking-fieldname"></a>
The name of the metadata field to be used during the reranking process.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
