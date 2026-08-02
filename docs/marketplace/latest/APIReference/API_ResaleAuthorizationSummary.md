---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ResaleAuthorizationSummary.html
---

# ResaleAuthorizationSummary
<a name="API_ResaleAuthorizationSummary"></a>

Summarized information about a Resale Authorization.

## Contents
<a name="API_ResaleAuthorizationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityEndDate **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-AvailabilityEndDate"></a>
The availability end date of the ResaleAuthorization.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** CreatedDate **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-CreatedDate"></a>
The created date of the ResaleAuthorization.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** ManufacturerAccountId **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-ManufacturerAccountId"></a>
The manufacturer account ID of the ResaleAuthorization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** ManufacturerLegalName **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-ManufacturerLegalName"></a>
The manufacturer legal name of the ResaleAuthorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-Name"></a>
The name of the ResaleAuthorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** OfferExtendedStatus **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-OfferExtendedStatus"></a>
The offer extended status of the ResaleAuthorization
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** ProductId **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-ProductId"></a>
The product ID of the ResaleAuthorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** ProductName **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-ProductName"></a>
The product name of the ResaleAuthorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** ResellerAccountID **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-ResellerAccountID"></a>
The reseller account ID of the ResaleAuthorization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** ResellerLegalName **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-ResellerLegalName"></a>
The reseller legal name of the ResaleAuthorization
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** Status **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationSummary-Status"></a>
The status of the ResaleAuthorization.
Type: String
Valid Values: `Draft | Active | Restricted`
Required: No

## See Also
<a name="API_ResaleAuthorizationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ResaleAuthorizationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ResaleAuthorizationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ResaleAuthorizationSummary)
