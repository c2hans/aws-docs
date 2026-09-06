---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-pineconeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase PineconeConfiguration
<a name="aws-properties-bedrock-knowledgebase-pineconeconfiguration"></a>

Contains details about the storage configuration of the knowledge base in Pinecone. For more information, see [Create a vector index in Pinecone](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-pinecone.html).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-pineconeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-pineconeconfiguration-syntax.json"></a>

```
{
  "[ConnectionString](#cfn-bedrock-knowledgebase-pineconeconfiguration-connectionstring)" : {{String}},
  "[CredentialsSecretArn](#cfn-bedrock-knowledgebase-pineconeconfiguration-credentialssecretarn)" : {{String}},
  "[FieldMapping](#cfn-bedrock-knowledgebase-pineconeconfiguration-fieldmapping)" : {{PineconeFieldMapping}},
  "[Namespace](#cfn-bedrock-knowledgebase-pineconeconfiguration-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-pineconeconfiguration-syntax.yaml"></a>

```
  [ConnectionString](#cfn-bedrock-knowledgebase-pineconeconfiguration-connectionstring): {{
    String}}
  [CredentialsSecretArn](#cfn-bedrock-knowledgebase-pineconeconfiguration-credentialssecretarn): {{String}}
  [FieldMapping](#cfn-bedrock-knowledgebase-pineconeconfiguration-fieldmapping): {{
    PineconeFieldMapping}}
  [Namespace](#cfn-bedrock-knowledgebase-pineconeconfiguration-namespace): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-pineconeconfiguration-properties"></a>

`ConnectionString`  <a name="cfn-bedrock-knowledgebase-pineconeconfiguration-connectionstring"></a>
The endpoint URL for your index management page.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CredentialsSecretArn`  <a name="cfn-bedrock-knowledgebase-pineconeconfiguration-credentialssecretarn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that is linked to your Pinecone API key.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldMapping`  <a name="cfn-bedrock-knowledgebase-pineconeconfiguration-fieldmapping"></a>
Contains the names of the fields to which to map information about the vector store.
*Required*: Yes
*Type*: [PineconeFieldMapping](aws-properties-bedrock-knowledgebase-pineconefieldmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-bedrock-knowledgebase-pineconeconfiguration-namespace"></a>
The namespace to be used to write new data to your database.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
