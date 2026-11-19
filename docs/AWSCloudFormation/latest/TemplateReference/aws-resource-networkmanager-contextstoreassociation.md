---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-contextstoreassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ContextStoreAssociation

Describes the association between a context store and a transit gateway.

## Syntax
<a name="aws-resource-networkmanager-contextstoreassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-contextstoreassociation-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkManager::ContextStoreAssociation",
  "Properties" : {
      "[ContextStoreId](#cfn-networkmanager-contextstoreassociation-contextstoreid)" : {{String}},
      "[ResourceArn](#cfn-networkmanager-contextstoreassociation-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-contextstoreassociation-syntax.yaml"></a>

```
Type: AWS::NetworkManager::ContextStoreAssociation
Properties:
  [ContextStoreId](#cfn-networkmanager-contextstoreassociation-contextstoreid): {{String}}
  [ResourceArn](#cfn-networkmanager-contextstoreassociation-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-networkmanager-contextstoreassociation-properties"></a>

`ContextStoreId`  <a name="cfn-networkmanager-contextstoreassociation-contextstoreid"></a>
The ID of the context store.
*Required*: Yes
*Type*: String
*Pattern*: `^context-store-([0-9a-f]{8,17})$`
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArn`  <a name="cfn-networkmanager-contextstoreassociation-resourcearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkmanager-contextstoreassociation-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-contextstoreassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-networkmanager-contextstoreassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-networkmanager-contextstoreassociation-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the association was created.

`State`  <a name="State-fn::getatt"></a>
The state of the association. The possible values are the following:
+ `ASSOCIATING`: The transit gateway is being associated with the context store.
+ `ASSOCIATED`: The transit gateway is associated with the context store.
+ `DISASSOCIATING`: The transit gateway is being disassociated from the context store.
+ `FAILED`: The association failed. To remove it, disassociate the transit gateway.
