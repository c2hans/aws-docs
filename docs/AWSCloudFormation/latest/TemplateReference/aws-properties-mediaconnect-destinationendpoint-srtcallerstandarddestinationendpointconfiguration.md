---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint SrtCallerStandardDestinationEndpointConfiguration

The configuration settings for a destination endpoint that uses SRT in caller mode.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-syntax.json"></a>

```json
{
  "[EncryptionPassphrase](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-encryptionpassphrase)" : {{EndpointEncryptionSecretConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[SourceListenerPort](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-sourcelistenerport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-syntax.yaml"></a>

```yaml
  [EncryptionPassphrase](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-encryptionpassphrase): {{
    EndpointEncryptionSecretConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-minimumlatencymilliseconds): {{Integer}}
  [SourceListenerPort](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-sourcelistenerport): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-properties"></a>

`EncryptionPassphrase`  <a name="cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-encryptionpassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-destinationendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-minimumlatencymilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceListenerPort`  <a name="cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-sourcelistenerport"></a>
The port on which the source listens for the connection. The valid range is 3000 to 30000.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
