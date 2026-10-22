---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-gateway-gatewayelbnetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Gateway GatewayElbNetworkConfiguration
<a name="aws-properties-ecs-gateway-gatewayelbnetworkconfiguration"></a>

The network configuration for the load balancers that a gateway manages.

## Syntax
<a name="aws-properties-ecs-gateway-gatewayelbnetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-gateway-gatewayelbnetworkconfiguration-syntax.json"></a>

```
{
  "[InboundSecurityGroup](#cfn-ecs-gateway-gatewayelbnetworkconfiguration-inboundsecuritygroup)" : {{String}},
  "[IpAddressType](#cfn-ecs-gateway-gatewayelbnetworkconfiguration-ipaddresstype)" : {{String}},
  "[Subnets](#cfn-ecs-gateway-gatewayelbnetworkconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-gateway-gatewayelbnetworkconfiguration-syntax.yaml"></a>

```
  [InboundSecurityGroup](#cfn-ecs-gateway-gatewayelbnetworkconfiguration-inboundsecuritygroup): {{String}}
  [IpAddressType](#cfn-ecs-gateway-gatewayelbnetworkconfiguration-ipaddresstype): {{String}}
  [Subnets](#cfn-ecs-gateway-gatewayelbnetworkconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-gateway-gatewayelbnetworkconfiguration-properties"></a>

`InboundSecurityGroup`  <a name="cfn-ecs-gateway-gatewayelbnetworkconfiguration-inboundsecuritygroup"></a>
The ID of a security group that you provide to control inbound traffic to the load balancers that the gateway manages. When you specify a security group, the gateway doesn't create inbound rules on the security group it manages.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-ecs-gateway-gatewayelbnetworkconfiguration-ipaddresstype"></a>
The IP address type for the load balancers that the gateway manages. The default is `dualstack`.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack | dualstack-without-public-ipv4`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-ecs-gateway-gatewayelbnetworkconfiguration-subnets"></a>
The subnets for the load balancers that the gateway manages. The default is the subnets in the default VPC.
*Required*: No
*Type*: Array of String
*Minimum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
