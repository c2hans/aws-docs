---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint VpcSourceEndpointNetworkingConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-description"></a>The `VpcSourceEndpointNetworkingConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-securitygroupids"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-subnetid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
