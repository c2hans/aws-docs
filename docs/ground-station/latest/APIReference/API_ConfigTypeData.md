---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigTypeData.html
---

# ConfigTypeData
<a name="API_ConfigTypeData"></a>

Object containing the parameters of a `Config`.

See the subtype definitions for what each type of `Config` contains.

## Contents
<a name="API_ConfigTypeData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** antennaDownlinkConfig **   <a name="groundstation-Type-ConfigTypeData-antennaDownlinkConfig"></a>
Information about how AWS Ground Station should configure an antenna for downlink during a contact.
Type: [AntennaDownlinkConfig](API_AntennaDownlinkConfig.md) object
Required: No

 ** antennaDownlinkDemodDecodeConfig **   <a name="groundstation-Type-ConfigTypeData-antennaDownlinkDemodDecodeConfig"></a>
Information about how AWS Ground Station should conﬁgure an antenna for downlink demod decode during a contact.
Type: [AntennaDownlinkDemodDecodeConfig](API_AntennaDownlinkDemodDecodeConfig.md) object
Required: No

 ** antennaUplinkConfig **   <a name="groundstation-Type-ConfigTypeData-antennaUplinkConfig"></a>
Information about how AWS Ground Station should conﬁgure an antenna for uplink during a contact.
Type: [AntennaUplinkConfig](API_AntennaUplinkConfig.md) object
Required: No

 ** dataflowEndpointConfig **   <a name="groundstation-Type-ConfigTypeData-dataflowEndpointConfig"></a>
Information about the dataflow endpoint `Config`.
Type: [DataflowEndpointConfig](API_DataflowEndpointConfig.md) object
Required: No

 ** s3RecordingConfig **   <a name="groundstation-Type-ConfigTypeData-s3RecordingConfig"></a>
Information about an S3 recording `Config`.
Type: [S3RecordingConfig](API_S3RecordingConfig.md) object
Required: No

 ** telemetrySinkConfig **   <a name="groundstation-Type-ConfigTypeData-telemetrySinkConfig"></a>
Information about a telemetry sink `Config`.
Type: [TelemetrySinkConfig](API_TelemetrySinkConfig.md) object
Required: No

 ** trackingConfig **   <a name="groundstation-Type-ConfigTypeData-trackingConfig"></a>
Object that determines whether tracking should be used during a contact executed with this `Config` in the mission profile.
Type: [TrackingConfig](API_TrackingConfig.md) object
Required: No

 ** uplinkEchoConfig **   <a name="groundstation-Type-ConfigTypeData-uplinkEchoConfig"></a>
Information about an uplink echo `Config`.
Parameters from the `AntennaUplinkConfig`, corresponding to the specified ` AntennaUplinkConfigArn`, are used when this `UplinkEchoConfig` is used in a contact.
Type: [UplinkEchoConfig](API_UplinkEchoConfig.md) object
Required: No

## See Also
<a name="API_ConfigTypeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ConfigTypeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ConfigTypeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ConfigTypeData)
