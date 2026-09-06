---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Filter.html
---

# Filter
<a name="API_marketplace-agreements_Filter"></a>

The filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as `offerId` or `productId`.

## Contents
<a name="API_marketplace-agreements_Filter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Filter-name"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z_]+`
Required: No

 ** values **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Filter-values"></a>
The filter value.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9.,+:/_-]+`
Required: No

## See Also
<a name="API_marketplace-agreements_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/Filter)
