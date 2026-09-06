---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CallResult.html
---

# CallResult
<a name="API_CallResult"></a>

The result returned from executing a tool call.

## Contents
<a name="API_CallResult_Contents"></a>

 ** content **   <a name="novaact-Type-CallResult-content"></a>
The content returned by the tool execution, which can include text or other media types.
Type: Array of [CallResultContent](API_CallResultContent.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** callId **   <a name="novaact-Type-CallResult-callId"></a>
The identifier of the tool call that this result corresponds to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_CallResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/CallResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/CallResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/CallResult)
