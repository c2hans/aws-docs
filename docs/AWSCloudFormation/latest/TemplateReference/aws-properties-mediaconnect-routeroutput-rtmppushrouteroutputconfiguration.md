---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput RtmpPushRouterOutputConfiguration

The configuration settings for a router output that pushes a stream to a destination using the RTMP (Real-Time Messaging Protocol) protocol, or RTMPS (RTMP over TLS) when TLS encryption is specified. These settings include the destination address and port, the application and stream names, and optional TLS encryption configuration.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-syntax.json"></a>

```json
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

```yaml
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
The name of the RTMP application on the destination server. Together with the stream name, the application name forms the RTMP URL path, in the pattern `rtmp://destinationAddress/applicationName/streamName`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationAddress`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationaddress"></a>
The IP address or hostname of the destination RTMP server that the router output pushes the stream to. Provide only the server address; specify the application and stream names separately.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPort`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-destinationport"></a>
The TCP port on the destination RTMP server. For RTMP, valid values range from `1024` to `65535`. For RTMPS (RTMP over TLS), valid values are `443` or `1024` to `65535`. RTMP typically uses port `1935`, and RTMPS typically uses port `443`.
*Required*: Yes
*Type*: Integer
*Minimum*: `443`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamName`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-streamname"></a>
The name of the RTMP stream that the output publishes to the destination application. The stream name forms the final segment of the RTMP URL path.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsEncryption`  <a name="cfn-mediaconnect-routeroutput-rtmppushrouteroutputconfiguration-tlsencryption"></a>
The TLS encryption settings for the output. When you specify these settings, the output uses RTMPS (RTMP over TLS) to establish a secure, encrypted connection to the destination server.
*Required*: No
*Type*: [TlsEncryption](aws-properties-mediaconnect-routeroutput-tlsencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
