---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PromptAttemptSpecification.html
---

# PromptAttemptSpecification
<a name="API_PromptAttemptSpecification"></a>

Specifies the settings on a prompt attempt.

## Contents
<a name="API_PromptAttemptSpecification_Contents"></a>

 ** allowedInputTypes **   <a name="lexv2-Type-PromptAttemptSpecification-allowedInputTypes"></a>
Indicates the allowed input types of the prompt attempt.
Type: [AllowedInputTypes](API_AllowedInputTypes.md) object
Required: Yes

 ** allowInterrupt **   <a name="lexv2-Type-PromptAttemptSpecification-allowInterrupt"></a>
Indicates whether the user can interrupt a speech prompt attempt from the bot.
Type: Boolean
Required: No

 ** audioAndDTMFInputSpecification **   <a name="lexv2-Type-PromptAttemptSpecification-audioAndDTMFInputSpecification"></a>
Specifies the settings on audio and DTMF input.
Type: [AudioAndDTMFInputSpecification](API_AudioAndDTMFInputSpecification.md) object
Required: No

 ** textInputSpecification **   <a name="lexv2-Type-PromptAttemptSpecification-textInputSpecification"></a>
Specifies the settings on text input.
Type: [TextInputSpecification](API_TextInputSpecification.md) object
Required: No

## See Also
<a name="API_PromptAttemptSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/PromptAttemptSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/PromptAttemptSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/PromptAttemptSpecification)
