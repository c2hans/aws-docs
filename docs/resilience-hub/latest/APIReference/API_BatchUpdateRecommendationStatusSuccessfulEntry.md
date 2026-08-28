---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_BatchUpdateRecommendationStatusSuccessfulEntry.html
---

# BatchUpdateRecommendationStatusSuccessfulEntry
<a name="API_BatchUpdateRecommendationStatusSuccessfulEntry"></a>

List of operational recommendations that were successfully included or excluded.

## Contents
<a name="API_BatchUpdateRecommendationStatusSuccessfulEntry_Contents"></a>

 ** entryId **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusSuccessfulEntry-entryId"></a>
An identifier for an entry in this batch that is used to communicate the result.
The `entryId`s of a batch request need to be unique within a request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** excluded **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusSuccessfulEntry-excluded"></a>
Indicates if the operational recommendation was successfully excluded.
Type: Boolean
Required: Yes

 ** referenceId **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusSuccessfulEntry-referenceId"></a>
Reference identifier of the operational recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** appComponentId **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusSuccessfulEntry-appComponentId"></a>
Indicates the identifier of an AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: No

 ** excludeReason **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusSuccessfulEntry-excludeReason"></a>
Indicates the reason for excluding an operational recommendation.
Type: String
Valid Values: `AlreadyImplemented | NotRelevant | ComplexityOfImplementation`
Required: No

 ** item **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusSuccessfulEntry-item"></a>
The operational recommendation item.
Type: [UpdateRecommendationStatusItem](API_UpdateRecommendationStatusItem.md) object
Required: No

## See Also
<a name="API_BatchUpdateRecommendationStatusSuccessfulEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/BatchUpdateRecommendationStatusSuccessfulEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/BatchUpdateRecommendationStatusSuccessfulEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/BatchUpdateRecommendationStatusSuccessfulEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
