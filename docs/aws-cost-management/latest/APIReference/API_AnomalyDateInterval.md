---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyDateInterval.html
---

# AnomalyDateInterval
<a name="API_AnomalyDateInterval"></a>

The time period for an anomaly.

## Contents
<a name="API_AnomalyDateInterval_Contents"></a>

 ** StartDate **   <a name="awscostmanagement-Type-AnomalyDateInterval-StartDate"></a>
The first date an anomaly was observed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: Yes

 ** EndDate **   <a name="awscostmanagement-Type-AnomalyDateInterval-EndDate"></a>
The last date an anomaly was observed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: No

## See Also
<a name="API_AnomalyDateInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/AnomalyDateInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/AnomalyDateInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/AnomalyDateInterval)
