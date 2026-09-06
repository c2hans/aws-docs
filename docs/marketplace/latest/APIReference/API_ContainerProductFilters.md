---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ContainerProductFilters.html
---

# ContainerProductFilters
<a name="API_ContainerProductFilters"></a>

Object containing all the filter fields for container products. Client can add only one wildcard filter and a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_ContainerProductFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityId **   <a name="AWSMarketplaceService-Type-ContainerProductFilters-EntityId"></a>
Unique identifier for the container product.
Type: [ContainerProductEntityIdFilter](API_ContainerProductEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-ContainerProductFilters-LastModifiedDate"></a>
The last date on which the container product was modified.
Type: [ContainerProductLastModifiedDateFilter](API_ContainerProductLastModifiedDateFilter.md) object
Required: No

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-ContainerProductFilters-ProductTitle"></a>
The title of the container product.
Type: [ContainerProductTitleFilter](API_ContainerProductTitleFilter.md) object
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-ContainerProductFilters-Visibility"></a>
The visibility of the container product.
Type: [ContainerProductVisibilityFilter](API_ContainerProductVisibilityFilter.md) object
Required: No

## See Also
<a name="API_ContainerProductFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ContainerProductFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ContainerProductFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ContainerProductFilters)
