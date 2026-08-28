---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SpeechFoundationModel.html
---

# SpeechFoundationModel
<a name="API_SpeechFoundationModel"></a>

Configuration for a foundation model used for speech synthesis and recognition capabilities.

## Contents
<a name="API_SpeechFoundationModel_Contents"></a>

 ** modelArn **   <a name="lexv2-Type-SpeechFoundationModel-modelArn"></a>
The Amazon Resource Name (ARN) of the foundation model used for speech processing.
Type: String
Pattern: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model\/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}$`
Required: Yes

 ** voiceId **   <a name="lexv2-Type-SpeechFoundationModel-voiceId"></a>
The identifier of the voice to use for speech synthesis with the foundation model.
Type: String
Required: No

## See Also
<a name="API_SpeechFoundationModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SpeechFoundationModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SpeechFoundationModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SpeechFoundationModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
