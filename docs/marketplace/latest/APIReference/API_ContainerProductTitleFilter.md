---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ContainerProductTitleFilter.html
---

# ContainerProductTitleFilter
<a name="API_ContainerProductTitleFilter"></a>

Object that allows filtering on product title.

## Contents
<a name="API_ContainerProductTitleFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-ContainerProductTitleFilter-ValueList"></a>
A string array of unique product title values to be filtered on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** WildCardValue **   <a name="AWSMarketplaceService-Type-ContainerProductTitleFilter-WildCardValue"></a>
A string that will be the `wildCard` input for product tile filter. It matches the provided value as a substring in the actual value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_ContainerProductTitleFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ContainerProductTitleFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ContainerProductTitleFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ContainerProductTitleFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
