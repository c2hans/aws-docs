---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ToolUseResultData.html
---

# ToolUseResultData
<a name="API_amazon-q-connect_ToolUseResultData"></a>

Data about the result of tool usage.

## Contents
<a name="API_amazon-q-connect_ToolUseResultData_Contents"></a>

 ** toolName **   <a name="connect-Type-amazon-q-connect_ToolUseResultData-toolName"></a>
The name of the tool that was used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** toolResult **   <a name="connect-Type-amazon-q-connect_ToolUseResultData-toolResult"></a>
The result of the tool usage.
Type: JSON value
Required: Yes

 ** toolUseId **   <a name="connect-Type-amazon-q-connect_ToolUseResultData-toolUseId"></a>
The identifier of the tool use instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** inputSchema **   <a name="connect-Type-amazon-q-connect_ToolUseResultData-inputSchema"></a>
The input schema for the tool use result.
Type: JSON value
Required: No

## See Also
<a name="API_amazon-q-connect_ToolUseResultData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ToolUseResultData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ToolUseResultData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ToolUseResultData)
