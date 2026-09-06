---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-knowledgebase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase
<a name="aws-resource-bedrock-knowledgebase"></a>

Specifies a knowledge base as a resource in a top-level template. Minimally, you must specify the following properties:
+ Name – Specify a name for the knowledge base.
+ RoleArn – Specify the Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base. For more information, see [Create a service role for Knowledge base for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html).
+ KnowledgeBaseConfiguration – Specify the embeddings configuration of the knowledge base. The following sub-properties are required:
  + Type – Specify the value `VECTOR`.
+ StorageConfiguration – Specify information about the vector store in which the data source is stored. The following sub-properties are required:
  + Type – Specify the vector store service that you are using.
**Note**
Redis Enterprise Cloud vector stores are currently unsupported in CloudFormation.

For more information about using knowledge bases in Amazon Bedrock, see [Knowledge base for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrock-knowledgebase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-knowledgebase-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::KnowledgeBase",
  "Properties" : {
      "[Description](#cfn-bedrock-knowledgebase-description)" : {{String}},
      "[KnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration)" : {{KnowledgeBaseConfiguration}},
      "[Name](#cfn-bedrock-knowledgebase-name)" : {{String}},
      "[RoleArn](#cfn-bedrock-knowledgebase-rolearn)" : {{String}},
      "[StorageConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration)" : {{StorageConfiguration}},
      "[Tags](#cfn-bedrock-knowledgebase-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-knowledgebase-syntax.yaml"></a>

```
Type: AWS::Bedrock::KnowledgeBase
Properties:
  [Description](#cfn-bedrock-knowledgebase-description): {{String}}
  [KnowledgeBaseConfiguration](#cfn-bedrock-knowledgebase-knowledgebaseconfiguration): {{
    KnowledgeBaseConfiguration}}
  [Name](#cfn-bedrock-knowledgebase-name): {{String}}
  [RoleArn](#cfn-bedrock-knowledgebase-rolearn): {{String}}
  [StorageConfiguration](#cfn-bedrock-knowledgebase-storageconfiguration): {{
    StorageConfiguration}}
  [Tags](#cfn-bedrock-knowledgebase-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrock-knowledgebase-properties"></a>

`Description`  <a name="cfn-bedrock-knowledgebase-description"></a>
 The description of the knowledge base associated with the inline agent.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseConfiguration`  <a name="cfn-bedrock-knowledgebase-knowledgebaseconfiguration"></a>
Contains details about the embeddings configuration of the knowledge base.
*Required*: Yes
*Type*: [KnowledgeBaseConfiguration](aws-properties-bedrock-knowledgebase-knowledgebaseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-knowledgebase-name"></a>
The name of the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-bedrock-knowledgebase-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfiguration`  <a name="cfn-bedrock-knowledgebase-storageconfiguration"></a>
Contains details about the storage configuration of the knowledge base.
*Required*: No
*Type*: [StorageConfiguration](aws-properties-bedrock-knowledgebase-storageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-knowledgebase-tags"></a>
Metadata that you can assign to a resource as key-value pairs. For more information, see the following resources:
+  [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions)
+  [Tagging best practices](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices)
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-knowledgebase-return-values"></a>

### Ref
<a name="aws-resource-bedrock-knowledgebase-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the knowledge base ID.

For example, `{ "Ref": "myKnowledgeBase" }` could return the value `"KB12345678"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-knowledgebase-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-knowledgebase-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the knowledge base was created.

`FailureReasons`  <a name="FailureReasons-fn::getatt"></a>
A list of reasons that the API operation on the knowledge base failed.

`KnowledgeBaseArn`  <a name="KnowledgeBaseArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the knowledge base.

`KnowledgeBaseId`  <a name="KnowledgeBaseId-fn::getatt"></a>
 The unique identifier for a knowledge base associated with the inline agent.

`Status`  <a name="Status-fn::getatt"></a>
The status of the knowledge base.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time the knowledge base was last updated.

## Examples
<a name="aws-resource-bedrock-knowledgebase--examples"></a>

The following examples provide example templates for creating knowledge bases in different vector stores.

**Note**
Redis Enterprise Cloud vector stores are currently unsupported in CloudFormation.

**Topics**
+ [Create a knowledge base in an Amazon OpenSearch Serverless vector collection.](#aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_OpenSearch_Serverless_vector_collection.)
+ [Create a knowledge base in an Amazon Aurora database cluster.](#aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_Aurora_database_cluster.)
+ [Create a knowledge base in a Pinecone index.](#aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_a_Pinecone_index.)

### Create a knowledge base in an Amazon OpenSearch Serverless vector collection.
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_OpenSearch_Serverless_vector_collection."></a>

The following example creates a knowledge base in a vector index within an Amazon OpenSearch Serverless vector collection.

#### YAML
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_OpenSearch_Serverless_vector_collection.--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template for Knowledge base with Amazon Opensearch Serverless vector database.
Parameters:
  KnowledgeBaseName:
    Type: String
    Description: The name of the knowledge base.
  KnowledgeBaseDescription:
    Type: String
    Description: The description of the knowledge base.
  DataSourceName:
    Type: String
    Description: The name of the data source.
  DataSourceDescription:
    Type: String
    Description: The description of the data source.
Resources:
  KnowledgeBaseWithAoss:
    Type: AWS::Bedrock::KnowledgeBase
    Properties:
      Name: !Ref KnowledgeBaseName
      Description: !Ref KnowledgeBaseDescription
      RoleArn: "arn:aws:iam::123456789012:role/cfn-local-test-role"
      KnowledgeBaseConfiguration:
        Type: "VECTOR"
        VectorKnowledgeBaseConfiguration:
          EmbeddingModelArn: !Sub "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v1"
      StorageConfiguration:
        Type: "OPENSEARCH_SERVERLESS"
        OpensearchServerlessConfiguration:
          CollectionArn: "arn:aws:aoss:us-west-2:123456789012:collection/abcdefghij1234567890"
          VectorIndexName: "cfn-test-index"
          FieldMapping:
            VectorField: "cfn-test-vector-field"
            TextField: "text"
            MetadataField: "metadata"
  SampleDataSource:
    Type: AWS::Bedrock::DataSource
    Properties:
      KnowledgeBaseId: !Ref KnowledgeBaseWithAoss
      Name: !Ref DataSourceName
      Description: !Ref DataSourceDescription
      DataSourceConfiguration:
        Type: "S3"
        S3Configuration:
          BucketArn: "arn:aws:s3:::kb-test-aws"
          InclusionPrefixes: ["aws-overview.pdf"]
```

#### JSON
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_OpenSearch_Serverless_vector_collection.--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "KnowledgeBaseName": {
            "Description": "The name of the knowledge base.",
            "Type": "String"
        },
        "KnowledgeBaseDescription": {
            "Description": "The description of the knowledge base.",
            "Type": "String"
        },
        "DataSourceName": {
            "Description": "The name of the data source.",
            "Type": "String"
        },
        "DataSourceDescription": {
            "Description": "The description of the data source.",
            "Type": "String"
        }
    },
    "Resources": {
        "KnowledgeBaseWithAoss": {
            "Type": "AWS::Bedrock::KnowledgeBase",
            "Properties": {
                "Name": {
                    "Ref": "KnowledgeBaseName"
                },
                "Description": {
                    "Ref": "KnowledgeBaseDescription"
                },
                "RoleArn": "arn:aws:iam::123456789012:role/cfn-local-test-role",
                "KnowledgeBaseConfiguration": {
                    "Type": "VECTOR",
                    "VectorKnowledgeBaseConfiguration": {
                        "EmbeddingModelArn": {
                            "Fn::Sub": "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v1"
                        }
                    }
                },
                "StorageConfiguration": {
                    "Type": "OPENSEARCH_SERVERLESS",
                    "OpensearchServerlessConfiguration": {
                        "CollectionArn": "arn:aws:aoss:us-west-2:123456789012:collection/abcdefghij1234567890",
                        "VectorIndexName": "cfn-test-index",
                        "FieldMapping": {
                            "VectorField": "cfn-test-vector-field",
                            "TextField": "text",
                            "MetadataField": "metadata"
                        }
                    }
                }
            }
        },
        "SampleDataSource": {
            "Type": "AWS::Bedrock::DataSource",
            "Properties": {
                "KnowledgeBaseId": {
                    "Ref": "KnowledgeBaseWithAoss"
                },
                "Name": {
                    "Ref": "DataSourceName"
                },
                "Description": {
                    "Ref": "DataSourceDescription"
                },
                "DataSourceConfiguration": {
                    "Type": "S3",
                    "S3Configuration": {
                        "BucketArn": "arn:aws:s3:::kb-test-aws",
                        "InclusionPrefixes": ["aws-overview.pdf"]
                    }
                }
            }
        }
    }
}
```

### Create a knowledge base in an Amazon Aurora database cluster.
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_Aurora_database_cluster."></a>

The following example creates a knowledge base in a vector index within an Amazon Aurora database cluster.

#### YAML
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_Aurora_database_cluster.--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template for Knowledge base with RDS vector database.
Parameters:
  KnowledgeBaseName:
    Type: String
    Description: The name of the knowledge base.
  KnolwedgeBaseDescription:
    Type: String
    Description: The description of the knowledge base.
  DataSourceName:
    Type: String
    Description: The name of the data source.
  DataSourceDescription:
    Type: String
    Description: The description of the data source.
Resources:
  KnowledgeBaseWithRDS:
    Type: AWS::Bedrock::KnowledgeBase
    Properties:
      Name: !Ref KnowledgeBaseName
      Description: !Ref KnolwedgeBaseDescription
      RoleArn: "arn:aws:iam::123456789012:role/cfn-local-test-role"
      KnowledgeBaseConfiguration:
        Type: "VECTOR"
        VectorKnowledgeBaseConfiguration:
          EmbeddingModelArn: !Sub "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v1"
      StorageConfiguration:
        Type: "RDS"
        RdsConfiguration:
          ResourceArn: !Sub "arn:${AWS::Partition}:rds:${AWS::Region}:${AWS::AccountId}:cluster:ct-kb-cluster"
          CredentialsSecretArn: !Sub "arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:rds!cluster-4f5961a1-ebd5-4887-818f-0f902e945e04-eFxmC6"
          DatabaseName: "postgres"
          TableName: "bedrock_integration.bedrock_kb"
          FieldMapping:
            VectorField: "embedding"
            TextField: "chunks"
            MetadataField: "metadata"
            PrimaryKeyField: "id"
  SampleDataSource:
    Type: AWS::Bedrock::DataSource
    Properties:
      KnowledgeBaseId: !Ref KnowledgeBaseWithRDS
      Name: !Ref DataSourceName
      Description: !Ref DataSourceDescription
      DataSourceConfiguration:
        Type: "S3"
        S3Configuration:
          BucketArn: "arn:aws:s3:::kb-test-aws"
          InclusionPrefixes: ["aws-overview.pdf"]
```

#### JSON
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_an_Amazon_Aurora_database_cluster.--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "KnowledgeBaseName": {
            "Description": "The name of the knowledge base.",
            "Type": "String"
        },
        "KnolwedgeBaseDescription": {
            "Description": "The description of the knowledge base.",
            "Type": "String"
        },
        "DataSourceName": {
            "Description": "The name of the data source.",
            "Type": "String"
        },
        "DataSourceDescription": {
            "Description": "The description of the data source.",
            "Type": "String"
        }
    },
    "Resources": {
        "KnowledgeBaseWithRds": {
            "Type": "AWS::Bedrock::KnowledgeBase",
            "Properties": {
                "Name": {
                    "Ref": "KnowledgeBaseName"
                },
                "Description": {
                    "Ref": "KnolwedgeBaseDescription"
                },
                "RoleArn": "arn:aws:iam::123456789012:role/cfn-local-test-role",
                "KnowledgeBaseConfiguration": {
                    "Type": "VECTOR",
                    "VectorKnowledgeBaseConfiguration": {
                        "EmbeddingModelArn": {
                            "Fn::Sub": "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v1"
                        }
                    }
                },
                "StorageConfiguration": {
                    "Type": "RDS",
                    "RdsConfiguration": {
                        "ResourceArn": {
                            "Fn::Sub": "arn:${AWS::Partition}:rds:${AWS::Region}:${AWS::AccountId}:cluster:knowledgebase-cluster"
                        },
                        "CredentialsSecretArn": {
                            "Fn::Sub": "arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:rds!cluster-4f5961a1-ebd5-4887-818f-0f902e945e04-eFxmC6"
                        },
                        "DatabaseName": "postgres",
                        "TableName": "bedrock_integration.bedrock_kb",
                        "FieldMapping": {
                            "VectorField": "vectorKey",
                            "TextField": "text",
                            "MetadataField": "metadata",
                            "PrimaryKeyField": "id"
                        }
                    }
                }
            }
        },
        "SampleDataSource": {
            "Type": "AWS::Bedrock::DataSource",
            "Properties": {
                "KnowledgeBaseId": {
                    "Ref": "KnowledgeBaseWithRds"
                },
                "Name": {
                    "Ref": "DataSourceName"
                },
                "Description": {
                    "Ref": "DataSourceDescription"
                },
                "DataSourceConfiguration": {
                    "Type": "S3",
                    "S3Configuration": {
                        "BucketArn": "arn:aws:s3:::kb-test-aws",
                        "InclusionPrefixes": ["aws-overview.pdf"]
                    }
                }
            }
        }
    }
}
```

### Create a knowledge base in a Pinecone index.
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_a_Pinecone_index."></a>

The following example creates a knowledge base in a Pinecone index.

#### YAML
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_a_Pinecone_index.--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template for Knowledge base with Pinecone vector database.
Parameters:
  KnowledgeBaseName:
    Type: String
    Description: The name of the knowledge base.
  KnowledgeBaseDescription:
    Type: String
    Description: The description of the knowledge base.
  DataSourceName:
    Type: String
    Description: The name of the data source.
  DataSourceDescription:
    Type: String
    Description: The description of the data source.
Resources:
  KnowledgeBaseWithPinecone:
    Type: AWS::Bedrock::KnowledgeBase
    Properties:
      Name: !Ref KnowledgeBaseName
      Description: !Ref KnowledgeBaseDescription
      RoleArn: "arn:aws:iam::123456789012:role/cfn-local-test-role"
      KnowledgeBaseConfiguration:
        Type: "VECTOR"
        VectorKnowledgeBaseConfiguration:
          EmbeddingModelArn: !Sub "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v1"
      StorageConfiguration:
        Type: "PINECONE"
        PineconeConfiguration:
          ConnectionString: "https://xxxx.pinecone.io>"
          CredentialsSecretArn: "arn:aws:secretsmanager:us-west-2:123456789012:secret:pinecone-secret-abc123"
          Namespace: "kb-namespace"
          FieldMapping:
            TextField: "text"
            MetadataField: "metadata"
  SampleDataSource:
    Type: AWS::Bedrock::DataSource
    Properties:
      KnowledgeBaseId: !Ref KnowledgeBaseWithPinecone
      Name: !Ref DataSourceName
      Description: !Ref DataSourceDescription
      DataSourceConfiguration:
        Type: "S3"
        S3Configuration:
          BucketArn: "arn:aws:s3:::kb-test-aws"
          InclusionPrefixes: ["aws-overview.pdf"]
```

#### JSON
<a name="aws-resource-bedrock-knowledgebase--examples--Create_a_knowledge_base_in_a_Pinecone_index.--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "KnowledgeBaseName": {
            "Description": "The name of the knowledge base.",
            "Type": "String"
        },
        "KnowledgeBaseDescription": {
            "Description": "The description of the knowledge base.",
            "Type": "String"
        },
        "DataSourceName": {
            "Description": "The name of the data source.",
            "Type": "String"
        },
        "DataSourceDescription": {
            "Description": "The description of the data source.",
            "Type": "String"
        }
    },
    "Resources": {
        "KnowledgeBaseWithPinecone": {
            "Type": "AWS::Bedrock::KnowledgeBase",
            "Properties": {
                "Name": {
                    "Ref": "KnowledgeBaseName"
                },
                "Description": {
                    "Ref": "KnowledgeBaseDescription"
                },
                "RoleArn": "arn:aws:iam::123456789012:role/cfn-local-test-role",
                "KnowledgeBaseConfiguration": {
                    "Type": "VECTOR",
                    "VectorKnowledgeBaseConfiguration": {
                        "EmbeddingModelArn": {
                            "Fn::Sub": "arn:${AWS::Partition}:bedrock:${AWS::Region}::foundation-model/amazon.titan-embed-text-v1"
                        }
                    }
                },
                "StorageConfiguration": {
                    "Type": "PINECONE",
                    "PineconeConfiguration": {
                        "ConnectionString": "https://xxxx.pinecone.io",
                        "CredentialsSecretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:pinecone-secret-abc123",
                        "Namespace": "kb-namespace",
                        "FieldMapping": {
                            "TextField": "text",
                            "MetadataField": "metadata"
                        }
                    }
                }
            }
        },
        "SampleDataSource": {
            "Type": "AWS::Bedrock::DataSource",
            "Properties": {
                "KnowledgeBaseId": {
                    "Ref": "KnowledgeBaseWithPinecone"
                },
                "Name": {
                    "Ref": "DataSourceName"
                },
                "Description": {
                    "Ref": "DataSourceDescription"
                },
                "DataSourceConfiguration": {
                    "Type": "S3",
                    "S3Configuration": {
                        "BucketArn": "arn:aws:s3:::kb-test-aws",
                        "InclusionPrefixes": ["aws-overview.pdf"]
                    }
                }
            }
        }
    }
}
```
