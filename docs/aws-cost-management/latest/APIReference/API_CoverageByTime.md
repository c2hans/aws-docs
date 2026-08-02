---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageByTime.html
---

# CoverageByTime
<a name="API_CoverageByTime"></a>

Reservation coverage for a specified period, in hours.

## Contents
<a name="API_CoverageByTime_Contents"></a>

 ** Groups **   <a name="awscostmanagement-Type-CoverageByTime-Groups"></a>
The groups of instances that the reservation covered.
Type: Array of [ReservationCoverageGroup](API_ReservationCoverageGroup.md) objects
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-CoverageByTime-TimePeriod"></a>
The period that this coverage was used over.
Type: [DateInterval](API_DateInterval.md) object
Required: No

 ** Total **   <a name="awscostmanagement-Type-CoverageByTime-Total"></a>
The total reservation coverage, in hours.
Type: [Coverage](API_Coverage.md) object
Required: No

## See Also
<a name="API_CoverageByTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CoverageByTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CoverageByTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CoverageByTime)
