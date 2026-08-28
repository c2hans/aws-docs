---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaypeeringattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPeeringAttachment
<a name="aws-resource-ec2-transitgatewaypeeringattachment"></a>

Requests a transit gateway peering attachment between the specified transit gateway (requester) and a peer transit gateway (accepter). The peer transit gateway can be in your account or a different AWS account.

After you create the peering attachment, the owner of the accepter transit gateway must accept the attachment request.

## Syntax
<a name="aws-resource-ec2-transitgatewaypeeringattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaypeeringattachment-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayPeeringAttachment",
  "Properties" : {
      "[PeerAccountId](#cfn-ec2-transitgatewaypeeringattachment-peeraccountid)" : {{String}},
      "[PeerRegion](#cfn-ec2-transitgatewaypeeringattachment-peerregion)" : {{String}},
      "[PeerTransitGatewayId](#cfn-ec2-transitgatewaypeeringattachment-peertransitgatewayid)" : {{String}},
      "[Tags](#cfn-ec2-transitgatewaypeeringattachment-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-transitgatewaypeeringattachment-transitgatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaypeeringattachment-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayPeeringAttachment
Properties:
  [PeerAccountId](#cfn-ec2-transitgatewaypeeringattachment-peeraccountid): {{String}}
  [PeerRegion](#cfn-ec2-transitgatewaypeeringattachment-peerregion): {{String}}
  [PeerTransitGatewayId](#cfn-ec2-transitgatewaypeeringattachment-peertransitgatewayid): {{String}}
  [Tags](#cfn-ec2-transitgatewaypeeringattachment-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-transitgatewaypeeringattachment-transitgatewayid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaypeeringattachment-properties"></a>

`PeerAccountId`  <a name="cfn-ec2-transitgatewaypeeringattachment-peeraccountid"></a>
The ID of the AWS account that owns the transit gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerRegion`  <a name="cfn-ec2-transitgatewaypeeringattachment-peerregion"></a>
The Region where the transit gateway that you want to create the peer for is located.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerTransitGatewayId`  <a name="cfn-ec2-transitgatewaypeeringattachment-peertransitgatewayid"></a>
The ID of the transit gateway in the PeerRegion.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-transitgatewaypeeringattachment-tags"></a>
The tags for the transit gateway peering attachment.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-transitgatewaypeeringattachment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-transitgatewaypeeringattachment-transitgatewayid"></a>
The ID of the transit gateway peering attachment.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaypeeringattachment-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaypeeringattachment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the transit gateway peering attachment.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaypeeringattachment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-transitgatewaypeeringattachment-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time the transit gateway peering attachment was created.

`State`  <a name="State-fn::getatt"></a>
The state of the transit gateway peering attachment. Note that the `initiating` state has been deprecated.

`TransitGatewayAttachmentId`  <a name="TransitGatewayAttachmentId-fn::getatt"></a>
The ID of the transit gateway peering attachment.

## See also
<a name="aws-resource-ec2-transitgatewaypeeringattachment--seealso"></a>
+ [CreateTransitGatewayPeeringAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPeeringAttachment.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
