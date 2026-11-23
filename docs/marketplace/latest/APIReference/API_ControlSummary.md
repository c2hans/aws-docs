---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ControlSummary.html
---

# ControlSummary

A summary of what a control produced. Exactly one member is set, corresponding to the kind of control.

## Contents
<a name="API_ControlSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ListingRecommendations **   <a name="AWSMarketplaceService-Type-ControlSummary-ListingRecommendations"></a>
The recommendations that a listing recommendations control produced for the listing.
Type: [ListingRecommendations](API_ListingRecommendations.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ControlSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ControlSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ControlSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ControlSummary)
