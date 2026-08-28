---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConversationLogsDataSource.html
---

# ConversationLogsDataSource
<a name="API_ConversationLogsDataSource"></a>

The data source that uses conversation logs.

## Contents
<a name="API_ConversationLogsDataSource_Contents"></a>

 ** botAliasId **   <a name="lexv2-Type-ConversationLogsDataSource-botAliasId"></a>
The bot alias Id from the conversation logs.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: Yes

 ** botId **   <a name="lexv2-Type-ConversationLogsDataSource-botId"></a>
The bot Id from the conversation logs.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** filter **   <a name="lexv2-Type-ConversationLogsDataSource-filter"></a>
The filter for the data source of the conversation log.
Type: [ConversationLogsDataSourceFilterBy](API_ConversationLogsDataSourceFilterBy.md) object
Required: Yes

 ** localeId **   <a name="lexv2-Type-ConversationLogsDataSource-localeId"></a>
The locale Id of the conversation log.
Type: String
Required: Yes

## See Also
<a name="API_ConversationLogsDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConversationLogsDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConversationLogsDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConversationLogsDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
