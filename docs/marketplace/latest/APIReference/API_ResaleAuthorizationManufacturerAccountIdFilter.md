---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ResaleAuthorizationManufacturerAccountIdFilter.html
---

# ResaleAuthorizationManufacturerAccountIdFilter
<a name="API_ResaleAuthorizationManufacturerAccountIdFilter"></a>

Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization.

## Contents
<a name="API_ResaleAuthorizationManufacturerAccountIdFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationManufacturerAccountIdFilter-ValueList"></a>
Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization with list input.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** WildCardValue **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationManufacturerAccountIdFilter-WildCardValue"></a>
Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization with wild card input.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_ResaleAuthorizationManufacturerAccountIdFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ResaleAuthorizationManufacturerAccountIdFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ResaleAuthorizationManufacturerAccountIdFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ResaleAuthorizationManufacturerAccountIdFilter)
