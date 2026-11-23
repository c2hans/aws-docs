---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint VpcSourceEndpointNetworkingConfiguration

The networking configuration for a source endpoint in a virtual private cloud (VPC).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-syntax.json"></a>

```json
{
  "[SecurityGroupIds](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-syntax.yaml"></a>

```yaml
  [SecurityGroupIds](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-properties"></a>

`SecurityGroupIds`  <a name="cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-securitygroupids"></a>
The IDs of the security groups to associate with the source endpoint. You can specify from 1 to 5 security groups.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration-subnetid"></a>
The ID of the subnet to use for the source endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
