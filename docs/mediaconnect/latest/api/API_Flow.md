---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Flow.html
---

# Flow
<a name="API_Flow"></a>

 The settings for a flow, including its source, outputs, and entitlements.

## Contents
<a name="API_Flow_Contents"></a>

 ** availabilityZone **   <a name="mediaconnect-Type-Flow-availabilityZone"></a>
 The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
Type: String
Required: Yes

 ** entitlements **   <a name="mediaconnect-Type-Flow-entitlements"></a>
 The entitlements in this flow.
Type: Array of [Entitlement](API_Entitlement.md) objects
Required: Yes

 ** flowArn **   <a name="mediaconnect-Type-Flow-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-Flow-name"></a>
 The name of the flow.
Type: String
Required: Yes

 ** outputs **   <a name="mediaconnect-Type-Flow-outputs"></a>
 The outputs in this flow.
Type: Array of [Output](API_Output.md) objects
Required: Yes

 ** source **   <a name="mediaconnect-Type-Flow-source"></a>
 The source for the flow.
Type: [Source](API_Source.md) object
Required: Yes

 ** status **   <a name="mediaconnect-Type-Flow-status"></a>
 The current status of the flow.
Type: String
Valid Values: `STANDBY | ACTIVE | UPDATING | DELETING | STARTING | STOPPING | ERROR`
Required: Yes

 ** description **   <a name="mediaconnect-Type-Flow-description"></a>
 A description of the flow. This value is not used or seen outside of the current MediaConnect account.
Type: String
Required: No

 ** egressIp **   <a name="mediaconnect-Type-Flow-egressIp"></a>
 The IP address from which video will be sent to output destinations.
Type: String
Required: No

 ** encodingConfig **   <a name="mediaconnect-Type-Flow-encodingConfig"></a>
 The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution.
Type: [EncodingConfig](API_EncodingConfig.md) object
Required: No

 ** flowSize **   <a name="mediaconnect-Type-Flow-flowSize"></a>
 Determines the processing capacity and feature set of the flow.
Type: String
Valid Values: `MEDIUM | LARGE | LARGE_4X`
Required: No

 ** maintenance **   <a name="mediaconnect-Type-Flow-maintenance"></a>
 The maintenance settings for the flow.
Type: [Maintenance](API_Maintenance.md) object
Required: No

 ** mediaStreams **   <a name="mediaconnect-Type-Flow-mediaStreams"></a>
 The media streams that are associated with the flow. After you associate a media stream with a source, you can also associate it with outputs on the flow.
Type: Array of [MediaStream](API_MediaStream.md) objects
Required: No

 ** ndiConfig **   <a name="mediaconnect-Type-Flow-ndiConfig"></a>
Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output.
Type: [NdiConfig](API_NdiConfig.md) object
Required: No

 ** sourceFailoverConfig **   <a name="mediaconnect-Type-Flow-sourceFailoverConfig"></a>
 The settings for the source failover.
Type: [FailoverConfig](API_FailoverConfig.md) object
Required: No

 ** sourceMonitoringConfig **   <a name="mediaconnect-Type-Flow-sourceMonitoringConfig"></a>
 The settings for source monitoring.
Type: [MonitoringConfig](API_MonitoringConfig.md) object
Required: No

 ** sources **   <a name="mediaconnect-Type-Flow-sources"></a>
The settings for the sources that are assigned to the flow.
Type: Array of [Source](API_Source.md) objects
Required: No

 ** vpcInterfaces **   <a name="mediaconnect-Type-Flow-vpcInterfaces"></a>
 The VPC Interfaces for this flow.
Type: Array of [VpcInterface](API_VpcInterface.md) objects
Required: No

## See Also
<a name="API_Flow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Flow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Flow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Flow)
