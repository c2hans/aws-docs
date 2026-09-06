---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_SignalFetchConfig.html
---

# SignalFetchConfig
<a name="API_SignalFetchConfig"></a>

The configuration of the signal fetch operation.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_SignalFetchConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conditionBased **   <a name="iotfleetwise-Type-SignalFetchConfig-conditionBased"></a>
The configuration of a condition-based signal fetch operation.
Type: [ConditionBasedSignalFetchConfig](API_ConditionBasedSignalFetchConfig.md) object
Required: No

 ** timeBased **   <a name="iotfleetwise-Type-SignalFetchConfig-timeBased"></a>
The configuration of a time-based signal fetch operation.
Type: [TimeBasedSignalFetchConfig](API_TimeBasedSignalFetchConfig.md) object
Required: No

## See Also
<a name="API_SignalFetchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/SignalFetchConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/SignalFetchConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/SignalFetchConfig)
