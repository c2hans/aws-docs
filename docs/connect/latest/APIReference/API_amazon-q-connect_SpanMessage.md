---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SpanMessage.html
---

# SpanMessage
<a name="API_amazon-q-connect_SpanMessage"></a>

A message in the conversation history with participant role and content values

## Contents
<a name="API_amazon-q-connect_SpanMessage_Contents"></a>

 ** messageId **   <a name="connect-Type-amazon-q-connect_SpanMessage-messageId"></a>
Unique message identifier
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** participant **   <a name="connect-Type-amazon-q-connect_SpanMessage-participant"></a>
Message source role
Type: String
Valid Values: `CUSTOMER | AGENT | BOT`
Required: Yes

 ** timestamp **   <a name="connect-Type-amazon-q-connect_SpanMessage-timestamp"></a>
Message timestamp
Type: Timestamp
Required: Yes

 ** values **   <a name="connect-Type-amazon-q-connect_SpanMessage-values"></a>
Message content values (text, tool use, tool result, reasoning)
Type: Array of [SpanMessageValue](API_amazon-q-connect_SpanMessageValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_amazon-q-connect_SpanMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanMessage)
