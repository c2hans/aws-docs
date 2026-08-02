---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageStatistics.html
---

# CoverageStatistics
<a name="API_CoverageStatistics"></a>

Information about the coverage statistics for a resource.

## Contents
<a name="API_CoverageStatistics_Contents"></a>

 ** countByCoverageStatus **   <a name="guardduty-Type-CoverageStatistics-countByCoverageStatus"></a>
Represents coverage statistics for EKS clusters aggregated by coverage status.
Type: String to long map
Valid Keys: `HEALTHY | UNHEALTHY`
Required: No

 ** countByResourceType **   <a name="guardduty-Type-CoverageStatistics-countByResourceType"></a>
Represents coverage statistics for EKS clusters aggregated by resource type.
Type: String to long map
Valid Keys: `EKS | ECS | EC2`
Required: No

## See Also
<a name="API_CoverageStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageStatistics)
