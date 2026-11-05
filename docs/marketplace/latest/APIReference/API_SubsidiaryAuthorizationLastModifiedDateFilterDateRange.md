---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationLastModifiedDateFilterDateRange.html
---

# SubsidiaryAuthorizationLastModifiedDateFilterDateRange
<a name="API_SubsidiaryAuthorizationLastModifiedDateFilterDateRange"></a>

A date range for filtering subsidiary authorizations by last modified date.

## Contents
<a name="API_SubsidiaryAuthorizationLastModifiedDateFilterDateRange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AfterValue **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationLastModifiedDateFilterDateRange-AfterValue"></a>
The start date (inclusive) of the date range. The operation returns subsidiary authorizations last modified on or after this date.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

 ** BeforeValue **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationLastModifiedDateFilterDateRange-BeforeValue"></a>
The end date (inclusive) of the date range. The operation returns subsidiary authorizations last modified on or before this date.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationLastModifiedDateFilterDateRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationLastModifiedDateFilterDateRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationLastModifiedDateFilterDateRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationLastModifiedDateFilterDateRange)
