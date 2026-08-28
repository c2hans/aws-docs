---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_RecommenderUpdate.html
---

# RecommenderUpdate
<a name="API_connect-customer-profiles_RecommenderUpdate"></a>

Contains information about an update operation performed on a recommender.

## Contents
<a name="API_connect-customer-profiles_RecommenderUpdate_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_RecommenderUpdate-CreatedAt"></a>
The timestamp when this recommender update was initiated.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="connect-Type-connect-customer-profiles_RecommenderUpdate-FailureReason"></a>
If the update operation failed, provides the reason for the failure.
Type: String
Required: No

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_RecommenderUpdate-LastUpdatedAt"></a>
The timestamp of when the recommender was edited.
Type: Timestamp
Required: No

 ** RecommenderConfig **   <a name="connect-Type-connect-customer-profiles_RecommenderUpdate-RecommenderConfig"></a>
The updated configuration settings applied to the recommender during this update.
Type: [RecommenderConfig](API_connect-customer-profiles_RecommenderConfig.md) object
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_RecommenderUpdate-Status"></a>
The current status of the recommender update operation.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE | FAILED | STOPPING | INACTIVE | STARTING | DELETING`
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
