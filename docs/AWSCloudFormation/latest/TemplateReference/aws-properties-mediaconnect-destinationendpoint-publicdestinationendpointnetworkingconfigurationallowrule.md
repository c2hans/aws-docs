---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint PublicDestinationEndpointNetworkingConfigurationAllowRule

A rule that allows a specific CIDR block to connect to the public destination endpoint.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-syntax.json"></a>

```json
{
  "[Cidr](#cfn-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-syntax.yaml"></a>

```yaml
  [Cidr](#cfn-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-cidr): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-properties"></a>

`Cidr`  <a name="cfn-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfigurationallowrule-cidr"></a>
The CIDR block that is allowed to connect to the destination endpoint, in CIDR notation.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/([0-9]|[12][0-9]|3[0-2])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
