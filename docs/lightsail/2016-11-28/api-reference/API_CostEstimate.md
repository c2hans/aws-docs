---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CostEstimate.html
---

# CostEstimate
<a name="API_CostEstimate"></a>

Describes the estimated cost for resources in your Lightsail for Research account.

## Contents
<a name="API_CostEstimate_Contents"></a>

 ** resultsByTime **   <a name="Lightsail-Type-CostEstimate-resultsByTime"></a>
The cost estimate result that's associated with a time period.
Type: Array of [EstimateByTime](API_EstimateByTime.md) objects
Required: No

 ** usageType **   <a name="Lightsail-Type-CostEstimate-usageType"></a>
The types of usage that are included in the estimate, such as costs, usage, or data transfer.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_CostEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CostEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CostEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CostEstimate)
