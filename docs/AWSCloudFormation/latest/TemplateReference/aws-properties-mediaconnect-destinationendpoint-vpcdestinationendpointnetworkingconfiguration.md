---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint VpcDestinationEndpointNetworkingConfiguration

The networking configuration for a destination endpoint in a virtual private cloud (VPC).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-syntax.json"></a>

```json
{
  "[SecurityGroupIds](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-syntax.yaml"></a>

```yaml
  [SecurityGroupIds](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-securitygroupids"></a>
The IDs of the security groups to associate with the destination endpoint. You can specify from 1 to 5 security groups.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-subnetid"></a>
The ID of the subnet to use for the destination endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
