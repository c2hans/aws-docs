---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_DeviceStatusReason.html
---

# DeviceStatusReason

Provides information about the reason for the current status of a device.

## Contents
<a name="API_DeviceStatusReason_Contents"></a>

 ** reason **   <a name="braket-Type-DeviceStatusReason-reason"></a>
The reason code for the current status of the device.
Type: String
Valid Values: `OUTSIDE_AVAILABILITY_WINDOW | MAINTENANCE | RESERVATION`
Required: Yes

 ** updatedAt **   <a name="braket-Type-DeviceStatusReason-updatedAt"></a>
The time of the most recent update to the device status reason.
Type: Timestamp
Required: Yes

 ** estimatedEndAt **   <a name="braket-Type-DeviceStatusReason-estimatedEndAt"></a>
The estimated time at which the current status reason will end.
Type: Timestamp
Required: No

 ** startedAt **   <a name="braket-Type-DeviceStatusReason-startedAt"></a>
The time at which the device status reason started.
Type: Timestamp
Required: No

## See Also
<a name="API_DeviceStatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/DeviceStatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/DeviceStatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/DeviceStatusReason)
