---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SessionDataSortBy.html
---

# SessionDataSortBy
<a name="API_SessionDataSortBy"></a>

An object specifying the measure and method by which to sort the session analytics data.

## Contents
<a name="API_SessionDataSortBy_Contents"></a>

 ** name **   <a name="lexv2-Type-SessionDataSortBy-name"></a>
The measure by which to sort the session analytics data.
+  `conversationStartTime` – The date and time when the conversation began. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
+  `numberOfTurns` – The number of turns that the session took.
+  `conversationDurationSeconds` – The duration of the conversation in seconds.
Type: String
Valid Values: `ConversationStartTime | NumberOfTurns | Duration`
Required: Yes

 ** order **   <a name="lexv2-Type-SessionDataSortBy-order"></a>
Specifies whether to sort the results in ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: Yes

## See Also
<a name="API_SessionDataSortBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SessionDataSortBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SessionDataSortBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SessionDataSortBy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
