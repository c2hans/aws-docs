---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase OpenSearchManagedClusterConfiguration
<a name="aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration"></a>

Contains details about the Managed Cluster configuration of the knowledge base in Amazon OpenSearch Service. For more information, see [Create a vector index in OpenSearch Managed Cluster](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-syntax.json"></a>

```
{
  "[DomainArn](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-domainarn)" : {{String}},
  "[DomainEndpoint](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-domainendpoint)" : {{String}},
  "[FieldMapping](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-fieldmapping)" : {{OpenSearchManagedClusterFieldMapping}},
  "[VectorIndexName](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-vectorindexname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-syntax.yaml"></a>

```
  [DomainArn](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-domainarn): {{String}}
  [DomainEndpoint](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-domainendpoint): {{String}}
  [FieldMapping](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-fieldmapping): {{
    OpenSearchManagedClusterFieldMapping}}
  [VectorIndexName](#cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-vectorindexname): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-properties"></a>

`DomainArn`  <a name="cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-domainarn"></a>
The Amazon Resource Name (ARN) of the OpenSearch domain.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:es:([a-z]{2,}-){2,}\d:\d{12}:domain/[a-z][a-z0-9-]{3,28}$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainEndpoint`  <a name="cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-domainendpoint"></a>
The endpoint URL the OpenSearch domain.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldMapping`  <a name="cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-fieldmapping"></a>
Contains the names of the fields to which to map information about the vector store.
*Required*: Yes
*Type*: [OpenSearchManagedClusterFieldMapping](aws-properties-bedrock-knowledgebase-opensearchmanagedclusterfieldmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorIndexName`  <a name="cfn-bedrock-knowledgebase-opensearchmanagedclusterconfiguration-vectorindexname"></a>
The name of the vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![\-_+.])[a-z0-9][a-z0-9\-_\.]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
