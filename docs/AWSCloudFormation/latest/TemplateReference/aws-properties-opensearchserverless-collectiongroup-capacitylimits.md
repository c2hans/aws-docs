---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-collectiongroup-capacitylimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::CollectionGroup CapacityLimits
<a name="aws-properties-opensearchserverless-collectiongroup-capacitylimits"></a>

The maximum capacity limits for all OpenSearch Serverless collections, in OpenSearch Compute Units (OCUs). These limits are used to scale your collections based on the current workload. For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html).

## Syntax
<a name="aws-properties-opensearchserverless-collectiongroup-capacitylimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-collectiongroup-capacitylimits-syntax.json"></a>

```
{
  "[MaxIndexingCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-maxindexingcapacityinocu)" : {{Number}},
  "[MaxSearchCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-maxsearchcapacityinocu)" : {{Number}},
  "[MinIndexingCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-minindexingcapacityinocu)" : {{Number}},
  "[MinSearchCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-minsearchcapacityinocu)" : {{Number}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-collectiongroup-capacitylimits-syntax.yaml"></a>

```
  [MaxIndexingCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-maxindexingcapacityinocu): {{Number}}
  [MaxSearchCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-maxsearchcapacityinocu): {{Number}}
  [MinIndexingCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-minindexingcapacityinocu): {{Number}}
  [MinSearchCapacityInOcu](#cfn-opensearchserverless-collectiongroup-capacitylimits-minsearchcapacityinocu): {{Number}}
```

## Properties
<a name="aws-properties-opensearchserverless-collectiongroup-capacitylimits-properties"></a>

`MaxIndexingCapacityInOcu`  <a name="cfn-opensearchserverless-collectiongroup-capacitylimits-maxindexingcapacityinocu"></a>
The maximum indexing capacity for collections.
*Required*: No
*Type*: Number
*Minimum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxSearchCapacityInOcu`  <a name="cfn-opensearchserverless-collectiongroup-capacitylimits-maxsearchcapacityinocu"></a>
The maximum search capacity for collections.
*Required*: No
*Type*: Number
*Minimum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinIndexingCapacityInOcu`  <a name="cfn-opensearchserverless-collectiongroup-capacitylimits-minindexingcapacityinocu"></a>
The minimum indexing capacity for collections.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinSearchCapacityInOcu`  <a name="cfn-opensearchserverless-collectiongroup-capacitylimits-minsearchcapacityinocu"></a>
The minimum search capacity for collections.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
