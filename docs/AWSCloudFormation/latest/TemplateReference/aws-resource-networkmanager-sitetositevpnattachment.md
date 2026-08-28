---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkmanager-sitetositevpnattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::SiteToSiteVpnAttachment
<a name="aws-resource-networkmanager-sitetositevpnattachment"></a>

Creates an Amazon Web Services site-to-site VPN attachment on an edge location of a core network.

## Syntax
<a name="aws-resource-networkmanager-sitetositevpnattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkmanager-sitetositevpnattachment-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkManager::SiteToSiteVpnAttachment",
  "Properties" : {
      "[CoreNetworkId](#cfn-networkmanager-sitetositevpnattachment-corenetworkid)" : {{String}},
      "[NetworkFunctionGroupName](#cfn-networkmanager-sitetositevpnattachment-networkfunctiongroupname)" : {{String}},
      "[ProposedNetworkFunctionGroupChange](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange)" : {{ProposedNetworkFunctionGroupChange}},
      "[ProposedSegmentChange](#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange)" : {{ProposedSegmentChange}},
      "[RoutingPolicyLabel](#cfn-networkmanager-sitetositevpnattachment-routingpolicylabel)" : {{String}},
      "[Tags](#cfn-networkmanager-sitetositevpnattachment-tags)" : {{[ Tag, ... ]}},
      "[VpnConnectionArn](#cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkmanager-sitetositevpnattachment-syntax.yaml"></a>

```
Type: AWS::NetworkManager::SiteToSiteVpnAttachment
Properties:
  [CoreNetworkId](#cfn-networkmanager-sitetositevpnattachment-corenetworkid): {{String}}
  [NetworkFunctionGroupName](#cfn-networkmanager-sitetositevpnattachment-networkfunctiongroupname): {{String}}
  [ProposedNetworkFunctionGroupChange](#cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange): {{
    ProposedNetworkFunctionGroupChange}}
  [ProposedSegmentChange](#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange): {{
    ProposedSegmentChange}}
  [RoutingPolicyLabel](#cfn-networkmanager-sitetositevpnattachment-routingpolicylabel): {{String}}
  [Tags](#cfn-networkmanager-sitetositevpnattachment-tags): {{
    - Tag}}
  [VpnConnectionArn](#cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn): {{String}}
```

## Properties
<a name="aws-resource-networkmanager-sitetositevpnattachment-properties"></a>

`CoreNetworkId`  <a name="cfn-networkmanager-sitetositevpnattachment-corenetworkid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkFunctionGroupName`  <a name="cfn-networkmanager-sitetositevpnattachment-networkfunctiongroupname"></a>
The name of the network function group.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProposedNetworkFunctionGroupChange`  <a name="cfn-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange"></a>
Describes proposed changes to a network function group.
*Required*: No
*Type*: [ProposedNetworkFunctionGroupChange](aws-properties-networkmanager-sitetositevpnattachment-proposednetworkfunctiongroupchange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProposedSegmentChange`  <a name="cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange"></a>
Describes a proposed segment change. In some cases, the segment change must first be evaluated and accepted.
*Required*: No
*Type*: [ProposedSegmentChange](aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingPolicyLabel`  <a name="cfn-networkmanager-sitetositevpnattachment-routingpolicylabel"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networkmanager-sitetositevpnattachment-tags"></a>
The tags associated with the Site-to-Site VPN attachment.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkmanager-sitetositevpnattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpnConnectionArn`  <a name="cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn"></a>
The ARN of the site-to-site VPN attachment.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:vpn-connection\/vpn-[0-9a-f]{8,17}$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkmanager-sitetositevpnattachment-return-values"></a>

### Ref
<a name="aws-resource-networkmanager-sitetositevpnattachment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AttachmentId`. For example, `{ "Ref: "attachment-05467e74104d33861" }`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networkmanager-sitetositevpnattachment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networkmanager-sitetositevpnattachment-return-values-fn--getatt-fn--getatt"></a>

`AttachmentId`  <a name="AttachmentId-fn::getatt"></a>
The ID of the site-to-site VPN attachment.

`AttachmentPolicyRuleNumber`  <a name="AttachmentPolicyRuleNumber-fn::getatt"></a>
The policy rule number associated with the attachment.

`AttachmentType`  <a name="AttachmentType-fn::getatt"></a>
The type of attachment. This will be `SITE_TO_SITE_VPN`.

`CoreNetworkArn`  <a name="CoreNetworkArn-fn::getatt"></a>
The ARN of the core network.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the site-to-site VPN attachment was created.

`EdgeLocation`  <a name="EdgeLocation-fn::getatt"></a>
The Region where the core network edge is located.

`LastModificationErrors`  <a name="LastModificationErrors-fn::getatt"></a>
Property description not available.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
The ID of the site-to-site VPN attachment owner.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
The resource ARN for the site-to-site VPN attachment.

`SegmentName`  <a name="SegmentName-fn::getatt"></a>
The name of the site-to-site VPN attachment's segment.

`State`  <a name="State-fn::getatt"></a>
The state of the site-to-site VPN attachment. This can be: `REJECTED` \| `PENDING_ATTACHMENT_ACCEPTANCE` \| `CREATING` \| `FAILED` \| `AVAILABLE` \| `UPDATING` \| ` PENDING_NETWORK_UPDATE` \| `PENDING_TAG_ACCEPTANCE` \| `DELETING`.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the site-to-site VPN attachment was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
