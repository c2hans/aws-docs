---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UtteranceAudioInputSpecification.html
---

# UtteranceAudioInputSpecification
<a name="API_UtteranceAudioInputSpecification"></a>

Contains information about the audio for an utterance.

## Contents
<a name="API_UtteranceAudioInputSpecification_Contents"></a>

 ** audioFileS3Location **   <a name="lexv2-Type-UtteranceAudioInputSpecification-audioFileS3Location"></a>
Amazon S3 file pointing to the audio.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^s3://([a-z0-9\\.-]+)/(.+)$`
Required: Yes

## See Also
<a name="API_UtteranceAudioInputSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UtteranceAudioInputSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UtteranceAudioInputSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UtteranceAudioInputSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
