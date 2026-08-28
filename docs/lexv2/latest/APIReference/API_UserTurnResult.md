---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UserTurnResult.html
---

# UserTurnResult
<a name="API_UserTurnResult"></a>

Contains the results for the user turn by the test execution.

## Contents
<a name="API_UserTurnResult_Contents"></a>

 ** expectedOutput **   <a name="lexv2-Type-UserTurnResult-expectedOutput"></a>
Contains information about the expected output for the user turn.
Type: [UserTurnOutputSpecification](API_UserTurnOutputSpecification.md) object
Required: Yes

 ** input **   <a name="lexv2-Type-UserTurnResult-input"></a>
Contains information about the user messages in the turn in the input.
Type: [UserTurnInputSpecification](API_UserTurnInputSpecification.md) object
Required: Yes

 ** actualOutput **   <a name="lexv2-Type-UserTurnResult-actualOutput"></a>
Contains information about the actual output for the user turn.
Type: [UserTurnOutputSpecification](API_UserTurnOutputSpecification.md) object
Required: No

 ** conversationLevelResult **   <a name="lexv2-Type-UserTurnResult-conversationLevelResult"></a>
Contains information about the results related to the conversation associated with the user turn.
Type: [ConversationLevelResultDetail](API_ConversationLevelResultDetail.md) object
Required: No

 ** endToEndResult **   <a name="lexv2-Type-UserTurnResult-endToEndResult"></a>
Specifies whether the expected and actual outputs match or not, or if there is an error in execution.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: No

 ** errorDetails **   <a name="lexv2-Type-UserTurnResult-errorDetails"></a>
Details about an error in an execution of a test set.
Type: [ExecutionErrorDetails](API_ExecutionErrorDetails.md) object
Required: No

 ** intentMatchResult **   <a name="lexv2-Type-UserTurnResult-intentMatchResult"></a>
Specifies whether the expected and actual intents match or not.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: No

 ** slotMatchResult **   <a name="lexv2-Type-UserTurnResult-slotMatchResult"></a>
Specifies whether the expected and actual slots match or not.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: No

 ** speechTranscriptionResult **   <a name="lexv2-Type-UserTurnResult-speechTranscriptionResult"></a>
Specifies whether the expected and actual speech transcriptions match or not, or if there is an error in execution.
Type: String
Valid Values: `Matched | Mismatched | ExecutionError`
Required: No

## See Also
<a name="API_UserTurnResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UserTurnResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UserTurnResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UserTurnResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
