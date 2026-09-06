---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_MachineLearningProductFilters.html
---

# MachineLearningProductFilters
<a name="API_MachineLearningProductFilters"></a>

The filters that you can use with the ListEntities operation to filter machine learning products. You can filter by `EntityId`, `astModifiedDate`, `ProductTitle`, and `Visibility`.

## Contents
<a name="API_MachineLearningProductFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityId **   <a name="AWSMarketplaceService-Type-MachineLearningProductFilters-EntityId"></a>
Filter machine learning products by their entity IDs.
Type: [MachineLearningProductEntityIdFilter](API_MachineLearningProductEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-MachineLearningProductFilters-LastModifiedDate"></a>
Filter machine learning products by their last modified date.
Type: [MachineLearningProductLastModifiedDateFilter](API_MachineLearningProductLastModifiedDateFilter.md) object
Required: No

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-MachineLearningProductFilters-ProductTitle"></a>
Filter machine learning products by their product titles.
Type: [MachineLearningProductTitleFilter](API_MachineLearningProductTitleFilter.md) object
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-MachineLearningProductFilters-Visibility"></a>
Filter machine learning products by their visibility status.
Type: [MachineLearningProductVisibilityFilter](API_MachineLearningProductVisibilityFilter.md) object
Required: No

## See Also
<a name="API_MachineLearningProductFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/MachineLearningProductFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/MachineLearningProductFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/MachineLearningProductFilters)
