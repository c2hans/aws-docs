---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_RecommendationTrigger.html
---

# RecommendationTrigger
<a name="API_amazon-q-connect_RecommendationTrigger"></a>

A recommendation trigger provides context on the event that produced the referenced recommendations. Recommendations are only referenced in `recommendationIds` by a single RecommendationTrigger.

## Contents
<a name="API_amazon-q-connect_RecommendationTrigger_Contents"></a>

 ** data **   <a name="connect-Type-amazon-q-connect_RecommendationTrigger-data"></a>
A union type containing information related to the trigger.
Type: [RecommendationTriggerData](API_amazon-q-connect_RecommendationTriggerData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** id **   <a name="connect-Type-amazon-q-connect_RecommendationTrigger-id"></a>
The identifier of the recommendation trigger.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** recommendationIds **   <a name="connect-Type-amazon-q-connect_RecommendationTrigger-recommendationIds"></a>
The identifiers of the recommendations.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** source **   <a name="connect-Type-amazon-q-connect_RecommendationTrigger-source"></a>
The source of the recommendation trigger.
+ ISSUE\_DETECTION: The corresponding recommendations were triggered by a Contact Lens issue.
+ RULE\_EVALUATION: The corresponding recommendations were triggered by a Contact Lens rule.
Type: String
Valid Values: `ISSUE_DETECTION | RULE_EVALUATION | OTHER`
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_RecommendationTrigger-type"></a>
The type of recommendation trigger.
Type: String
Valid Values: `QUERY | GENERATIVE`
Required: Yes

## See Also
<a name="API_amazon-q-connect_RecommendationTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RecommendationTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RecommendationTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RecommendationTrigger)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
