---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_OfferSetLastModifiedDateFilterDateRange.html
---

# OfferSetLastModifiedDateFilterDateRange
<a name="API_OfferSetLastModifiedDateFilterDateRange"></a>

Allows filtering on the `LastModifiedDate` of an offer set with date range as input.

## Contents
<a name="API_OfferSetLastModifiedDateFilterDateRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AfterValue **   <a name="AWSMarketplaceService-Type-OfferSetLastModifiedDateFilterDateRange-AfterValue"></a>
Allows filtering on the `LastModifiedDate` of an offer set after a date.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** BeforeValue **   <a name="AWSMarketplaceService-Type-OfferSetLastModifiedDateFilterDateRange-BeforeValue"></a>
Allows filtering on the `LastModifiedDate` of an offer set before a date.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

## See Also
<a name="API_OfferSetLastModifiedDateFilterDateRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/OfferSetLastModifiedDateFilterDateRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/OfferSetLastModifiedDateFilterDateRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/OfferSetLastModifiedDateFilterDateRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
