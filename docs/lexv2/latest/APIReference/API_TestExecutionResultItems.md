---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestExecutionResultItems.html
---

# TestExecutionResultItems
<a name="API_TestExecutionResultItems"></a>

Contains the results of the test execution, grouped by type of results. See [Test result details">Test results details](https://docs.aws.amazon.com/lexv2/latest/dg/test-results-details-test-set.html) for details about different types of results.

## Contents
<a name="API_TestExecutionResultItems_Contents"></a>

 ** conversationLevelTestResults **   <a name="lexv2-Type-TestExecutionResultItems-conversationLevelTestResults"></a>
Results related to conversations in the test set, including metrics about success and failure of conversations and intent and slot failures.
Type: [ConversationLevelTestResults](API_ConversationLevelTestResults.md) object
Required: No

 ** intentClassificationTestResults **   <a name="lexv2-Type-TestExecutionResultItems-intentClassificationTestResults"></a>
Intent recognition results aggregated by intent name. The aggregated results contain success and failure rates of intent recognition, speech transcriptions, and end-to-end conversations.
Type: [IntentClassificationTestResults](API_IntentClassificationTestResults.md) object
Required: No

 ** intentLevelSlotResolutionTestResults **   <a name="lexv2-Type-TestExecutionResultItems-intentLevelSlotResolutionTestResults"></a>
Slot resolution results aggregated by intent and slot name. The aggregated results contain success and failure rates of slot resolution, speech transcriptions, and end-to-end conversations
Type: [IntentLevelSlotResolutionTestResults](API_IntentLevelSlotResolutionTestResults.md) object
Required: No

 ** overallTestResults **   <a name="lexv2-Type-TestExecutionResultItems-overallTestResults"></a>
Overall results for the test execution, including the breakdown of conversations and single-input utterances.
Type: [OverallTestResults](API_OverallTestResults.md) object
Required: No

 ** utteranceLevelTestResults **   <a name="lexv2-Type-TestExecutionResultItems-utteranceLevelTestResults"></a>
Results related to utterances in the test set.
Type: [UtteranceLevelTestResults](API_UtteranceLevelTestResults.md) object
Required: No

## See Also
<a name="API_TestExecutionResultItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestExecutionResultItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestExecutionResultItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestExecutionResultItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
