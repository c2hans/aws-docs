---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rtbfabric-requestergateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::RequesterGateway
<a name="aws-resource-rtbfabric-requestergateway"></a>

Creates a requester gateway.

## Syntax
<a name="aws-resource-rtbfabric-requestergateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rtbfabric-requestergateway-syntax.json"></a>

```
{
  "Type" : "AWS::RTBFabric::RequesterGateway",
  "Properties" : {
      "[Description](#cfn-rtbfabric-requestergateway-description)" : {{String}},
      "[SecurityGroupIds](#cfn-rtbfabric-requestergateway-securitygroupids)" : {{[ String, ... ]}},
      "[SubnetIds](#cfn-rtbfabric-requestergateway-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-rtbfabric-requestergateway-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-rtbfabric-requestergateway-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-rtbfabric-requestergateway-syntax.yaml"></a>

```
Type: AWS::RTBFabric::RequesterGateway
Properties:
  [Description](#cfn-rtbfabric-requestergateway-description): {{String}}
  [SecurityGroupIds](#cfn-rtbfabric-requestergateway-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-rtbfabric-requestergateway-subnetids): {{
    - String}}
  [Tags](#cfn-rtbfabric-requestergateway-tags): {{
    - Tag}}
  [VpcId](#cfn-rtbfabric-requestergateway-vpcid): {{String}}
```

## Properties
<a name="aws-resource-rtbfabric-requestergateway-properties"></a>

`Description`  <a name="cfn-rtbfabric-requestergateway-description"></a>
An optional description for the requester gateway.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9 ]+$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SecurityGroupIds`  <a name="cfn-rtbfabric-requestergateway-securitygroupids"></a>
The unique identifiers of the security groups.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SubnetIds`  <a name="cfn-rtbfabric-requestergateway-subnetids"></a>
The unique identifiers of the subnets.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-rtbfabric-requestergateway-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-rtbfabric-requestergateway-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-rtbfabric-requestergateway-vpcid"></a>
The unique identifier of the Virtual Private Cloud (VPC).
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `50`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-rtbfabric-requestergateway-return-values"></a>

### Ref
<a name="aws-resource-rtbfabric-requestergateway-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rtbfabric-requestergateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rtbfabric-requestergateway-return-values-fn--getatt-fn--getatt"></a>

`ActiveLinksCount`  <a name="ActiveLinksCount-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
Property description not available.

`DomainName`  <a name="DomainName-fn::getatt"></a>
Property description not available.

`GatewayId`  <a name="GatewayId-fn::getatt"></a>
Property description not available.

`RequesterGatewayStatus`  <a name="RequesterGatewayStatus-fn::getatt"></a>
Property description not available.

`TotalLinksCount`  <a name="TotalLinksCount-fn::getatt"></a>
Property description not available.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
