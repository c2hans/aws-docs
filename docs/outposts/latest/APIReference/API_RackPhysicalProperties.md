---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_RackPhysicalProperties.html
---

# RackPhysicalProperties
<a name="API_RackPhysicalProperties"></a>

 Information about the physical and logistical details for racks at sites. For more information about hardware requirements for racks, see [Network readiness checklist](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist) in the AWS Outposts User Guide.

## Contents
<a name="API_RackPhysicalProperties_Contents"></a>

 ** FiberOpticCableType **   <a name="outposts-Type-RackPhysicalProperties-FiberOpticCableType"></a>
The type of fiber used to attach the Outpost to the network.
Type: String
Valid Values: `SINGLE_MODE | MULTI_MODE`
Required: No

 ** MaximumSupportedWeightLbs **   <a name="outposts-Type-RackPhysicalProperties-MaximumSupportedWeightLbs"></a>
The maximum rack weight that this site can support. `NO_LIMIT` is over 2000 lbs (907 kg).
Type: String
Valid Values: `NO_LIMIT | MAX_1400_LBS | MAX_1600_LBS | MAX_1800_LBS | MAX_2000_LBS`
Required: No

 ** OpticalStandard **   <a name="outposts-Type-RackPhysicalProperties-OpticalStandard"></a>
The type of optical standard used to attach the Outpost to the network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see [Network](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking) in the AWS Outposts User Guide.
Type: String
Valid Values: `OPTIC_10GBASE_SR | OPTIC_10GBASE_IR | OPTIC_10GBASE_LR | OPTIC_40GBASE_SR | OPTIC_40GBASE_ESR | OPTIC_40GBASE_IR4_LR4L | OPTIC_40GBASE_LR4 | OPTIC_100GBASE_SR4 | OPTIC_100GBASE_CWDM4 | OPTIC_100GBASE_LR4 | OPTIC_100G_PSM4_MSA | OPTIC_1000BASE_LX | OPTIC_1000BASE_SX`
Required: No

 ** PowerConnector **   <a name="outposts-Type-RackPhysicalProperties-PowerConnector"></a>
The power connector for the hardware.
Type: String
Valid Values: `L6_30P | IEC309 | AH530P7W | AH532P6W | CS8365C`
Required: No

 ** PowerDrawKva **   <a name="outposts-Type-RackPhysicalProperties-PowerDrawKva"></a>
The power draw available at the hardware placement position for the rack.
Type: String
Valid Values: `POWER_5_KVA | POWER_10_KVA | POWER_15_KVA | POWER_30_KVA`
Required: No

 ** PowerFeedDrop **   <a name="outposts-Type-RackPhysicalProperties-PowerFeedDrop"></a>
The position of the power feed.
Type: String
Valid Values: `ABOVE_RACK | BELOW_RACK`
Required: No

 ** PowerPhase **   <a name="outposts-Type-RackPhysicalProperties-PowerPhase"></a>
The power option that you can provide for hardware.
Type: String
Valid Values: `SINGLE_PHASE | THREE_PHASE`
Required: No

 ** UplinkCount **   <a name="outposts-Type-RackPhysicalProperties-UplinkCount"></a>
The number of uplinks each Outpost network device.
Type: String
Valid Values: `UPLINK_COUNT_1 | UPLINK_COUNT_2 | UPLINK_COUNT_3 | UPLINK_COUNT_4 | UPLINK_COUNT_5 | UPLINK_COUNT_6 | UPLINK_COUNT_7 | UPLINK_COUNT_8 | UPLINK_COUNT_12 | UPLINK_COUNT_16`
Required: No

 ** UplinkGbps **   <a name="outposts-Type-RackPhysicalProperties-UplinkGbps"></a>
The uplink speed the rack supports for the connection to the Region.
Type: String
Valid Values: `UPLINK_1G | UPLINK_10G | UPLINK_40G | UPLINK_100G`
Required: No

## See Also
<a name="API_RackPhysicalProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/RackPhysicalProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/RackPhysicalProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/RackPhysicalProperties)
