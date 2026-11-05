---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationStatusFilter.html
---

# SubsidiaryAuthorizationStatusFilter
<a name="API_SubsidiaryAuthorizationStatusFilter"></a>

The filter for subsidiary authorization statuses.

## Contents
<a name="API_SubsidiaryAuthorizationStatusFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationStatusFilter-ValueList"></a>
A list of statuses to filter by. The operation returns subsidiary authorizations with a status that matches a value in this list. Valid values are:
+  `Draft` - The subsidiary authorization was created but not yet released. The subsidiary account can't see it.
+  `Active` - The subsidiary account can use the subsidiary authorization to create offers for the authorized product.
+  `Restricted` - The subsidiary authorization was discarded while in `Draft` or revoked while `Active`. It can't be used to create new offers. This status is final.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `Draft | Active | Restricted`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationStatusFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationStatusFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationStatusFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationStatusFilter)
