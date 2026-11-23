---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint RistStandardDestinationEndpointConfiguration

The configuration settings for a destination endpoint that uses the RIST protocol.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-syntax.json"></a>

```json
{
  "[DestinationAddress](#cfn-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-destinationaddress)" : {{String}},
  "[DestinationIngestPort](#cfn-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-destinationingestport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-syntax.yaml"></a>

```yaml
  [DestinationAddress](#cfn-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-destinationaddress): {{String}}
  [DestinationIngestPort](#cfn-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-destinationingestport): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-properties"></a>

`DestinationAddress`  <a name="cfn-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-destinationaddress"></a>
The IP address on which the destination endpoint receives content.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationIngestPort`  <a name="cfn-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration-destinationingestport"></a>
The port on which the destination endpoint receives content. The valid range is 1024 to 65531.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65531`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
