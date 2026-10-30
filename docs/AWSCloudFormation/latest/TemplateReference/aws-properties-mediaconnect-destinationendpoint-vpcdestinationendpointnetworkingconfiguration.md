---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint VpcDestinationEndpointNetworkingConfiguration
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration"></a>

<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-description"></a>The `VpcDestinationEndpointNetworkingConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::DestinationEndpoint](aws-resource-mediaconnect-destinationendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-securitygroupids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration-subnetid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
