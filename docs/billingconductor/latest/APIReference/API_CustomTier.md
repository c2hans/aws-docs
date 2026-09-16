---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CustomTier.html
---

# CustomTier
<a name="API_CustomTier"></a>

 A custom tier for the pricing rule. Each custom tier applies a rate to the usage that falls within the tier's range.

## Contents
<a name="API_CustomTier_Contents"></a>

 ** BeginRangeInclusive **   <a name="billingconductor-Type-CustomTier-BeginRangeInclusive"></a>
 The inclusive start of the usage range that this tier applies to.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** RateValue **   <a name="billingconductor-Type-CustomTier-RateValue"></a>
 The rate that's applied to the usage that falls within this tier.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** EndRangeExclusive **   <a name="billingconductor-Type-CustomTier-EndRangeExclusive"></a>
 The exclusive end of the usage range that this tier applies to. If you don't specify a value, this tier applies to all usage that is greater than or equal to `BeginRangeInclusive`.
Type: Double
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CustomTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CustomTier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CustomTier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CustomTier)
