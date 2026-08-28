---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_OfferSetSummary.html
---

# OfferSetSummary
<a name="API_OfferSetSummary"></a>

Summarized information about an offer set.

## Contents
<a name="API_OfferSetSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssociatedOfferIds **   <a name="AWSMarketplaceService-Type-OfferSetSummary-AssociatedOfferIds"></a>
The list of offer IDs associated with the offer set.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-OfferSetSummary-Name"></a>
The name of the offer set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `^(.)+$`
Required: No

 ** ReleaseDate **   <a name="AWSMarketplaceService-Type-OfferSetSummary-ReleaseDate"></a>
The release date of the offer set.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** SolutionId **   <a name="AWSMarketplaceService-Type-OfferSetSummary-SolutionId"></a>
The solution ID associated with the offer set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

 ** State **   <a name="AWSMarketplaceService-Type-OfferSetSummary-State"></a>
The state of the offer set.
Type: String
Valid Values: `Draft | Released`
Required: No

## See Also
<a name="API_OfferSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/OfferSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/OfferSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/OfferSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
