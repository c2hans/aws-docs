---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_TextMessage.html
---

# TextMessage
<a name="API_amazon-q-connect_TextMessage"></a>

The message data in text type.

## Contents
<a name="API_amazon-q-connect_TextMessage_Contents"></a>

 ** aiGuardrailAssessment **   <a name="connect-Type-amazon-q-connect_TextMessage-aiGuardrailAssessment"></a>
The AI Guardrail assessment for the text message.
Type: [AIGuardrailAssessment](API_amazon-q-connect_AIGuardrailAssessment.md) object
Required: No

 ** citations **   <a name="connect-Type-amazon-q-connect_TextMessage-citations"></a>
The citations associated with the text message.
Type: Array of [Citation](API_amazon-q-connect_Citation.md) objects
Required: No

 ** value **   <a name="connect-Type-amazon-q-connect_TextMessage-value"></a>
The value of the message data in text type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 25000.
Required: No

## See Also
<a name="API_amazon-q-connect_TextMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/TextMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/TextMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/TextMessage)
