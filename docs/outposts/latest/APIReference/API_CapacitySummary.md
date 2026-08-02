---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CapacitySummary.html
---

# CapacitySummary
<a name="API_CapacitySummary"></a>

A summary of the capacity changes for a quote option.

## Contents
<a name="API_CapacitySummary_Contents"></a>

 ** CapacityChange **   <a name="outposts-Type-CapacitySummary-CapacityChange"></a>
The change in capacity between the existing and final state.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** ExistingCapacities **   <a name="outposts-Type-CapacitySummary-ExistingCapacities"></a>
The existing capacities on the Outpost before the quote is fulfilled.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** FinalCapacities **   <a name="outposts-Type-CapacitySummary-FinalCapacities"></a>
The final capacities on the Outpost after the quote is fulfilled.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

## See Also
<a name="API_CapacitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CapacitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CapacitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CapacitySummary)
