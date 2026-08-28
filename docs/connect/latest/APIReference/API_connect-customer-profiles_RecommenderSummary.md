---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_RecommenderSummary.html
---

# RecommenderSummary
<a name="API_connect-customer-profiles_RecommenderSummary"></a>

Provides a summary of a recommender's configuration and current state.

## Contents
<a name="API_connect-customer-profiles_RecommenderSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-CreatedAt"></a>
The timestamp when the recommender was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-Description"></a>
A description of the recommender's purpose and characteristics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** FailureReason **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-FailureReason"></a>
If the recommender is in a failed state, provides the reason for the failure.
Type: String
Required: No

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-LastUpdatedAt"></a>
The timestamp of when the recommender was edited.
Type: Timestamp
Required: No

 ** LatestRecommenderUpdate **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-LatestRecommenderUpdate"></a>
Information about the most recent update performed on the recommender, including its status and timing.
Type: [RecommenderUpdate](API_connect-customer-profiles_RecommenderUpdate.md) object
Required: No

 ** RecipeName **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-RecipeName"></a>
The name of the recipe used by this recommender.
Type: String
Valid Values: `recommended-for-you | similar-items | frequently-paired-items | popular-items | trending-now | personalized-ranking`
Required: No

 ** RecommenderConfig **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-RecommenderConfig"></a>
The configuration settings applied to this recommender.
Type: [RecommenderConfig](API_connect-customer-profiles_RecommenderConfig.md) object
Required: No

 ** RecommenderName **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-RecommenderName"></a>
The name of the recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** RecommenderSchemaName **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-RecommenderSchemaName"></a>
The name of the recommender schema associated with this recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-Status"></a>
The current operational status of the recommender.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE | FAILED | STOPPING | INACTIVE | STARTING | DELETING`
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_RecommenderSummary-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
