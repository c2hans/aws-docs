---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AudioSpecification.html
---

# AudioSpecification
<a name="API_AudioSpecification"></a>

Specifies the audio input specifications.

## Contents
<a name="API_AudioSpecification_Contents"></a>

 ** endTimeoutMs **   <a name="lexv2-Type-AudioSpecification-endTimeoutMs"></a>
Time for which a bot waits after the customer stops speaking to assume the utterance is finished.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** maxLengthMs **   <a name="lexv2-Type-AudioSpecification-maxLengthMs"></a>
Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_AudioSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AudioSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AudioSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AudioSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
