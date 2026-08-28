---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_RecommenderPromotionalFilter.html
---

# RecommenderPromotionalFilter
<a name="API_connect-customer-profiles_RecommenderPromotionalFilter"></a>

Contains information on a promotion. A promotion defines additional business rules that apply to a configurable subset of recommended items.

## Contents
<a name="API_connect-customer-profiles_RecommenderPromotionalFilter_Contents"></a>

 ** Name **   <a name="connect-Type-connect-customer-profiles_RecommenderPromotionalFilter-Name"></a>
The name of the recommender filter to use for the promotion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** PercentPromotedItems **   <a name="connect-Type-connect-customer-profiles_RecommenderPromotionalFilter-PercentPromotedItems"></a>
The percentage of recommended items to apply the promotion to.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** PromotionName **   <a name="connect-Type-connect-customer-profiles_RecommenderPromotionalFilter-PromotionName"></a>
The name of the promotion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** Values **   <a name="connect-Type-connect-customer-profiles_RecommenderPromotionalFilter-Values"></a>
The values to use when promoting items. For each placeholder parameter in your promotion's filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.
Type: String to string map
Map Entries: Maximum number of 25 items.
Key Length Constraints: Maximum length of 50.
Key Pattern: `[A-Za-z0-9_]+`
Value Length Constraints: Maximum length of 3000.
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderPromotionalFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderPromotionalFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderPromotionalFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderPromotionalFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
