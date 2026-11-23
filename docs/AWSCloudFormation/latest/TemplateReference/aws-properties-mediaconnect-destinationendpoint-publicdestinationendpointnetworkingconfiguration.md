---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint PublicDestinationEndpointNetworkingConfiguration

The networking configuration for a publicly accessible destination endpoint, including the CIDR blocks that are allowed to connect.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-syntax.json"></a>

```json
{
  "[DestinationAllowRules](#cfn-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-destinationallowrules)" : {{[ PublicDestinationEndpointNetworkingConfigurationAllowRule, ... ]}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-syntax.yaml"></a>

```yaml
  [DestinationAllowRules](#cfn-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-destinationallowrules): {{
    - PublicDestinationEndpointNetworkingConfigurationAllowRule}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-properties"></a>

`DestinationAllowRules`  <a name="cfn-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration-destinationallowrules"></a>
The rules that specify which CIDR blocks can connect to the destination endpoint. You can specify up to 10 rules.
*Required*: Yes
*Type*: Array of [PublicDestinationEndpointNetworkingConfigurationAllowRule](aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
