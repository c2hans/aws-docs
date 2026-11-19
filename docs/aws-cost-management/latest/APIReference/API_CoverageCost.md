---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageCost.html
---

# CoverageCost

The cost of the On-Demand Instance usage that reservations didn't cover.

## Contents
<a name="API_CoverageCost_Contents"></a>

 ** OnDemandCost **   <a name="awscostmanagement-Type-CoverageCost-OnDemandCost"></a>
The cost of the On-Demand Instance usage that reservations didn't cover (the usage in `OnDemandHours`), at public On-Demand rates. It doesn't include Spot usage or usage that Savings Plans covered. This isn't your billed cost. It's 0 for usage that has no public On-Demand rate.
Type: String
Required: No

## See Also
<a name="API_CoverageCost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CoverageCost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CoverageCost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CoverageCost)
