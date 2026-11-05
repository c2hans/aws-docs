---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationEntityIdFilter.html
---

# SubsidiaryAuthorizationEntityIdFilter
<a name="API_SubsidiaryAuthorizationEntityIdFilter"></a>

The filter for subsidiary authorization entity IDs. Each ID begins with `subauthz-` followed by 13 alphanumeric characters.

## Contents
<a name="API_SubsidiaryAuthorizationEntityIdFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationEntityIdFilter-ValueList"></a>
A list of entity IDs to filter by. The operation returns subsidiary authorizations with an entity ID that matches any value in this list. You can include up to 10 entity IDs in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationEntityIdFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationEntityIdFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationEntityIdFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationEntityIdFilter)
