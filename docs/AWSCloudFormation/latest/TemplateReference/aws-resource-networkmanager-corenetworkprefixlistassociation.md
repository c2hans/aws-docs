---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-corenetworkprefixlistassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::CoreNetworkPrefixListAssociation
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation"></a>

Creates an association between a core network and a prefix list for routing control.

## Syntax
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkManager::CoreNetworkPrefixListAssociation",
  "Properties" : {
      "[CoreNetworkId](#cfn-networkmanager-corenetworkprefixlistassociation-corenetworkid)" : {{String}},
      "[PrefixListAlias](#cfn-networkmanager-corenetworkprefixlistassociation-prefixlistalias)" : {{String}},
      "[PrefixListArn](#cfn-networkmanager-corenetworkprefixlistassociation-prefixlistarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation-syntax.yaml"></a>

```
Type: AWS::NetworkManager::CoreNetworkPrefixListAssociation
Properties:
  [CoreNetworkId](#cfn-networkmanager-corenetworkprefixlistassociation-corenetworkid): {{String}}
  [PrefixListAlias](#cfn-networkmanager-corenetworkprefixlistassociation-prefixlistalias): {{String}}
  [PrefixListArn](#cfn-networkmanager-corenetworkprefixlistassociation-prefixlistarn): {{String}}
```

## Properties
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation-properties"></a>

`CoreNetworkId`  <a name="cfn-networkmanager-corenetworkprefixlistassociation-corenetworkid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrefixListAlias`  <a name="cfn-networkmanager-corenetworkprefixlistassociation-prefixlistalias"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrefixListArn`  <a name="cfn-networkmanager-corenetworkprefixlistassociation-prefixlistarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-corenetworkprefixlistassociation-return-values-ref"></a>
