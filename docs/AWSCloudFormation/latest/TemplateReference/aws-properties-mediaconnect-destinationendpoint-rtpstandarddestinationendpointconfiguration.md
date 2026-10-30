---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint RtpStandardDestinationEndpointConfiguration
<a name="aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-description"></a>The `RtpStandardDestinationEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::DestinationEndpoint](aws-resource-mediaconnect-destinationendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-syntax.json"></a>

```
{
  "[DestinationAddress](#cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-destinationaddress)" : {{String}},
  "[DestinationIngestPort](#cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-destinationingestport)" : {{Integer}},
  "[ForwardErrorCorrectionState](#cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-forwarderrorcorrectionstate)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-syntax.yaml"></a>

```
  [DestinationAddress](#cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-destinationaddress): {{String}}
  [DestinationIngestPort](#cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-destinationingestport): {{Integer}}
  [ForwardErrorCorrectionState](#cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-forwarderrorcorrectionstate): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-properties"></a>

`DestinationAddress`  <a name="cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-destinationaddress"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationIngestPort`  <a name="cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-destinationingestport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65531`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardErrorCorrectionState`  <a name="cfn-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration-forwarderrorcorrectionstate"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
