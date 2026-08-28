---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-managedvpcresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime ManagedVpcResource
<a name="aws-properties-bedrockagentcore-runtime-managedvpcresource"></a>

Configuration for a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resource gateway and resource configuration on your behalf using a service-linked role.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-managedvpcresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-managedvpcresource-syntax.json"></a>

```
{
  "[EndpointIpAddressType](#cfn-bedrockagentcore-runtime-managedvpcresource-endpointipaddresstype)" : {{String}},
  "[RoutingDomain](#cfn-bedrockagentcore-runtime-managedvpcresource-routingdomain)" : {{String}},
  "[SecurityGroupIds](#cfn-bedrockagentcore-runtime-managedvpcresource-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-bedrockagentcore-runtime-managedvpcresource-subnetids)" : {{[ String, ... ]}},
  "[Tags](#cfn-bedrockagentcore-runtime-managedvpcresource-tags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[VpcIdentifier](#cfn-bedrockagentcore-runtime-managedvpcresource-vpcidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-managedvpcresource-syntax.yaml"></a>

```
  [EndpointIpAddressType](#cfn-bedrockagentcore-runtime-managedvpcresource-endpointipaddresstype): {{String}}
  [RoutingDomain](#cfn-bedrockagentcore-runtime-managedvpcresource-routingdomain): {{String}}
  [SecurityGroupIds](#cfn-bedrockagentcore-runtime-managedvpcresource-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-bedrockagentcore-runtime-managedvpcresource-subnetids): {{
    - String}}
  [Tags](#cfn-bedrockagentcore-runtime-managedvpcresource-tags): {{
    {{Key}}: {{Value}}}}
  [VpcIdentifier](#cfn-bedrockagentcore-runtime-managedvpcresource-vpcidentifier): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-managedvpcresource-properties"></a>

`EndpointIpAddressType`  <a name="cfn-bedrockagentcore-runtime-managedvpcresource-endpointipaddresstype"></a>
The IP address type for the resource configuration endpoint.
*Required*: Yes
*Type*: String
*Allowed values*: `IPV4 | IPV6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingDomain`  <a name="cfn-bedrockagentcore-runtime-managedvpcresource-routingdomain"></a>
An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain[Route traffic through an intermediate domain].
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-bedrockagentcore-runtime-managedvpcresource-securitygroupids"></a>
The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-bedrockagentcore-runtime-managedvpcresource-subnetids"></a>
The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-runtime-managedvpcresource-tags"></a>
Tags to apply to the managed VPC Lattice resource gateway.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcIdentifier`  <a name="cfn-bedrockagentcore-runtime-managedvpcresource-vpcidentifier"></a>
The ID of the VPC that contains your private resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
