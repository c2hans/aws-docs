---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint SrtCallerStandardSourceEndpointConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-description"></a>The `SrtCallerStandardSourceEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-syntax.json"></a>

```
{
  "[DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-destinationingestport)" : {{Integer}},
  "[EncryptionPassphrase](#cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-encryptionpassphrase)" : {{EndpointEncryptionSecretConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-minimumlatencymilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-syntax.yaml"></a>

```
  [DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-destinationingestport): {{Integer}}
  [EncryptionPassphrase](#cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-encryptionpassphrase): {{
    EndpointEncryptionSecretConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-minimumlatencymilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-properties"></a>

`DestinationIngestPort`  <a name="cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-destinationingestport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionPassphrase`  <a name="cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-encryptionpassphrase"></a>
Property description not available.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration-minimumlatencymilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
