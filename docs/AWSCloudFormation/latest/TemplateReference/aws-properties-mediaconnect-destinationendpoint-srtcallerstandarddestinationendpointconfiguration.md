---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint SrtCallerStandardDestinationEndpointConfiguration
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-description"></a>The `SrtCallerStandardDestinationEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::DestinationEndpoint](aws-resource-mediaconnect-destinationendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-syntax.json"></a>

```
{
  "[EncryptionPassphrase](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-encryptionpassphrase)" : {{EndpointEncryptionSecretConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[SourceListenerPort](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-sourcelistenerport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-syntax.yaml"></a>

```
  [EncryptionPassphrase](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-encryptionpassphrase): {{
    EndpointEncryptionSecretConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-minimumlatencymilliseconds): {{Integer}}
  [SourceListenerPort](#cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-sourcelistenerport): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-properties"></a>

`EncryptionPassphrase`  <a name="cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-encryptionpassphrase"></a>
Property description not available.
*Required*: No
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-destinationendpoint-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-minimumlatencymilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceListenerPort`  <a name="cfn-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration-sourcelistenerport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
