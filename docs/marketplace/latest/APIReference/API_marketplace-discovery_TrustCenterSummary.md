---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterSummary.html
---

# TrustCenterSummary

A summary of trust center information associated with a listing.

## Contents
<a name="API_marketplace-discovery_TrustCenterSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** certificationSummaries **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSummary-certificationSummaries"></a>
A subset of certifications associated with the listing, selected by importance.
Type: Array of [TrustCenterCertificationSummary](API_marketplace-discovery_TrustCenterCertificationSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** sourceSummaries **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSummary-sourceSummaries"></a>
Trust center source summaries associated with the listing.
Type: Array of [TrustCenterSourceSummary](API_marketplace-discovery_TrustCenterSourceSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** totalCertificationCount **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSummary-totalCertificationCount"></a>
The total number of distinct certifications associated with the listing, including certifications omitted from `certificationSummaries`.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_marketplace-discovery_TrustCenterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterSummary)
