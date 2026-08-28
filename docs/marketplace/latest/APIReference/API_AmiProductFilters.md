---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_AmiProductFilters.html
---

# AmiProductFilters
<a name="API_AmiProductFilters"></a>

Object containing all the filter fields for AMI products. Client can add only one wildcard filter and a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_AmiProductFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityId **   <a name="AWSMarketplaceService-Type-AmiProductFilters-EntityId"></a>
Unique identifier for the AMI product.
Type: [AmiProductEntityIdFilter](API_AmiProductEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-AmiProductFilters-LastModifiedDate"></a>
The last date on which the AMI product was modified.
Type: [AmiProductLastModifiedDateFilter](API_AmiProductLastModifiedDateFilter.md) object
Required: No

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-AmiProductFilters-ProductTitle"></a>
The title of the AMI product.
Type: [AmiProductTitleFilter](API_AmiProductTitleFilter.md) object
Required: No

 ** Visibility **   <a name="AWSMarketplaceService-Type-AmiProductFilters-Visibility"></a>
The visibility of the AMI product.
Type: [AmiProductVisibilityFilter](API_AmiProductVisibilityFilter.md) object
Required: No

## See Also
<a name="API_AmiProductFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/AmiProductFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/AmiProductFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/AmiProductFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
