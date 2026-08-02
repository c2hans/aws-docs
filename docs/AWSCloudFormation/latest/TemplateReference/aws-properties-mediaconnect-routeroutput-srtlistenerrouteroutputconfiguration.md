---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput SrtListenerRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration"></a>

The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and encryption key configuration.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-syntax.json"></a>

```
{
  "[EncryptionConfiguration](#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-encryptionconfiguration)" : {{SrtEncryptionConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[Port](#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-syntax.yaml"></a>

```
  [EncryptionConfiguration](#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-encryptionconfiguration): {{
    SrtEncryptionConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-minimumlatencymilliseconds): {{Integer}}
  [Port](#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-port): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-properties"></a>

`EncryptionConfiguration`  <a name="cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-encryptionconfiguration"></a>
Defines the encryption settings for an SRT listener output, including the encryption key configuration and associated parameters.
*Required*: No
*Type*: [SrtEncryptionConfiguration](aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-minimumlatencymilliseconds"></a>
The minimum latency in milliseconds for the SRT protocol in listener mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-port"></a>
The port number for the SRT protocol in listener mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
