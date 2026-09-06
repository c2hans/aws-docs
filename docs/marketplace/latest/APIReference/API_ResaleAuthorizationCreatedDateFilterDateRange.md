---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ResaleAuthorizationCreatedDateFilterDateRange.html
---

# ResaleAuthorizationCreatedDateFilterDateRange
<a name="API_ResaleAuthorizationCreatedDateFilterDateRange"></a>

Allows filtering on `CreatedDate` of a ResaleAuthorization with date range as input.

## Contents
<a name="API_ResaleAuthorizationCreatedDateFilterDateRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AfterValue **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationCreatedDateFilterDateRange-AfterValue"></a>
Allows filtering on `CreatedDate` of a ResaleAuthorization after a date.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** BeforeValue **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationCreatedDateFilterDateRange-BeforeValue"></a>
Allows filtering on `CreatedDate` of a ResaleAuthorization before a date.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

## See Also
<a name="API_ResaleAuthorizationCreatedDateFilterDateRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ResaleAuthorizationCreatedDateFilterDateRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ResaleAuthorizationCreatedDateFilterDateRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ResaleAuthorizationCreatedDateFilterDateRange)
