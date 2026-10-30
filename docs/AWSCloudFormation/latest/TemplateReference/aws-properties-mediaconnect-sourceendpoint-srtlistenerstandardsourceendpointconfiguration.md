---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint SrtListenerStandardSourceEndpointConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-description"></a>The `SrtListenerStandardSourceEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-syntax.json"></a>

```
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

```
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
Property description not available.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-minimumlatencymilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAddress`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourceaddress"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceListenerPort`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-sourcelistenerport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration-streamid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
