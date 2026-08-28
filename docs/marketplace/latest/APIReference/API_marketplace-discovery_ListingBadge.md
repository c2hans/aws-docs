---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListingBadge.html
---

# ListingBadge
<a name="API_marketplace-discovery_ListingBadge"></a>

A badge indicating a special attribute of a listing, such as free tier eligibility or Quick Launch support.

## Contents
<a name="API_marketplace-discovery_ListingBadge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** badgeType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingBadge-badgeType"></a>
The machine-readable type of the badge.
Type: String
Valid Values: `AWS_FREE_TIER | FREE_TRIAL | DEPLOYED_ON_AWS | QUICK_LAUNCH | MULTI_PRODUCT`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingBadge-displayName"></a>
The human-readable name of the badge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_marketplace-discovery_ListingBadge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListingBadge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListingBadge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListingBadge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
