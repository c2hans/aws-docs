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
