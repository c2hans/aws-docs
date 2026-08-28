---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_OverallTestResultItem.html
---

# OverallTestResultItem
<a name="API_OverallTestResultItem"></a>

Information about the overall results for a test execution result.

## Contents
<a name="API_OverallTestResultItem_Contents"></a>

 ** endToEndResultCounts **   <a name="lexv2-Type-OverallTestResultItem-endToEndResultCounts"></a>
The number of results that succeeded.
Type: String to integer map
Valid Keys: `Matched | Mismatched | ExecutionError`
Required: Yes

 ** multiTurnConversation **   <a name="lexv2-Type-OverallTestResultItem-multiTurnConversation"></a>
Indicates whether the conversation contains multiple turns or not.
Type: Boolean
Required: Yes

 ** totalResultCount **   <a name="lexv2-Type-OverallTestResultItem-totalResultCount"></a>
The total number of overall results in the result of the test execution.
Type: Integer
Required: Yes

 ** speechTranscriptionResultCounts **   <a name="lexv2-Type-OverallTestResultItem-speechTranscriptionResultCounts"></a>
The number of speech transcription results in the overall test.
Type: String to integer map
Valid Keys: `Matched | Mismatched | ExecutionError`
Required: No

## See Also
<a name="API_OverallTestResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/OverallTestResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/OverallTestResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/OverallTestResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
