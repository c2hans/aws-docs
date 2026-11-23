---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint PublicSourceEndpointNetworkingConfiguration

The networking configuration for a publicly accessible source endpoint, including the CIDR blocks that are allowed to connect.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-syntax.json"></a>

```json
{
  "[SourceAllowRules](#cfn-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-sourceallowrules)" : {{[ PublicSourceEndpointNetworkingConfigurationAllowRule, ... ]}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-syntax.yaml"></a>

```yaml
  [SourceAllowRules](#cfn-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-sourceallowrules): {{
    - PublicSourceEndpointNetworkingConfigurationAllowRule}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-properties"></a>

`SourceAllowRules`  <a name="cfn-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfiguration-sourceallowrules"></a>
The rules that specify which CIDR blocks can connect to the source endpoint. You can specify up to 10 rules.
*Required*: Yes
*Type*: Array of [PublicSourceEndpointNetworkingConfigurationAllowRule](aws-properties-mediaconnect-sourceendpoint-publicsourceendpointnetworkingconfigurationallowrule.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
