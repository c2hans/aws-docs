---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationSort.html
---

# SubsidiaryAuthorizationSort
<a name="API_SubsidiaryAuthorizationSort"></a>

Specifies the field to sort subsidiary authorizations by and the order (ascending or descending) to apply.

## Contents
<a name="API_SubsidiaryAuthorizationSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSort-SortBy"></a>
The field to sort subsidiary authorizations by. Valid values are `EntityId`, `Status`, `ResourceId`, `SubsidiaryAccountId`, `CreatedDate`, and `LastModifiedDate`.
Type: String
Valid Values: `EntityId | Status | ResourceId | SubsidiaryAccountId | CreatedDate | LastModifiedDate`
Required: No

 ** SortOrder **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationSort-SortOrder"></a>
The sorting order. Can be `ASCENDING` or `DESCENDING`. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationSort)
