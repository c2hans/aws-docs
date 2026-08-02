---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-collection-vectoroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Collection VectorOptions
<a name="aws-properties-opensearchserverless-collection-vectoroptions"></a>

Configuration options for vector search capabilities in an OpenSearch Serverless collection.

## Syntax
<a name="aws-properties-opensearchserverless-collection-vectoroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-collection-vectoroptions-syntax.json"></a>

```
{
  "[ServerlessVectorAcceleration](#cfn-opensearchserverless-collection-vectoroptions-serverlessvectoracceleration)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-collection-vectoroptions-syntax.yaml"></a>

```
  [ServerlessVectorAcceleration](#cfn-opensearchserverless-collection-vectoroptions-serverlessvectoracceleration): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-collection-vectoroptions-properties"></a>

`ServerlessVectorAcceleration`  <a name="cfn-opensearchserverless-collection-vectoroptions-serverlessvectoracceleration"></a>
Specifies whether serverless vector acceleration is enabled for the collection.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED | ALLOWED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
