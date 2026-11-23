---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint StandardSourceEndpointNetworkingConfiguration

The networking configuration for a standard source endpoint. This is a union type, so exactly one of its members is set: `public` for a publicly accessible endpoint, or `vpc` for an endpoint in a virtual private cloud (VPC).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-syntax.json"></a>

```json
{
  "[Public](#cfn-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-public)" : {{PublicSourceEndpointNetworkingConfiguration}},
  "[Vpc](#cfn-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-vpc)" : {{VpcSourceEndpointNetworkingConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-syntax.yaml"></a>

```yaml
  [Public](#cfn-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-public): {{
    PublicSourceEndpointNetworkingConfiguration}}
  [Vpc](#cfn-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-vpc): {{
    VpcSourceEndpointNetworkingConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-properties"></a>

`Public`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-public"></a>
The configuration for a publicly accessible source endpoint.
*Required*: No
*Type*: [PublicSourceEndpointNetworkingConfiguration](aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vpc`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration-vpc"></a>
The configuration for a source endpoint in a virtual private cloud (VPC).
*Required*: No
*Type*: [VpcSourceEndpointNetworkingConfiguration](aws-properties-mediaconnect-sourceendpoint-vpcsourceendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
