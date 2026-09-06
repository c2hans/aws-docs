---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SpanMessageValue.html
---

# SpanMessageValue
<a name="API_amazon-q-connect_SpanMessageValue"></a>

Message content value - can be text, tool invocation, tool result, or reasoning

## Contents
<a name="API_amazon-q-connect_SpanMessageValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoning **   <a name="connect-Type-amazon-q-connect_SpanMessageValue-reasoning"></a>
Model reasoning and it's internal decision making process
Type: [SpanReasoningValue](API_amazon-q-connect_SpanReasoningValue.md) object
Required: No

 ** text **   <a name="connect-Type-amazon-q-connect_SpanMessageValue-text"></a>
Text message content
Type: [SpanTextValue](API_amazon-q-connect_SpanTextValue.md) object
Required: No

 ** toolResult **   <a name="connect-Type-amazon-q-connect_SpanMessageValue-toolResult"></a>
Tool result message content
Type: [SpanToolResultValue](API_amazon-q-connect_SpanToolResultValue.md) object
Required: No

 ** toolUse **   <a name="connect-Type-amazon-q-connect_SpanMessageValue-toolUse"></a>
Tool invocation message content
Type: [SpanToolUseValue](API_amazon-q-connect_SpanToolUseValue.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_SpanMessageValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanMessageValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanMessageValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanMessageValue)
