---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentClassificationTestResultItemCounts.html
---

# IntentClassificationTestResultItemCounts
<a name="API_IntentClassificationTestResultItemCounts"></a>

The number of items in the intent classification test.

## Contents
<a name="API_IntentClassificationTestResultItemCounts_Contents"></a>

 ** intentMatchResultCounts **   <a name="lexv2-Type-IntentClassificationTestResultItemCounts-intentMatchResultCounts"></a>
The number of matched and mismatched results for intent recognition for the intent.
Type: String to integer map
Valid Keys: `Matched | Mismatched | ExecutionError`
Required: Yes

 ** totalResultCount **   <a name="lexv2-Type-IntentClassificationTestResultItemCounts-totalResultCount"></a>
The total number of results in the intent classification test.
Type: Integer
Required: Yes

 ** speechTranscriptionResultCounts **   <a name="lexv2-Type-IntentClassificationTestResultItemCounts-speechTranscriptionResultCounts"></a>
The number of matched, mismatched, and execution error results for speech transcription for the intent.
Type: String to integer map
Valid Keys: `Matched | Mismatched | ExecutionError`
Required: No

## See Also
<a name="API_IntentClassificationTestResultItemCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/IntentClassificationTestResultItemCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/IntentClassificationTestResultItemCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/IntentClassificationTestResultItemCounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
