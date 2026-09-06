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
