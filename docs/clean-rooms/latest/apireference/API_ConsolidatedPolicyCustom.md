---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ConsolidatedPolicyCustom.html
---

# ConsolidatedPolicyCustom
<a name="API_ConsolidatedPolicyCustom"></a>

Controls on the analysis specifications that can be run on a configured table.

## Contents
<a name="API_ConsolidatedPolicyCustom_Contents"></a>

 ** allowedAnalyses **   <a name="API-Type-ConsolidatedPolicyCustom-allowedAnalyses"></a>
 The allowed analyses.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `(ANY_QUERY|ANY_JOB|arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+)`
Required: Yes

 ** additionalAnalyses **   <a name="API-Type-ConsolidatedPolicyCustom-additionalAnalyses"></a>
 Additional analyses for the consolidated policy.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: No

 ** aggregationThresholds **   <a name="API-Type-ConsolidatedPolicyCustom-aggregationThresholds"></a>
 The aggregation thresholds for the consolidated policy.
Type: Array of [AggregationThreshold](API_AggregationThreshold.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** allowedAdditionalAnalyses **   <a name="API-Type-ConsolidatedPolicyCustom-allowedAdditionalAnalyses"></a>
 The additional analyses allowed by the consolidated policy.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: No

 ** allowedAnalysisProviders **   <a name="API-Type-ConsolidatedPolicyCustom-allowedAnalysisProviders"></a>
 The allowed analysis providers.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** allowedResultReceivers **   <a name="API-Type-ConsolidatedPolicyCustom-allowedResultReceivers"></a>
 The allowed result receivers.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** comparisonControls **   <a name="API-Type-ConsolidatedPolicyCustom-comparisonControls"></a>
 The comparison controls for the consolidated policy.
Type: [ComparisonControls](API_ComparisonControls.md) object
Required: No

 ** differentialPrivacy **   <a name="API-Type-ConsolidatedPolicyCustom-differentialPrivacy"></a>
Specifies the unique identifier for your users.
Type: [DifferentialPrivacyConfiguration](API_DifferentialPrivacyConfiguration.md) object
Required: No

 ** disallowedOutputColumns **   <a name="API-Type-ConsolidatedPolicyCustom-disallowedOutputColumns"></a>
 Disallowed output columns
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: No

## See Also
<a name="API_ConsolidatedPolicyCustom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ConsolidatedPolicyCustom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ConsolidatedPolicyCustom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ConsolidatedPolicyCustom)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
