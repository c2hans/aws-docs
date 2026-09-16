---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-directconnectgatewayattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::DirectConnectGatewayAttachment
<a name="aws-resource-networkmanager-directconnectgatewayattachment"></a>

Creates an AWS Direct Connect gateway attachment

## Syntax
<a name="aws-resource-networkmanager-directconnectgatewayattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-directconnectgatewayattachment-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkManager::DirectConnectGatewayAttachment",
  "Properties" : {
      "[CoreNetworkId](#cfn-networkmanager-directconnectgatewayattachment-corenetworkid)" : {{String}},
      "[DirectConnectGatewayArn](#cfn-networkmanager-directconnectgatewayattachment-directconnectgatewayarn)" : {{String}},
      "[EdgeLocations](#cfn-networkmanager-directconnectgatewayattachment-edgelocations)" : {{[ String, ... ]}},
      "[RoutingPolicyLabel](#cfn-networkmanager-directconnectgatewayattachment-routingpolicylabel)" : {{String}},
      "[Tags](#cfn-networkmanager-directconnectgatewayattachment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-directconnectgatewayattachment-syntax.yaml"></a>

```
Type: AWS::NetworkManager::DirectConnectGatewayAttachment
Properties:
  [CoreNetworkId](#cfn-networkmanager-directconnectgatewayattachment-corenetworkid): {{String}}
  [DirectConnectGatewayArn](#cfn-networkmanager-directconnectgatewayattachment-directconnectgatewayarn): {{String}}
  [EdgeLocations](#cfn-networkmanager-directconnectgatewayattachment-edgelocations): {{
    - String}}
  [RoutingPolicyLabel](#cfn-networkmanager-directconnectgatewayattachment-routingpolicylabel): {{String}}
  [Tags](#cfn-networkmanager-directconnectgatewayattachment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networkmanager-directconnectgatewayattachment-properties"></a>

`CoreNetworkId`  <a name="cfn-networkmanager-directconnectgatewayattachment-corenetworkid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectConnectGatewayArn`  <a name="cfn-networkmanager-directconnectgatewayattachment-directconnectgatewayarn"></a>
The Direct Connect gateway attachment ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:directconnect::[^:]{0,63}:dx-gateway\/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EdgeLocations`  <a name="cfn-networkmanager-directconnectgatewayattachment-edgelocations"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingPolicyLabel`  <a name="cfn-networkmanager-directconnectgatewayattachment-routingpolicylabel"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkmanager-directconnectgatewayattachment-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-directconnectgatewayattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networkmanager-directconnectgatewayattachment-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-directconnectgatewayattachment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-networkmanager-directconnectgatewayattachment-return-values-fn--getatt"></a>

####
<a name="aws-resource-networkmanager-directconnectgatewayattachment-return-values-fn--getatt-fn--getatt"></a>

`AttachmentId`  <a name="AttachmentId-fn::getatt"></a>
Property description not available.

`AttachmentPolicyRuleNumber`  <a name="AttachmentPolicyRuleNumber-fn::getatt"></a>
Property description not available.

`AttachmentType`  <a name="AttachmentType-fn::getatt"></a>
Property description not available.

`CoreNetworkArn`  <a name="CoreNetworkArn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`LastModificationErrors`  <a name="LastModificationErrors-fn::getatt"></a>
Property description not available.

`NetworkFunctionGroupName`  <a name="NetworkFunctionGroupName-fn::getatt"></a>
The name of the network function group.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
Property description not available.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
Property description not available.

`SegmentName`  <a name="SegmentName-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
