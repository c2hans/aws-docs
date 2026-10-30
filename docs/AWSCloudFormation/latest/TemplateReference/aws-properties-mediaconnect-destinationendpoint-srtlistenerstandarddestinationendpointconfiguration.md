---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint SrtListenerStandardDestinationEndpointConfiguration
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-description"></a>The `SrtListenerStandardDestinationEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::DestinationEndpoint](aws-resource-mediaconnect-destinationendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-syntax.json"></a>

```
{
  "[DestinationAddress](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationaddress)" : {{String}},
  "[DestinationIngestPort](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationingestport)" : {{Integer}},
  "[EncryptionPassphrase](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-encryptionpassphrase)" : {{EndpointEncryptionSecretConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[StreamId](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-syntax.yaml"></a>

```
  [DestinationAddress](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationaddress): {{String}}
  [DestinationIngestPort](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationingestport): {{Integer}}
  [EncryptionPassphrase](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-encryptionpassphrase): {{
    EndpointEncryptionSecretConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-minimumlatencymilliseconds): {{Integer}}
  [StreamId](#cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-streamid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-properties"></a>

`DestinationAddress`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationaddress"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationIngestPort`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationingestport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65531`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionPassphrase`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-encryptionpassphrase"></a>
Property description not available.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-destinationendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-minimumlatencymilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-streamid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
