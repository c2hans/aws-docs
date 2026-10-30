---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint RtpStandardSourceEndpointConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-description"></a>The `RtpStandardSourceEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-syntax.json"></a>

```
{
  "[DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-destinationingestport)" : {{Integer}},
  "[ForwardErrorCorrectionState](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-forwarderrorcorrectionstate)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-syntax.yaml"></a>

```
  [DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-destinationingestport): {{Integer}}
  [ForwardErrorCorrectionState](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-forwarderrorcorrectionstate): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-properties"></a>

`DestinationIngestPort`  <a name="cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-destinationingestport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardErrorCorrectionState`  <a name="cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-forwarderrorcorrectionstate"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
