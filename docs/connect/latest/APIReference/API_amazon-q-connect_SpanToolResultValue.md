---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SpanToolResultValue.html
---

# SpanToolResultValue
<a name="API_amazon-q-connect_SpanToolResultValue"></a>

Tool result message content

## Contents
<a name="API_amazon-q-connect_SpanToolResultValue_Contents"></a>

 ** toolUseId **   <a name="connect-Type-amazon-q-connect_SpanToolResultValue-toolUseId"></a>
Relates this result back to the tool invocation
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** values **   <a name="connect-Type-amazon-q-connect_SpanToolResultValue-values"></a>
The tool results
Type: Array of [SpanMessageValue](API_amazon-q-connect_SpanMessageValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** error **   <a name="connect-Type-amazon-q-connect_SpanToolResultValue-error"></a>
The tool invocation error if failed
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_SpanToolResultValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanToolResultValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanToolResultValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanToolResultValue)
