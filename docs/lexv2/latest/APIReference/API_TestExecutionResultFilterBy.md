---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestExecutionResultFilterBy.html
---

# TestExecutionResultFilterBy
<a name="API_TestExecutionResultFilterBy"></a>

Contains information about the method by which to filter the results of the test execution.

## Contents
<a name="API_TestExecutionResultFilterBy_Contents"></a>

 ** resultTypeFilter **   <a name="lexv2-Type-TestExecutionResultFilterBy-resultTypeFilter"></a>
Specifies which results to filter. See [Test result details">Test results details](https://docs.aws.amazon.com/lexv2/latest/dg/test-results-details-test-set.html) for details about different types of results.
Type: String
Valid Values: `OverallTestResults | ConversationLevelTestResults | IntentClassificationTestResults | SlotResolutionTestResults | UtteranceLevelResults`
Required: Yes

 ** conversationLevelTestResultsFilterBy **   <a name="lexv2-Type-TestExecutionResultFilterBy-conversationLevelTestResultsFilterBy"></a>
Contains information about the method for filtering Conversation level test results.
Type: [ConversationLevelTestResultsFilterBy](API_ConversationLevelTestResultsFilterBy.md) object
Required: No

## See Also
<a name="API_TestExecutionResultFilterBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestExecutionResultFilterBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestExecutionResultFilterBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestExecutionResultFilterBy)
