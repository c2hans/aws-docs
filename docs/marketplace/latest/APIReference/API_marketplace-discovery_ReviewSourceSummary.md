---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ReviewSourceSummary.html
---

# ReviewSourceSummary
<a name="API_marketplace-discovery_ReviewSourceSummary"></a>

A review summary from a specific source, including the average rating and total review count.

## Contents
<a name="API_marketplace-discovery_ReviewSourceSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** averageRating **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ReviewSourceSummary-averageRating"></a>
The average rating across all reviews from this source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** sourceId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ReviewSourceSummary-sourceId"></a>
The machine-readable identifier of the review source.
Type: String
Valid Values: `AWS_MARKETPLACE`
Required: Yes

 ** sourceName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ReviewSourceSummary-sourceName"></a>
The name of the review source, such as AWS Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** totalReviews **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ReviewSourceSummary-totalReviews"></a>
The total number of reviews available from this source.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** sourceUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ReviewSourceSummary-sourceUrl"></a>
The URL where the reviews can be accessed at the source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: No

## See Also
<a name="API_marketplace-discovery_ReviewSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ReviewSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ReviewSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ReviewSourceSummary)
