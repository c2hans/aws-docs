---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SaaSProductFilters.html
---

# SaaSProductFilters
<a name="API_SaaSProductFilters"></a>

Object containing all the filter fields for SaaS products. Client can add only one wildcard filter and a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_SaaSProductFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityId **   <a name="AWSMarketplaceService-Type-SaaSProductFilters-EntityId"></a>
Unique identifier for the SaaS product.
Type: [SaaSProductEntityIdFilter](API_SaaSProductEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-SaaSProductFilters-LastModifiedDate"></a>
The last date on which the SaaS product was modified.
Type: [SaaSProductLastModifiedDateFilter](API_SaaSProductLastModifiedDateFilter.md) object
Required: No

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-SaaSProductFilters-ProductTitle"></a>
The title of the SaaS product.
Type: [SaaSProductTitleFilter](API_SaaSProductTitleFilter.md) object
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-SaaSProductFilters-Visibility"></a>
The visibility of the SaaS product.
Type: [SaaSProductVisibilityFilter](API_SaaSProductVisibilityFilter.md) object
Required: No

## See Also
<a name="API_SaaSProductFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SaaSProductFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SaaSProductFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SaaSProductFilters)
