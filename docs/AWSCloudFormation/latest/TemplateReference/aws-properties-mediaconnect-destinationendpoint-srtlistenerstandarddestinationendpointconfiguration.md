---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint SrtListenerStandardDestinationEndpointConfiguration

The configuration settings for a destination endpoint that uses SRT in listener mode.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-syntax.json"></a>

```json
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

```yaml
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
The IP address on which the destination endpoint listens for incoming connections.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationIngestPort`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-destinationingestport"></a>
The port on which the destination endpoint listens for incoming connections. The valid range is 0 to 65531.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65531`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionPassphrase`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-encryptionpassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-destinationendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-minimumlatencymilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration-streamid"></a>
The stream ID that identifies the content for the SRT connection.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
