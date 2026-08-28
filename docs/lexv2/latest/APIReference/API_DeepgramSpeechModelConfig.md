---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeepgramSpeechModelConfig.html
---

# DeepgramSpeechModelConfig
<a name="API_DeepgramSpeechModelConfig"></a>

Configuration settings for integrating Deepgram speech-to-text models with Amazon Lex.

## Contents
<a name="API_DeepgramSpeechModelConfig_Contents"></a>

 ** apiTokenSecretArn **   <a name="lexv2-Type-DeepgramSpeechModelConfig-apiTokenSecretArn"></a>
The Amazon Resource Name (ARN) of the Secrets Manager secret that contains the Deepgram API token.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[A-Za-z-]*:secretsmanager:[a-z0-9-]{1,20}:[0-9]{12}:secret:[A-Za-z0-9/_+=.@-]{1,512}-[A-Za-z0-9]{6}$`
Required: Yes

 ** modelId **   <a name="lexv2-Type-DeepgramSpeechModelConfig-modelId"></a>
The identifier of the Deepgram speech-to-text model to use for processing speech input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9-_]+`
Required: No

## See Also
<a name="API_DeepgramSpeechModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeepgramSpeechModelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeepgramSpeechModelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeepgramSpeechModelConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
