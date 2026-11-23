---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_OfferSubsidiaryAuthorizationIdFilter.html
---

# OfferSubsidiaryAuthorizationIdFilter

A filter that matches offers by the ID of the subsidiary authorization they were created from.

**Note**
Not all offers have a `SubsidiaryAuthorizationId`.

## Contents
<a name="API_OfferSubsidiaryAuthorizationIdFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-OfferSubsidiaryAuthorizationIdFilter-ValueList"></a>
A list of subsidiary authorization IDs to filter offers by. You can include up to 10 subsidiary authorization IDs in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 22.
Pattern: `^subauthz-[a-zA-Z0-9]{13}$`
Required: No

## See Also
<a name="API_OfferSubsidiaryAuthorizationIdFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/OfferSubsidiaryAuthorizationIdFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/OfferSubsidiaryAuthorizationIdFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/OfferSubsidiaryAuthorizationIdFilter)
