---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchserverless-collectiongroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::CollectionGroup
<a name="aws-resource-opensearchserverless-collectiongroup"></a>

Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.

For more information, see [Managing collection groups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html).

## Syntax
<a name="aws-resource-opensearchserverless-collectiongroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchserverless-collectiongroup-syntax.json"></a>

```
{
  "Type" : "AWS::OpenSearchServerless::CollectionGroup",
  "Properties" : {
      "[CapacityLimits](#cfn-opensearchserverless-collectiongroup-capacitylimits)" : {{CapacityLimits}},
      "[Description](#cfn-opensearchserverless-collectiongroup-description)" : {{String}},
      "[Generation](#cfn-opensearchserverless-collectiongroup-generation)" : {{String}},
      "[Name](#cfn-opensearchserverless-collectiongroup-name)" : {{String}},
      "[StandbyReplicas](#cfn-opensearchserverless-collectiongroup-standbyreplicas)" : {{String}},
      "[Tags](#cfn-opensearchserverless-collectiongroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-opensearchserverless-collectiongroup-syntax.yaml"></a>

```
Type: AWS::OpenSearchServerless::CollectionGroup
Properties:
  [CapacityLimits](#cfn-opensearchserverless-collectiongroup-capacitylimits): {{
    CapacityLimits}}
  [Description](#cfn-opensearchserverless-collectiongroup-description): {{String}}
  [Generation](#cfn-opensearchserverless-collectiongroup-generation): {{String}}
  [Name](#cfn-opensearchserverless-collectiongroup-name): {{String}}
  [StandbyReplicas](#cfn-opensearchserverless-collectiongroup-standbyreplicas): {{String}}
  [Tags](#cfn-opensearchserverless-collectiongroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-opensearchserverless-collectiongroup-properties"></a>

`CapacityLimits`  <a name="cfn-opensearchserverless-collectiongroup-capacitylimits"></a>
The maximum capacity limits for all OpenSearch Serverless collections, in OpenSearch Compute Units (OCUs). These limits are used to scale your collections based on the current workload. For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html).
*Required*: No
*Type*: [CapacityLimits](aws-properties-opensearchserverless-collectiongroup-capacitylimits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-opensearchserverless-collectiongroup-description"></a>
The description of the collection group.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Generation`  <a name="cfn-opensearchserverless-collectiongroup-generation"></a>
The generation of Amazon OpenSearch Serverless for the collection group.
*Required*: No
*Type*: String
*Allowed values*: `CLASSIC | NEXTGEN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-opensearchserverless-collectiongroup-name"></a>
The name of the collection group.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9-]{2,31}$`
*Minimum*: `3`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StandbyReplicas`  <a name="cfn-opensearchserverless-collectiongroup-standbyreplicas"></a>
Indicates whether standby replicas are used for the collection group. Can be either `ENABLED` or `DISABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-opensearchserverless-collectiongroup-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-opensearchserverless-collectiongroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-opensearchserverless-collectiongroup-return-values"></a>

### Ref
<a name="aws-resource-opensearchserverless-collectiongroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the collection group ID. For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-opensearchserverless-collectiongroup-return-values-fn--getatt"></a>

Details about a collection group.

####
<a name="aws-resource-opensearchserverless-collectiongroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the collection group.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the collection group.
