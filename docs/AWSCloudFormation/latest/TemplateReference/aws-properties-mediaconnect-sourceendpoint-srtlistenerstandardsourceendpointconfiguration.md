---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint SrtListenerStandardSourceEndpointConfiguration

The configuration settings for a source endpoint that uses SRT in listener mode.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-syntax.json"></a>

```json
{
  "[EncryptionPassphrase](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-encryptionpassphrase)" : {{EndpointEncryptionSecretConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[SourceAddress](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourceaddress)" : {{String}},
  "[SourceListenerPort](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourcelistenerport)" : {{Integer}},
  "[StreamId](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-syntax.yaml"></a>

```yaml
  [EncryptionPassphrase](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-encryptionpassphrase): {{
    EndpointEncryptionSecretConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-minimumlatencymilliseconds): {{Integer}}
  [SourceAddress](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourceaddress): {{String}}
  [SourceListenerPort](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourcelistenerport): {{Integer}}
  [StreamId](#cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-streamid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-properties"></a>

`EncryptionPassphrase`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-encryptionpassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-minimumlatencymilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAddress`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourceaddress"></a>
The IP address that the source endpoint listens on for incoming connections.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceListenerPort`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourcelistenerport"></a>
The port that the source endpoint listens on for incoming connections. The valid range is 1024 to 65535.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-streamid"></a>
The stream ID that identifies the content for the SRT connection.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
