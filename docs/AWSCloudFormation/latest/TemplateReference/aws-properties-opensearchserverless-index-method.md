---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-index-method.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index Method
<a name="aws-properties-opensearchserverless-index-method"></a>

Configuration for k-NN search method.

## Syntax
<a name="aws-properties-opensearchserverless-index-method-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-index-method-syntax.json"></a>

```
{
  "[Engine](#cfn-opensearchserverless-index-method-engine)" : {{String}},
  "[Name](#cfn-opensearchserverless-index-method-name)" : {{String}},
  "[Parameters](#cfn-opensearchserverless-index-method-parameters)" : {{Parameters}},
  "[SpaceType](#cfn-opensearchserverless-index-method-spacetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-index-method-syntax.yaml"></a>

```
  [Engine](#cfn-opensearchserverless-index-method-engine): {{String}}
  [Name](#cfn-opensearchserverless-index-method-name): {{String}}
  [Parameters](#cfn-opensearchserverless-index-method-parameters): {{
    Parameters}}
  [SpaceType](#cfn-opensearchserverless-index-method-spacetype): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-index-method-properties"></a>

`Engine`  <a name="cfn-opensearchserverless-index-method-engine"></a>
The k-NN search engine to use
*Required*: No
*Type*: String
*Allowed values*: `nmslib | faiss | lucene`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-opensearchserverless-index-method-name"></a>
The algorithm name for k-NN search.
*Required*: Yes
*Type*: String
*Allowed values*: `hnsw | ivf`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-opensearchserverless-index-method-parameters"></a>
Additional parameters for the k-NN algorithm.
*Required*: No
*Type*: [Parameters](aws-properties-opensearchserverless-index-parameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceType`  <a name="cfn-opensearchserverless-index-method-spacetype"></a>
The distance function used for k-NN search.
*Required*: No
*Type*: String
*Allowed values*: `l2 | l1 | linf | cosinesimil | innerproduct | hamming`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
