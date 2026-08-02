---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DTMFSpecification.html
---

# DTMFSpecification
<a name="API_DTMFSpecification"></a>

Specifies the DTMF input specifications.

## Contents
<a name="API_DTMFSpecification_Contents"></a>

 ** deletionCharacter **   <a name="lexv2-Type-DTMFSpecification-deletionCharacter"></a>
The DTMF character that clears the accumulated DTMF digits and immediately ends the input.
Type: String
Pattern: `^[A-D0-9#*]{1}$`
Required: Yes

 ** endCharacter **   <a name="lexv2-Type-DTMFSpecification-endCharacter"></a>
The DTMF character that immediately ends input. If the user does not press this character, the input ends after the end timeout.
Type: String
Pattern: `^[A-D0-9#*]{1}$`
Required: Yes

 ** endTimeoutMs **   <a name="lexv2-Type-DTMFSpecification-endTimeoutMs"></a>
How long the bot should wait after the last DTMF character input before assuming that the input has concluded.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** maxLength **   <a name="lexv2-Type-DTMFSpecification-maxLength"></a>
The maximum number of DTMF digits allowed in an utterance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: Yes

## See Also
<a name="API_DTMFSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DTMFSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DTMFSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DTMFSpecification)
