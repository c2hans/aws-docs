---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase MongoDbAtlasConfiguration
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration"></a>

Contains details about the storage configuration of the knowledge base in MongoDB Atlas.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration-syntax.json"></a>

```
{
  "[CollectionName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-collectionname)" : {{String}},
  "[CredentialsSecretArn](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-credentialssecretarn)" : {{String}},
  "[DatabaseName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-databasename)" : {{String}},
  "[Endpoint](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-endpoint)" : {{String}},
  "[EndpointServiceName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-endpointservicename)" : {{String}},
  "[FieldMapping](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-fieldmapping)" : {{MongoDbAtlasFieldMapping}},
  "[TextIndexName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-textindexname)" : {{String}},
  "[VectorIndexName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-vectorindexname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration-syntax.yaml"></a>

```
  [CollectionName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-collectionname): {{String}}
  [CredentialsSecretArn](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-credentialssecretarn): {{String}}
  [DatabaseName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-databasename): {{String}}
  [Endpoint](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-endpoint): {{String}}
  [EndpointServiceName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-endpointservicename): {{String}}
  [FieldMapping](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-fieldmapping): {{
    MongoDbAtlasFieldMapping}}
  [TextIndexName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-textindexname): {{String}}
  [VectorIndexName](#cfn-bedrock-knowledgebase-mongodbatlasconfiguration-vectorindexname): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration-properties"></a>

`CollectionName`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-collectionname"></a>
The collection name of the knowledge base in MongoDB Atlas.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CredentialsSecretArn`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-credentialssecretarn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that contains user credentials for your MongoDB Atlas cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-databasename"></a>
The database name in your MongoDB Atlas cluster for your knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Endpoint`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-endpoint"></a>
The endpoint URL of your MongoDB Atlas cluster for your knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.mongodb\.net$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointServiceName`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-endpointservicename"></a>
The name of the VPC endpoint service in your account that is connected to your MongoDB Atlas cluster.
*Required*: No
*Type*: String
*Pattern*: `^(?:arn:aws(?:-us-gov|-cn|-iso|-iso-[a-z])*:.+:.*:\d+:.+/.+$|[a-zA-Z0-9*]+[a-zA-Z0-9._-]*)$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldMapping`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-fieldmapping"></a>
Contains the names of the fields to which to map information about the vector store.
*Required*: Yes
*Type*: [MongoDbAtlasFieldMapping](aws-properties-bedrock-knowledgebase-mongodbatlasfieldmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TextIndexName`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-textindexname"></a>
The name of the text search index in the MongoDB collection. This is required for using the hybrid search feature.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorIndexName`  <a name="cfn-bedrock-knowledgebase-mongodbatlasconfiguration-vectorindexname"></a>
The name of the MongoDB Atlas vector search index.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
