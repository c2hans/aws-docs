---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput RtmpPushRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration"></a>

<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-description"></a>The `RtmpPushRouterOutputConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterOutput](aws-resource-mediaconnect-routeroutput.md).

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-syntax.json"></a>

```
{
  "[ApplicationName](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-applicationname)" : {{String}},
  "[DestinationAddress](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationaddress)" : {{String}},
  "[DestinationPort](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationport)" : {{Integer}},
  "[StreamName](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-streamname)" : {{String}},
  "[TlsEncryption](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-tlsencryption)" : {{TlsEncryption}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-syntax.yaml"></a>

```
  [ApplicationName](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-applicationname): {{String}}
  [DestinationAddress](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationaddress): {{String}}
  [DestinationPort](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationport): {{Integer}}
  [StreamName](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-streamname): {{String}}
  [TlsEncryption](#cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-tlsencryption): {{
    TlsEncryption}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-properties"></a>

`ApplicationName`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-applicationname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationAddress`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationaddress"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPort`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `443`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamName`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-streamname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsEncryption`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-tlsencryption"></a>
Property description not available.
*Required*: No
*Type*: [TlsEncryption](aws-properties-mediaconnect-routeroutput-tlsencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
