---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchFilter.html
---

# SearchFilter
<a name="API_marketplace-discovery_SearchFilter"></a>

A filter used to narrow search results by attribute, such as category, pricing model, or fulfillment type.

## Contents
<a name="API_marketplace-discovery_SearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** filterType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SearchFilter-filterType"></a>
The type of filter to apply.
Type: String
Valid Values: `MIN_AVERAGE_CUSTOMER_RATING | MAX_AVERAGE_CUSTOMER_RATING | CATEGORY | PUBLISHER | FULFILLMENT_OPTION_TYPE | PRICING_MODEL | PRICING_UNIT | DEPLOYED_ON_AWS | NUMBER_OF_PRODUCTS`
Required: Yes

 ** filterValues **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SearchFilter-filterValues"></a>
The values to filter by. Term filters accept multiple values (OR logic). Range filters (MIN/MAX\_AVERAGE\_CUSTOMER\_RATING) accept a single value between 0.0 and 5.0.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\-\.]+`
Required: Yes

## See Also
<a name="API_marketplace-discovery_SearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SearchFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
