---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewayroutetableassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayRouteTableAssociation
<a name="aws-resource-ec2-transitgatewayroutetableassociation"></a>

Associates the specified attachment with the specified transit gateway route table. You can associate one route table with an attachment.

Before you can update the route table associated with an attachment, you must disassociate the transit gateway route table that is currently associated with the attachment. First update the stack to remove the associated transit gateway route table, and then update the stack with the ID of the new transit gateway route table to associate. In addition, the attachment must be in an `available` state; otherwise, the request will return an error.

## Syntax
<a name="aws-resource-ec2-transitgatewayroutetableassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewayroutetableassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayRouteTableAssociation",
  "Properties" : {
      "[TransitGatewayAttachmentId](#cfn-ec2-transitgatewayroutetableassociation-transitgatewayattachmentid)" : {{String}},
      "[TransitGatewayRouteTableId](#cfn-ec2-transitgatewayroutetableassociation-transitgatewayroutetableid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewayroutetableassociation-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayRouteTableAssociation
Properties:
  [TransitGatewayAttachmentId](#cfn-ec2-transitgatewayroutetableassociation-transitgatewayattachmentid): {{String}}
  [TransitGatewayRouteTableId](#cfn-ec2-transitgatewayroutetableassociation-transitgatewayroutetableid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewayroutetableassociation-properties"></a>

`TransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewayroutetableassociation-transitgatewayattachmentid"></a>
The ID of the attachment.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayRouteTableId`  <a name="cfn-ec2-transitgatewayroutetableassociation-transitgatewayroutetableid"></a>
The ID of the route table for the transit gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewayroutetableassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewayroutetableassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the transit gateway route table association.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also
<a name="aws-resource-ec2-transitgatewayroutetableassociation--seealso"></a>
+ [AssociateTransitGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayRouteTable.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
