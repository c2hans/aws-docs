---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchserverless-index.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index
<a name="aws-resource-opensearchserverless-index"></a>

An OpenSearch Serverless index resource.

## Syntax
<a name="aws-resource-opensearchserverless-index-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchserverless-index-syntax.json"></a>

```
{
  "Type" : "AWS::OpenSearchServerless::Index",
  "Properties" : {
      "[CollectionEndpoint](#cfn-opensearchserverless-index-collectionendpoint)" : {{String}},
      "[IndexName](#cfn-opensearchserverless-index-indexname)" : {{String}},
      "[Mappings](#cfn-opensearchserverless-index-mappings)" : {{Mappings}},
      "[Settings](#cfn-opensearchserverless-index-settings)" : {{IndexSettings}}
    }
}
```

### YAML
<a name="aws-resource-opensearchserverless-index-syntax.yaml"></a>

```
Type: AWS::OpenSearchServerless::Index
Properties:
  [CollectionEndpoint](#cfn-opensearchserverless-index-collectionendpoint): {{String}}
  [IndexName](#cfn-opensearchserverless-index-indexname): {{String}}
  [Mappings](#cfn-opensearchserverless-index-mappings): {{
    Mappings}}
  [Settings](#cfn-opensearchserverless-index-settings): {{
    IndexSettings}}
```

## Properties
<a name="aws-resource-opensearchserverless-index-properties"></a>

`CollectionEndpoint`  <a name="cfn-opensearchserverless-index-collectionendpoint"></a>
The endpoint for the collection.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IndexName`  <a name="cfn-opensearchserverless-index-indexname"></a>
The name of the OpenSearch Serverless index.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![_-])[a-z][a-z0-9_-]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Mappings`  <a name="cfn-opensearchserverless-index-mappings"></a>
Index mappings for the OpenSearch Serverless index.
*Required*: No
*Type*: [Mappings](aws-properties-opensearchserverless-index-mappings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-opensearchserverless-index-settings"></a>
Index settings for the OpenSearch Serverless index.
*Required*: No
*Type*: [IndexSettings](aws-properties-opensearchserverless-index-indexsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-opensearchserverless-index-return-values"></a>

### Ref
<a name="aws-resource-opensearchserverless-index-return-values-ref"></a>

The index name and the collection endpoint in the following format: index name\|endpoint. Here's an example:

1234TestIndex\|12345678TestEndPoint.us-east-1.aoss.amazonaws.com.

### Fn::GetAtt
<a name="aws-resource-opensearchserverless-index-return-values-fn--getatt"></a>

`GetAtt` returns a value for a specified attribute of this type. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html). The following are the available attributes and sample return values.

####
<a name="aws-resource-opensearchserverless-index-return-values-fn--getatt-fn--getatt"></a>

`Uuid`  <a name="Uuid-fn::getatt"></a>
The unique identifier for the index.

## Examples
<a name="aws-resource-opensearchserverless-index--examples"></a>

### Example - Define index field mappings
<a name="aws-resource-opensearchserverless-index--examples--Example_-_Define_index_field_mappings"></a>

The following example defines an index whose `Mappings` contain a `keyword` field named `status` and a `knn_vector` field named `embedding`. Each field is nested under its own field-name key within `Properties`:

#### YAML
<a name="aws-resource-opensearchserverless-index--examples--Example_-_Define_index_field_mappings--yaml"></a>

```
Resources:
  TestIndex:
    Type: 'AWS::OpenSearchServerless::Index'
    Properties:
      CollectionEndpoint: 'https://my-endpoint.us-east-1.aoss.amazonaws.com'
      IndexName: test-index
      Mappings:
        Properties:
          status:
            Type: keyword
          embedding:
            Type: knn_vector
            Dimension: 1536
```
