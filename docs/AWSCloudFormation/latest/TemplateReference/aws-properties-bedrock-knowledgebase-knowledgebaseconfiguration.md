---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase KnowledgeBaseConfiguration
<a name="aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration"></a>

Configurations to apply to a knowledge base attached to the agent during query. For more information, see [Knowledge base retrieval configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html#session-state-kb).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration-syntax.json"></a>

```
{
  "[KendraKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-kendraknowledgebaseconfiguration)" : {{KendraKnowledgeBaseConfiguration}},
  "[ManagedKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-managedknowledgebaseconfiguration)" : {{ManagedKnowledgeBaseConfiguration}},
  "[SqlKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-sqlknowledgebaseconfiguration)" : {{SqlKnowledgeBaseConfiguration}},
  "[Type](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-type)" : {{String}},
  "[VectorKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-vectorknowledgebaseconfiguration)" : {{VectorKnowledgeBaseConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration-syntax.yaml"></a>

```
  [KendraKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-kendraknowledgebaseconfiguration): {{
    KendraKnowledgeBaseConfiguration}}
  [ManagedKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-managedknowledgebaseconfiguration): {{
    ManagedKnowledgeBaseConfiguration}}
  [SqlKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-sqlknowledgebaseconfiguration): {{
    SqlKnowledgeBaseConfiguration}}
  [Type](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-type): {{String}}
  [VectorKnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration-vectorknowledgebaseconfiguration): {{
    VectorKnowledgeBaseConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration-properties"></a>

`KendraKnowledgeBaseConfiguration`  <a name="cfn-bedrock-knowledgebase-knowledgebaseconfiguration-kendraknowledgebaseconfiguration"></a>
Settings for an Amazon Kendra knowledge base.
*Required*: No
*Type*: [KendraKnowledgeBaseConfiguration](aws-properties-bedrock-knowledgebase-kendraknowledgebaseconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedKnowledgeBaseConfiguration`  <a name="cfn-bedrock-knowledgebase-knowledgebaseconfiguration-managedknowledgebaseconfiguration"></a>
Contains configuration details for a knowledge base that uses a vector store fully managed by Amazon Bedrock. Specify this object when the knowledge base type is MANAGED.
*Required*: No
*Type*: [ManagedKnowledgeBaseConfiguration](aws-properties-bedrock-knowledgebase-managedknowledgebaseconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SqlKnowledgeBaseConfiguration`  <a name="cfn-bedrock-knowledgebase-knowledgebaseconfiguration-sqlknowledgebaseconfiguration"></a>
Specifies configurations for a knowledge base connected to an SQL database.
*Required*: No
*Type*: [SqlKnowledgeBaseConfiguration](aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-knowledgebase-knowledgebaseconfiguration-type"></a>
The type of data that the data source is converted into for the knowledge base. Choose `MANAGED` to create a managed knowledge base.
*Required*: Yes
*Type*: String
*Allowed values*: `VECTOR | KENDRA | SQL | MANAGED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorKnowledgeBaseConfiguration`  <a name="cfn-bedrock-knowledgebase-knowledgebaseconfiguration-vectorknowledgebaseconfiguration"></a>
Contains details about the model that's used to convert the data source into vector embeddings.
*Required*: No
*Type*: [VectorKnowledgeBaseConfiguration](aws-properties-bedrock-knowledgebase-vectorknowledgebaseconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
