---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StorageMinimumTimeToLive.html
---

# StorageMinimumTimeToLive
<a name="API_StorageMinimumTimeToLive"></a>

Information about the minimum amount of time that data will be kept.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_StorageMinimumTimeToLive_Contents"></a>

 ** unit **   <a name="iotfleetwise-Type-StorageMinimumTimeToLive-unit"></a>
The time increment type.
Type: String
Valid Values: `HOURS | DAYS | WEEKS`
Required: Yes

 ** value **   <a name="iotfleetwise-Type-StorageMinimumTimeToLive-value"></a>
The minimum amount of time to store the data.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 876600.
Required: Yes

## See Also
<a name="API_StorageMinimumTimeToLive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StorageMinimumTimeToLive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StorageMinimumTimeToLive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StorageMinimumTimeToLive)
