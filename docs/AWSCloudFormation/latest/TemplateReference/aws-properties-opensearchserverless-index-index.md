---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-index-index.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index Index
<a name="aws-properties-opensearchserverless-index-index"></a>

An OpenSearch Serverless index resource

## Syntax
<a name="aws-properties-opensearchserverless-index-index-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-index-index-syntax.json"></a>

```
{
  "[Knn](#cfn-opensearchserverless-index-index-knn)" : {{Boolean}},
  "[KnnAlgoParamEfSearch](#cfn-opensearchserverless-index-index-knnalgoparamefsearch)" : {{Integer}},
  "[RefreshInterval](#cfn-opensearchserverless-index-index-refreshinterval)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-index-index-syntax.yaml"></a>

```
  [Knn](#cfn-opensearchserverless-index-index-knn): {{Boolean}}
  [KnnAlgoParamEfSearch](#cfn-opensearchserverless-index-index-knnalgoparamefsearch): {{Integer}}
  [RefreshInterval](#cfn-opensearchserverless-index-index-refreshinterval): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-index-index-properties"></a>

`Knn`  <a name="cfn-opensearchserverless-index-index-knn"></a>
Enable or disable k-nearest neighbor search capability.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnnAlgoParamEfSearch`  <a name="cfn-opensearchserverless-index-index-knnalgoparamefsearch"></a>
The size of the dynamic list for the nearest neighbors.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshInterval`  <a name="cfn-opensearchserverless-index-index-refreshinterval"></a>
How often to perform a refresh operation. For example, 1s or 5s.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
