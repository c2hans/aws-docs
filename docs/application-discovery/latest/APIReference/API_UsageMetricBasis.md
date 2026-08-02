---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_UsageMetricBasis.html
---

# UsageMetricBasis
<a name="API_UsageMetricBasis"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 Specifies the performance metrics to use for the server that is used for recommendations.

## Contents
<a name="API_UsageMetricBasis_Contents"></a>

 ** name **   <a name="DiscServ-Type-UsageMetricBasis-name"></a>
 A utilization metric that is used by the recommendations.
Type: String
Pattern: `^(p(\d{1,2}|100)|AVG|SPEC|MAX)$`
Required: No

 ** percentageAdjust **   <a name="DiscServ-Type-UsageMetricBasis-percentageAdjust"></a>
 Specifies the percentage of the specified utilization metric that is used by the recommendations.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: No

## See Also
<a name="API_UsageMetricBasis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/UsageMetricBasis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/UsageMetricBasis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/UsageMetricBasis)
