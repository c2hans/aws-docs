---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-flowoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput
<a name="aws-resource-mediaconnect-flowoutput"></a>

The `AWS::MediaConnect::FlowOutput` resource defines the destination address, protocol, and port that AWS Elemental MediaConnect sends the ingested video to. Each flow can have up to 50 outputs. An output can have the same protocol or a different protocol from the source. The following protocols are supported: RIST, RTP, RTP-FEC, SRT-listener, SRT-caller, Zixi pull, and Zixi push. CDI and ST 2110 JPEG XS protocols are not currently supported by AWS CloudFormation.

## Syntax
<a name="aws-resource-mediaconnect-flowoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-flowoutput-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::FlowOutput",
  "Properties" : {
      "[CidrAllowList](#cfn-mediaconnect-flowoutput-cidrallowlist)" : {{[ String, ... ]}},
      "[Description](#cfn-mediaconnect-flowoutput-description)" : {{String}},
      "[Destination](#cfn-mediaconnect-flowoutput-destination)" : {{String}},
      "[Encryption](#cfn-mediaconnect-flowoutput-encryption)" : {{Encryption}},
      "[FlowArn](#cfn-mediaconnect-flowoutput-flowarn)" : {{String}},
      "[MaxLatency](#cfn-mediaconnect-flowoutput-maxlatency)" : {{Integer}},
      "[MediaStreamOutputConfigurations](#cfn-mediaconnect-flowoutput-mediastreamoutputconfigurations)" : {{[ MediaStreamOutputConfiguration, ... ]}},
      "[MinLatency](#cfn-mediaconnect-flowoutput-minlatency)" : {{Integer}},
      "[Name](#cfn-mediaconnect-flowoutput-name)" : {{String}},
      "[NdiOutputTimecodeSource](#cfn-mediaconnect-flowoutput-ndioutputtimecodesource)" : {{String}},
      "[NdiProgramName](#cfn-mediaconnect-flowoutput-ndiprogramname)" : {{String}},
      "[NdiSpeedHqQuality](#cfn-mediaconnect-flowoutput-ndispeedhqquality)" : {{Integer}},
      "[OutputStatus](#cfn-mediaconnect-flowoutput-outputstatus)" : {{String}},
      "[Port](#cfn-mediaconnect-flowoutput-port)" : {{Integer}},
      "[Protocol](#cfn-mediaconnect-flowoutput-protocol)" : {{String}},
      "[RemoteId](#cfn-mediaconnect-flowoutput-remoteid)" : {{String}},
      "[RouterIntegrationState](#cfn-mediaconnect-flowoutput-routerintegrationstate)" : {{String}},
      "[RouterIntegrationTransitEncryption](#cfn-mediaconnect-flowoutput-routerintegrationtransitencryption)" : {{FlowTransitEncryption}},
      "[SmoothingLatency](#cfn-mediaconnect-flowoutput-smoothinglatency)" : {{Integer}},
      "[StreamId](#cfn-mediaconnect-flowoutput-streamid)" : {{String}},
      "[Tags](#cfn-mediaconnect-flowoutput-tags)" : {{[ Tag, ... ]}},
      "[VpcInterfaceAttachment](#cfn-mediaconnect-flowoutput-vpcinterfaceattachment)" : {{VpcInterfaceAttachment}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-flowoutput-syntax.yaml"></a>

```
Type: AWS::MediaConnect::FlowOutput
Properties:
  [CidrAllowList](#cfn-mediaconnect-flowoutput-cidrallowlist): {{
    - String}}
  [Description](#cfn-mediaconnect-flowoutput-description): {{String}}
  [Destination](#cfn-mediaconnect-flowoutput-destination): {{String}}
  [Encryption](#cfn-mediaconnect-flowoutput-encryption): {{
    Encryption}}
  [FlowArn](#cfn-mediaconnect-flowoutput-flowarn): {{String}}
  [MaxLatency](#cfn-mediaconnect-flowoutput-maxlatency): {{Integer}}
  [MediaStreamOutputConfigurations](#cfn-mediaconnect-flowoutput-mediastreamoutputconfigurations): {{
    - MediaStreamOutputConfiguration}}
  [MinLatency](#cfn-mediaconnect-flowoutput-minlatency): {{Integer}}
  [Name](#cfn-mediaconnect-flowoutput-name): {{String}}
  [NdiOutputTimecodeSource](#cfn-mediaconnect-flowoutput-ndioutputtimecodesource): {{String}}
  [NdiProgramName](#cfn-mediaconnect-flowoutput-ndiprogramname): {{String}}
  [NdiSpeedHqQuality](#cfn-mediaconnect-flowoutput-ndispeedhqquality): {{Integer}}
  [OutputStatus](#cfn-mediaconnect-flowoutput-outputstatus): {{String}}
  [Port](#cfn-mediaconnect-flowoutput-port): {{Integer}}
  [Protocol](#cfn-mediaconnect-flowoutput-protocol): {{String}}
  [RemoteId](#cfn-mediaconnect-flowoutput-remoteid): {{String}}
  [RouterIntegrationState](#cfn-mediaconnect-flowoutput-routerintegrationstate): {{String}}
  [RouterIntegrationTransitEncryption](#cfn-mediaconnect-flowoutput-routerintegrationtransitencryption): {{
    FlowTransitEncryption}}
  [SmoothingLatency](#cfn-mediaconnect-flowoutput-smoothinglatency): {{Integer}}
  [StreamId](#cfn-mediaconnect-flowoutput-streamid): {{String}}
  [Tags](#cfn-mediaconnect-flowoutput-tags): {{
    - Tag}}
  [VpcInterfaceAttachment](#cfn-mediaconnect-flowoutput-vpcinterfaceattachment): {{
    VpcInterfaceAttachment}}
```

## Properties
<a name="aws-resource-mediaconnect-flowoutput-properties"></a>

`CidrAllowList`  <a name="cfn-mediaconnect-flowoutput-cidrallowlist"></a>
 The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconnect-flowoutput-description"></a>
 A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-mediaconnect-flowoutput-destination"></a>
 The IP address where you want to send the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encryption`  <a name="cfn-mediaconnect-flowoutput-encryption"></a>
 The type of key used for the encryption. If no `keyType` is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.
*Required*: No
*Type*: [Encryption](aws-properties-mediaconnect-flowoutput-encryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowArn`  <a name="cfn-mediaconnect-flowoutput-flowarn"></a>
The Amazon Resource Name (ARN) of the flow this output is attached to.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxLatency`  <a name="cfn-mediaconnect-flowoutput-maxlatency"></a>
The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreamOutputConfigurations`  <a name="cfn-mediaconnect-flowoutput-mediastreamoutputconfigurations"></a>
 The media streams that are associated with the output, and the parameters for those associations.
*Required*: No
*Type*: Array of [MediaStreamOutputConfiguration](aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinLatency`  <a name="cfn-mediaconnect-flowoutput-minlatency"></a>
 The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-flowoutput-name"></a>
 The name of the bridge's output.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NdiOutputTimecodeSource`  <a name="cfn-mediaconnect-flowoutput-ndioutputtimecodesource"></a>
 The settings for the source of the flow.
*Required*: No
*Type*: String
*Allowed values*: `EMBEDDED_TIMECODE | UTC_SYSTEM_TIME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NdiProgramName`  <a name="cfn-mediaconnect-flowoutput-ndiprogramname"></a>
 A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NdiSpeedHqQuality`  <a name="cfn-mediaconnect-flowoutput-ndispeedhqquality"></a>
A quality setting for the NDI Speed HQ encoder.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputStatus`  <a name="cfn-mediaconnect-flowoutput-outputstatus"></a>
 An indication of whether the output should transmit data or not. If you don't specify the `outputStatus` field in your request, MediaConnect leaves the value unchanged.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-flowoutput-port"></a>
 The port to use when content is distributed to this output.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-flowoutput-protocol"></a>
The protocol to use for the output.
AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
*Required*: No
*Type*: String
*Allowed values*: `zixi-push | rtp-fec | rtp | zixi-pull | rist | srt-listener | srt-caller | st2110-jpegxs | cdi | ndi-speed-hq`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemoteId`  <a name="cfn-mediaconnect-flowoutput-remoteid"></a>
 The remote ID for the Zixi-pull stream.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RouterIntegrationState`  <a name="cfn-mediaconnect-flowoutput-routerintegrationstate"></a>
Indicates if router integration is enabled or disabled on the flow output.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RouterIntegrationTransitEncryption`  <a name="cfn-mediaconnect-flowoutput-routerintegrationtransitencryption"></a>
The encryption configuration for the output when router integration is enabled.
*Required*: No
*Type*: [FlowTransitEncryption](aws-properties-mediaconnect-flowoutput-flowtransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmoothingLatency`  <a name="cfn-mediaconnect-flowoutput-smoothinglatency"></a>
 The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-flowoutput-streamid"></a>
 The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flowoutput-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flowoutput-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcInterfaceAttachment`  <a name="cfn-mediaconnect-flowoutput-vpcinterfaceattachment"></a>
 The name of the VPC interface attachment to use for this output.
*Required*: No
*Type*: [VpcInterfaceAttachment](aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-flowoutput-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-flowoutput-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the output ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYCOutput" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-flowoutput-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconnect-flowoutput-return-values-fn--getatt-fn--getatt"></a>

`OutputArn`  <a name="OutputArn-fn::getatt"></a>
The ARN of the output.
