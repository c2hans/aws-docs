---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_MachineLearningProductEntityIdFilter.html
---

# MachineLearningProductEntityIdFilter
<a name="API_MachineLearningProductEntityIdFilter"></a>

The filter for machine learning product entity IDs.

## Contents
<a name="API_MachineLearningProductEntityIdFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-MachineLearningProductEntityIdFilter-ValueList"></a>
A list of entity IDs to filter by. The operation returns machine learning products with entity IDs that match the values in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

## See Also
<a name="API_MachineLearningProductEntityIdFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/MachineLearningProductEntityIdFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/MachineLearningProductEntityIdFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/MachineLearningProductEntityIdFilter)
