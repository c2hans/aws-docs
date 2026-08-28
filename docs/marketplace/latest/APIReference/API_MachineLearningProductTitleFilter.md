---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_MachineLearningProductTitleFilter.html
---

# MachineLearningProductTitleFilter
<a name="API_MachineLearningProductTitleFilter"></a>

The filter for machine learning product titles.

## Contents
<a name="API_MachineLearningProductTitleFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-MachineLearningProductTitleFilter-ValueList"></a>
A list of product titles to filter by. The operation returns machine learning products with titles that exactly match the values in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** WildCardValue **   <a name="AWSMarketplaceService-Type-MachineLearningProductTitleFilter-WildCardValue"></a>
A wildcard value to filter product titles. The operation returns machine learning products with titles that match this wildcard pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_MachineLearningProductTitleFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/MachineLearningProductTitleFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/MachineLearningProductTitleFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/MachineLearningProductTitleFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
