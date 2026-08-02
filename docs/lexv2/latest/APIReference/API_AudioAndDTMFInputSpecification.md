---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AudioAndDTMFInputSpecification.html
---

# AudioAndDTMFInputSpecification
<a name="API_AudioAndDTMFInputSpecification"></a>

Specifies the audio and DTMF input specification.

## Contents
<a name="API_AudioAndDTMFInputSpecification_Contents"></a>

 ** startTimeoutMs **   <a name="lexv2-Type-AudioAndDTMFInputSpecification-startTimeoutMs"></a>
Time for which a bot waits before assuming that the customer isn't going to speak or press a key. This timeout is shared between Audio and DTMF inputs.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** audioSpecification **   <a name="lexv2-Type-AudioAndDTMFInputSpecification-audioSpecification"></a>
Specifies the settings on audio input.
Type: [AudioSpecification](API_AudioSpecification.md) object
Required: No

 ** dtmfSpecification **   <a name="lexv2-Type-AudioAndDTMFInputSpecification-dtmfSpecification"></a>
Specifies the settings on DTMF input.
Type: [DTMFSpecification](API_DTMFSpecification.md) object
Required: No

## See Also
<a name="API_AudioAndDTMFInputSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AudioAndDTMFInputSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AudioAndDTMFInputSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AudioAndDTMFInputSpecification)
