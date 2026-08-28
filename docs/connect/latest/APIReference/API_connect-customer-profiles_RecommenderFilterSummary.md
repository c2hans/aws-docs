---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_RecommenderFilterSummary.html
---

# RecommenderFilterSummary
<a name="API_connect-customer-profiles_RecommenderFilterSummary"></a>

Provides a summary of a recommender filter's configuration and current state.

## Contents
<a name="API_connect-customer-profiles_RecommenderFilterSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-CreatedAt"></a>
The timestamp when the recommender filter was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-Description"></a>
A description of the recommender filter's purpose and characteristics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** FailureReason **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-FailureReason"></a>
If the recommender filter is in a failed state, provides the reason for the failure.
Type: String
Required: No

 ** RecommenderFilterExpression **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-RecommenderFilterExpression"></a>
The filter expression that defines which items to include or exclude from recommendations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** RecommenderFilterName **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-RecommenderFilterName"></a>
The name of the recommender filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** RecommenderSchemaName **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-RecommenderSchemaName"></a>
The name of the recommender schema associated with this recommender filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-Status"></a>
The current operational status of the recommender filter.
Type: String
Valid Values: `ACTIVE | PENDING | IN_PROGRESS | FAILED | DELETING`
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_RecommenderFilterSummary-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderFilterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderFilterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderFilterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderFilterSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
