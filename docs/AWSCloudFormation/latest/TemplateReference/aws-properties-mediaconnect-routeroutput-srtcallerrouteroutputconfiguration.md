---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput SrtCallerRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration"></a>

The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in caller mode, including the destination address and port, minimum latency, stream ID, and encryption key configuration.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-syntax.json"></a>

```
{
  "[DestinationAddress](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationaddress)" : {{String}},
  "[DestinationPort](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationport)" : {{Integer}},
  "[EncryptionConfiguration](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-encryptionconfiguration)" : {{SrtEncryptionConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[StreamId](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-syntax.yaml"></a>

```
  [DestinationAddress](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationaddress): {{String}}
  [DestinationPort](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationport): {{Integer}}
  [EncryptionConfiguration](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-encryptionconfiguration): {{
    SrtEncryptionConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-minimumlatencymilliseconds): {{Integer}}
  [StreamId](#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-streamid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-properties"></a>

`DestinationAddress`  <a name="cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationaddress"></a>
The destination IP address for the SRT protocol in caller mode.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPort`  <a name="cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationport"></a>
The destination port number for the SRT protocol in caller mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-encryptionconfiguration"></a>
Defines the encryption settings for an SRT caller output, including the encryption key configuration and associated parameters.
*Required*: No
*Type*: [SrtEncryptionConfiguration](aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-minimumlatencymilliseconds"></a>
The minimum latency in milliseconds for the SRT protocol in caller mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-streamid"></a>
The stream ID for the SRT protocol in caller mode.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
