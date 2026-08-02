---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteDriverScheduleInterval.html
---

# RouteDriverScheduleInterval
<a name="API_RouteDriverScheduleInterval"></a>

Interval of the driver work-rest schedule. Stops are added to fulfil the provided rest schedule.

## Contents
<a name="API_RouteDriverScheduleInterval_Contents"></a>

 ** DriveDuration **   <a name="location-Type-RouteDriverScheduleInterval-DriveDuration"></a>
Maximum allowed driving time before stopping to rest.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** RestDuration **   <a name="location-Type-RouteDriverScheduleInterval-RestDuration"></a>
Resting time before the driver can continue driving.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

## See Also
<a name="API_RouteDriverScheduleInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteDriverScheduleInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteDriverScheduleInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteDriverScheduleInterval)
