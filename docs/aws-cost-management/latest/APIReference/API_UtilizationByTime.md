---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UtilizationByTime.html
---

# UtilizationByTime
<a name="API_UtilizationByTime"></a>

The amount of utilization, in hours.

## Contents
<a name="API_UtilizationByTime_Contents"></a>

 ** Groups **   <a name="awscostmanagement-Type-UtilizationByTime-Groups"></a>
The groups that this utilization result uses.
Type: Array of [ReservationUtilizationGroup](API_ReservationUtilizationGroup.md) objects
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-UtilizationByTime-TimePeriod"></a>
The period of time that this utilization was used for.
Type: [DateInterval](API_DateInterval.md) object
Required: No

 ** Total **   <a name="awscostmanagement-Type-UtilizationByTime-Total"></a>
The total number of reservation hours that were used.
Type: [ReservationAggregates](API_ReservationAggregates.md) object
Required: No

## See Also
<a name="API_UtilizationByTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/UtilizationByTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/UtilizationByTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/UtilizationByTime)
