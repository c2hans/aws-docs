---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewayroutetable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayRouteTable
<a name="aws-resource-ec2-transitgatewayroutetable"></a>

Specifies a route table for a transit gateway.

## Syntax
<a name="aws-resource-ec2-transitgatewayroutetable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewayroutetable-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayRouteTable",
  "Properties" : {
      "[Tags](#cfn-ec2-transitgatewayroutetable-tags)" : {{[ Tag, ... ]}},
      "[TransitGatewayId](#cfn-ec2-transitgatewayroutetable-transitgatewayid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewayroutetable-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayRouteTable
Properties:
  [Tags](#cfn-ec2-transitgatewayroutetable-tags): {{
    - Tag}}
  [TransitGatewayId](#cfn-ec2-transitgatewayroutetable-transitgatewayid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewayroutetable-properties"></a>

`Tags`  <a name="cfn-ec2-transitgatewayroutetable-tags"></a>
Any tags assigned to the route table.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-transitgatewayroutetable-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayId`  <a name="cfn-ec2-transitgatewayroutetable-transitgatewayid"></a>
The ID of the transit gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewayroutetable-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewayroutetable-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the transit gateway route table.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewayroutetable-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-transitgatewayroutetable-return-values-fn--getatt-fn--getatt"></a>

`TransitGatewayRouteTableId`  <a name="TransitGatewayRouteTableId-fn::getatt"></a>
The ID of the transit gateway route table.

## See also
<a name="aws-resource-ec2-transitgatewayroutetable--seealso"></a>
+ [CreateTransitGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRouteTable.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
