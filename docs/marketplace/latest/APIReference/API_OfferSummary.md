---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_OfferSummary.html
---

# OfferSummary
<a name="API_OfferSummary"></a>

Summarized information about an offer.

## Contents
<a name="API_OfferSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityEndDate **   <a name="AWSMarketplaceService-Type-OfferSummary-AvailabilityEndDate"></a>
The availability end date of the offer.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** BuyerAccounts **   <a name="AWSMarketplaceService-Type-OfferSummary-BuyerAccounts"></a>
The buyer accounts in the offer.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 26 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** CreatedBySource **   <a name="AWSMarketplaceService-Type-OfferSummary-CreatedBySource"></a>
The creation source of the offer.
Type: String
Valid Values: `Seller | AwsMarketplace`
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-OfferSummary-Name"></a>
The name of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `^(.)+$`
Required: No

 ** OfferSetId **   <a name="AWSMarketplaceService-Type-OfferSummary-OfferSetId"></a>
The offer set ID of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^offerset-[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

 ** ProductId **   <a name="AWSMarketplaceService-Type-OfferSummary-ProductId"></a>
The product ID of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** ReleaseDate **   <a name="AWSMarketplaceService-Type-OfferSummary-ReleaseDate"></a>
The release date of the offer.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** ResaleAuthorizationId **   <a name="AWSMarketplaceService-Type-OfferSummary-ResaleAuthorizationId"></a>
The ResaleAuthorizationId of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

 ** State **   <a name="AWSMarketplaceService-Type-OfferSummary-State"></a>
The status of the offer.
Type: String
Valid Values: `Draft | Released`
Required: No

 ** TargetAgreementId **   <a name="AWSMarketplaceService-Type-OfferSummary-TargetAgreementId"></a>
The target agreement ID of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(.)+$`
Required: No

 ** TargetAgreementIntent **   <a name="AWSMarketplaceService-Type-OfferSummary-TargetAgreementIntent"></a>
The target agreement intent of the offer.
Type: String
Valid Values: `Renew`
Required: No

 ** Targeting **   <a name="AWSMarketplaceService-Type-OfferSummary-Targeting"></a>
The targeting in the offer.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `BuyerAccounts | ParticipatingPrograms | CountryCodes | None`
Required: No

## See Also
<a name="API_OfferSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/OfferSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/OfferSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/OfferSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
