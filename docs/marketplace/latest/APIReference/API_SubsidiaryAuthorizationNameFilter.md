---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationNameFilter.html
---

# SubsidiaryAuthorizationNameFilter
<a name="API_SubsidiaryAuthorizationNameFilter"></a>

The filter for subsidiary authorization names.

## Contents
<a name="API_SubsidiaryAuthorizationNameFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationNameFilter-ValueList"></a>
A list of names to filter by. The operation returns subsidiary authorizations with a name that matches any value in this list. You can include up to 10 names in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** WildCardValue **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationNameFilter-WildCardValue"></a>
A partial name to filter by. The operation returns subsidiary authorizations whose name contains this value. The value must be at least 3 characters.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationNameFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationNameFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationNameFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationNameFilter)
