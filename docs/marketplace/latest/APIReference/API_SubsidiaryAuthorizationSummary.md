---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationSummary.html
---

# SubsidiaryAuthorizationSummary
<a name="API_SubsidiaryAuthorizationSummary"></a>

An object that contains summary information about a subsidiary authorization, including its name, status, authorized resource, subsidiary account, and creation date. A subsidiary authorization lets a seller authorize one of its subsidiary accounts to create offers for one of its products.

## Contents
<a name="API_SubsidiaryAuthorizationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedDate **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSummary-CreatedDate"></a>
The date the subsidiary authorization was created.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSummary-Name"></a>
The name of the subsidiary authorization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ResourceId **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSummary-ResourceId"></a>
The ID of the resource that the subsidiary authorization applies to. Currently, this is always a product ID, such as `prod-example123`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ResourceName **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSummary-ResourceName"></a>
The name of the resource that the subsidiary authorization applies to. Currently, this is always a product name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Status **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSummary-Status"></a>
The status of the subsidiary authorization. Valid values are:
+  `Draft` - The subsidiary authorization was created but not yet released. The subsidiary account can't see it.
+  `Active` - The subsidiary account can use the subsidiary authorization to create offers for the authorized product.
+  `Restricted` - The subsidiary authorization was discarded while in `Draft` or revoked while `Active`. It can't be used to create new offers. This status is final.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SubsidiaryAccountId **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSummary-SubsidiaryAccountId"></a>
The 12-digit AWS account ID of the subsidiary account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSummary)
