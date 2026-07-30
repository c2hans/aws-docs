---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-storageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase StorageConfiguration
<a name="aws-properties-bedrock-knowledgebase-storageconfiguration"></a>

Contains the storage configuration of the knowledge base.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-storageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-storageconfiguration-syntax.json"></a>

```
{
  "[MongoDbAtlasConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-mongodbatlasconfiguration)" : {{MongoDbAtlasConfiguration}},
  "[NeptuneAnalyticsConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-neptuneanalyticsconfiguration)" : {{NeptuneAnalyticsConfiguration}},
  "[OpensearchManagedClusterConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-opensearchmanagedclusterconfiguration)" : {{OpenSearchManagedClusterConfiguration}},
  "[OpensearchServerlessConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-opensearchserverlessconfiguration)" : {{OpenSearchServerlessConfiguration}},
  "[PineconeConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-pineconeconfiguration)" : {{PineconeConfiguration}},
  "[RdsConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-rdsconfiguration)" : {{RdsConfiguration}},
  "[S3VectorsConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-s3vectorsconfiguration)" : {{S3VectorsConfiguration}},
  "[Type](#cfn-bedrock-knowledgebase-storageconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-storageconfiguration-syntax.yaml"></a>

```
  [MongoDbAtlasConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-mongodbatlasconfiguration): {{
    MongoDbAtlasConfiguration}}
  [NeptuneAnalyticsConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-neptuneanalyticsconfiguration): {{
    NeptuneAnalyticsConfiguration}}
  [OpensearchManagedClusterConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-opensearchmanagedclusterconfiguration): {{
    OpenSearchManagedClusterConfiguration}}
  [OpensearchServerlessConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-opensearchserverlessconfiguration): {{
    OpenSearchServerlessConfiguration}}
  [PineconeConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-pineconeconfiguration): {{
    PineconeConfiguration}}
  [RdsConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-rdsconfiguration): {{
    RdsConfiguration}}
  [S3VectorsConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration-s3vectorsconfiguration): {{
    S3VectorsConfiguration}}
  [Type](#cfn-bedrock-knowledgebase-storageconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-storageconfiguration-properties"></a>

`MongoDbAtlasConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-mongodbatlasconfiguration"></a>
Contains the storage configuration of the knowledge base in MongoDB Atlas.
*Required*: No
*Type*: [MongoDbAtlasConfiguration](aws-properties-bedrock-knowledgebase-mongodbatlasconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NeptuneAnalyticsConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-neptuneanalyticsconfiguration"></a>
Contains details about the Neptune Analytics configuration of the knowledge base in Amazon Neptune. For more information, see [Create a vector index in Amazon Neptune Analytics.](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html).
*Required*: No
*Type*: [NeptuneAnalyticsConfiguration](aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OpensearchManagedClusterConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-opensearchmanagedclusterconfiguration"></a>
Contains details about the storage configuration of the knowledge base in OpenSearch Managed Cluster. For more information, see [Create a vector index in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html).
*Required*: No
*Type*: [OpenSearchManagedClusterConfiguration](aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OpensearchServerlessConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-opensearchserverlessconfiguration"></a>
Contains the storage configuration of the knowledge base in Amazon OpenSearch Service.
*Required*: No
*Type*: [OpenSearchServerlessConfiguration](aws-properties-bedrock-knowledgebase-opensearchserverlessconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PineconeConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-pineconeconfiguration"></a>
Contains the storage configuration of the knowledge base in Pinecone.
*Required*: No
*Type*: [PineconeConfiguration](aws-properties-bedrock-knowledgebase-pineconeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RdsConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-rdsconfiguration"></a>
Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see [Create a vector index in Amazon RDS](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html).
*Required*: No
*Type*: [RdsConfiguration](aws-properties-bedrock-knowledgebase-rdsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3VectorsConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-s3vectorsconfiguration"></a>
The configuration settings for storing knowledge base data using S3 vectors. This includes vector index information and S3 bucket details for vector storage.
*Required*: No
*Type*: [S3VectorsConfiguration](aws-properties-bedrock-knowledgebase-s3vectorsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-bedrock-knowledgebase-storageconfiguration-type"></a>
The vector store service in which the knowledge base is stored.
*Required*: Yes
*Type*: String
*Allowed values*: `OPENSEARCH_SERVERLESS | PINECONE | RDS | MONGO_DB_ATLAS | NEPTUNE_ANALYTICS | S3_VECTORS | OPENSEARCH_MANAGED_CLUSTER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
