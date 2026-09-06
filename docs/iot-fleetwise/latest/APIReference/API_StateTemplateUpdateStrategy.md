---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StateTemplateUpdateStrategy.html
---

# StateTemplateUpdateStrategy
<a name="API_StateTemplateUpdateStrategy"></a>

The update strategy for the state template. Vehicles associated with the state template can stream telemetry data with either an `onChange` or `periodic` update strategy.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_StateTemplateUpdateStrategy_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** onChange **   <a name="iotfleetwise-Type-StateTemplateUpdateStrategy-onChange"></a>
Vehicles associated with the state template will stream telemetry data when there is a change.
Type: [OnChangeStateTemplateUpdateStrategy](API_OnChangeStateTemplateUpdateStrategy.md) object
Required: No

 ** periodic **   <a name="iotfleetwise-Type-StateTemplateUpdateStrategy-periodic"></a>
Vehicles associated with the state template will stream telemetry data during a specified time period.
Type: [PeriodicStateTemplateUpdateStrategy](API_PeriodicStateTemplateUpdateStrategy.md) object
Required: No

## See Also
<a name="API_StateTemplateUpdateStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StateTemplateUpdateStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StateTemplateUpdateStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StateTemplateUpdateStrategy)
