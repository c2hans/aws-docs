---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationSubsidiaryAccountIdFilter.html
---

# SubsidiaryAuthorizationSubsidiaryAccountIdFilter
<a name="API_SubsidiaryAuthorizationSubsidiaryAccountIdFilter"></a>

The filter for the AWS account IDs of subsidiary accounts.

## Contents
<a name="API_SubsidiaryAuthorizationSubsidiaryAccountIdFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSubsidiaryAccountIdFilter-ValueList"></a>
A list of AWS account IDs to filter by. The operation returns subsidiary authorizations whose subsidiary account ID matches any value in this list. You can include up to 10 account IDs in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationSubsidiaryAccountIdFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSubsidiaryAccountIdFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSubsidiaryAccountIdFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSubsidiaryAccountIdFilter)
