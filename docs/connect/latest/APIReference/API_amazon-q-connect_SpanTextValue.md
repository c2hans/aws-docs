---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SpanTextValue.html
---

# SpanTextValue
<a name="API_amazon-q-connect_SpanTextValue"></a>

Text message content

## Contents
<a name="API_amazon-q-connect_SpanTextValue_Contents"></a>

 ** value **   <a name="connect-Type-amazon-q-connect_SpanTextValue-value"></a>
String content of the message text
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** aiGuardrailAssessment **   <a name="connect-Type-amazon-q-connect_SpanTextValue-aiGuardrailAssessment"></a>
The AI Guardrail assessment for the span text.
Type: [AIGuardrailAssessment](API_amazon-q-connect_AIGuardrailAssessment.md) object
Required: No

 ** citations **   <a name="connect-Type-amazon-q-connect_SpanTextValue-citations"></a>
The citations associated with the span text.
Type: Array of [SpanCitation](API_amazon-q-connect_SpanCitation.md) objects
Required: No

## See Also
<a name="API_amazon-q-connect_SpanTextValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanTextValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanTextValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanTextValue)
