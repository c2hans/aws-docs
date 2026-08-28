---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ResaleAuthorizationProductNameFilter.html
---

# ResaleAuthorizationProductNameFilter
<a name="API_ResaleAuthorizationProductNameFilter"></a>

Allows filtering on the `ProductName` of a ResaleAuthorization.

## Contents
<a name="API_ResaleAuthorizationProductNameFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValueList **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationProductNameFilter-ValueList"></a>
Allows filtering on the `ProductName` of a ResaleAuthorization with list input.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

 ** WildCardValue **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationProductNameFilter-WildCardValue"></a>
Allows filtering on the `ProductName` of a ResaleAuthorization with wild card input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_ResaleAuthorizationProductNameFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ResaleAuthorizationProductNameFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ResaleAuthorizationProductNameFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ResaleAuthorizationProductNameFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
