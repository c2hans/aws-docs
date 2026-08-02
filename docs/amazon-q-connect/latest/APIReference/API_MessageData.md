---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_MessageData.html
---

# MessageData
<a name="API_amazon-q-connect_MessageData"></a>

The message data.

## Contents
<a name="API_amazon-q-connect_MessageData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** text **   <a name="connect-Type-amazon-q-connect_MessageData-text"></a>
The message data in text type.
Type: [TextMessage](API_amazon-q-connect_TextMessage.md) object
Required: No

 ** toolUseResult **   <a name="connect-Type-amazon-q-connect_MessageData-toolUseResult"></a>
The result of tool usage in the message.
Type: [ToolUseResultData](API_amazon-q-connect_ToolUseResultData.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_MessageData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageData)
