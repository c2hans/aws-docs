---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_DataProductFilters.html
---

# DataProductFilters
<a name="API_DataProductFilters"></a>

Object containing all the filter fields for data products. Client can add only one wildcard filter and a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_DataProductFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityId **   <a name="AWSMarketplaceService-Type-DataProductFilters-EntityId"></a>
Unique identifier for the data product.
Type: [DataProductEntityIdFilter](API_DataProductEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-DataProductFilters-LastModifiedDate"></a>
The last date on which the data product was modified.
Type: [DataProductLastModifiedDateFilter](API_DataProductLastModifiedDateFilter.md) object
Required: No

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-DataProductFilters-ProductTitle"></a>
The title of the data product.
Type: [DataProductTitleFilter](API_DataProductTitleFilter.md) object
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-DataProductFilters-Visibility"></a>
The visibility of the data product.
Type: [DataProductVisibilityFilter](API_DataProductVisibilityFilter.md) object
Required: No

## See Also
<a name="API_DataProductFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/DataProductFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/DataProductFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/DataProductFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
