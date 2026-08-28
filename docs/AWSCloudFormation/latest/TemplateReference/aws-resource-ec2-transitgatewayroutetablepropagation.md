---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewayroutetablepropagation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayRouteTablePropagation
<a name="aws-resource-ec2-transitgatewayroutetablepropagation"></a>

Enables the specified attachment to propagate routes to the specified propagation route table.

For more information about enabling transit gateway route propagation, see [EnableTransitGatewayRouteTablePropagation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableTransitGatewayRouteTablePropagation.html) in the *Amazon EC2 API Reference*.

## Syntax
<a name="aws-resource-ec2-transitgatewayroutetablepropagation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewayroutetablepropagation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayRouteTablePropagation",
  "Properties" : {
      "[TransitGatewayAttachmentId](#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayattachmentid)" : {{String}},
      "[TransitGatewayRouteTableId](#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayroutetableid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewayroutetablepropagation-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayRouteTablePropagation
Properties:
  [TransitGatewayAttachmentId](#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayattachmentid): {{String}}
  [TransitGatewayRouteTableId](#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayroutetableid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewayroutetablepropagation-properties"></a>

`TransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewayroutetablepropagation-transitgatewayattachmentid"></a>
The ID of the attachment.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayRouteTableId`  <a name="cfn-ec2-transitgatewayroutetablepropagation-transitgatewayroutetableid"></a>
The ID of the propagation route table.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewayroutetablepropagation-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewayroutetablepropagation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the transit gateway route table that is propagated.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also
<a name="aws-resource-ec2-transitgatewayroutetablepropagation--seealso"></a>
+ [EnableTransitGatewayRouteTablePropagation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableTransitGatewayRouteTablePropagation.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
