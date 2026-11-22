---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-contextstore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ContextStore

Describes a context store.

## Syntax
<a name="aws-resource-networkmanager-contextstore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-contextstore-syntax.json"></a>

```json
{
  "Type" : "AWS::NetworkManager::ContextStore",
  "Properties" : {
      "[Description](#cfn-networkmanager-contextstore-description)" : {{String}},
      "[GlobalNetworkId](#cfn-networkmanager-contextstore-globalnetworkid)" : {{String}},
      "[Tags](#cfn-networkmanager-contextstore-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-contextstore-syntax.yaml"></a>

```yaml
Type: AWS::NetworkManager::ContextStore
Properties:
  [Description](#cfn-networkmanager-contextstore-description): {{String}}
  [GlobalNetworkId](#cfn-networkmanager-contextstore-globalnetworkid): {{String}}
  [Tags](#cfn-networkmanager-contextstore-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networkmanager-contextstore-properties"></a>

`Description`  <a name="cfn-networkmanager-contextstore-description"></a>
The description of the context store.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalNetworkId`  <a name="cfn-networkmanager-contextstore-globalnetworkid"></a>
The ID of the global network that the context store belongs to.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networkmanager-contextstore-tags"></a>
The tags associated with the context store.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-contextstore-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networkmanager-contextstore-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-contextstore-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-networkmanager-contextstore-return-values-fn--getatt"></a>

####
<a name="aws-resource-networkmanager-contextstore-return-values-fn--getatt-fn--getatt"></a>

`ContextStoreArn`  <a name="ContextStoreArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the context store.

`ContextStoreId`  <a name="ContextStoreId-fn::getatt"></a>
The ID of the context store.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the context store was created.

`State`  <a name="State-fn::getatt"></a>
The state of the context store. The possible values are the following:
+ `PENDING`: The context store is being created.
+ `AVAILABLE`: The context store is ready to use.
+ `UPDATING`: The context store is being updated.
+ `DELETING`: The context store is being deleted.
+ `DELETED`: The context store is deleted.
