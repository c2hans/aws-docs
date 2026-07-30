---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-managedvpcresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway ManagedVpcResource
<a name="aws-properties-bedrockagentcore-gateway-managedvpcresource"></a>

Configuration for a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resource gateway and resource configuration on your behalf using a service-linked role.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-managedvpcresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-managedvpcresource-syntax.json"></a>

```
{
  "[EndpointIpAddressType](#cfn-bedrockagentcore-gateway-managedvpcresource-endpointipaddresstype)" : {{String}},
  "[RoutingDomain](#cfn-bedrockagentcore-gateway-managedvpcresource-routingdomain)" : {{String}},
  "[SecurityGroupIds](#cfn-bedrockagentcore-gateway-managedvpcresource-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-bedrockagentcore-gateway-managedvpcresource-subnetids)" : {{[ String, ... ]}},
  "[VpcIdentifier](#cfn-bedrockagentcore-gateway-managedvpcresource-vpcidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-managedvpcresource-syntax.yaml"></a>

```
  [EndpointIpAddressType](#cfn-bedrockagentcore-gateway-managedvpcresource-endpointipaddresstype): {{String}}
  [RoutingDomain](#cfn-bedrockagentcore-gateway-managedvpcresource-routingdomain): {{String}}
  [SecurityGroupIds](#cfn-bedrockagentcore-gateway-managedvpcresource-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-bedrockagentcore-gateway-managedvpcresource-subnetids): {{
    - String}}
  [VpcIdentifier](#cfn-bedrockagentcore-gateway-managedvpcresource-vpcidentifier): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-managedvpcresource-properties"></a>

`EndpointIpAddressType`  <a name="cfn-bedrockagentcore-gateway-managedvpcresource-endpointipaddresstype"></a>
The IP address type for the resource configuration endpoint.
*Required*: Yes
*Type*: String
*Allowed values*: `IPV4 | IPV6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingDomain`  <a name="cfn-bedrockagentcore-gateway-managedvpcresource-routingdomain"></a>
An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain[Route traffic through an intermediate domain].
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-bedrockagentcore-gateway-managedvpcresource-securitygroupids"></a>
The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-bedrockagentcore-gateway-managedvpcresource-subnetids"></a>
The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcIdentifier`  <a name="cfn-bedrockagentcore-gateway-managedvpcresource-vpcidentifier"></a>
The ID of the VPC that contains your private resource.
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
