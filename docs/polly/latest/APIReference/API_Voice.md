---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_Voice.html
---

# Voice

Describes a voice. Amazon Polly provides voices, and you can create custom voices with `CreateVoice`. `Origin` indicates whether Amazon Polly provides the voice or you created it. `DescribeVoices` returns a subset of the fields for each voice. `GetVoice` returns all fields of a custom voice.

## Contents
<a name="API_Voice_Contents"></a>

 ** AdditionalLanguageCodes **   <a name="polly-Type-Voice-AdditionalLanguageCodes"></a>
Additional codes for languages available for the specified voice in addition to its default language.
For example, the default language for Aditi is Indian English (en-IN) because it was first used for that language. Since Aditi is bilingual and fluent in both Indian English and Hindi, this parameter would show the code `hi-IN`.
Type: Array of strings
Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH | en-SG`
Required: No

 ** Arn **   <a name="polly-Type-Voice-Arn"></a>
The Amazon Resource Name (ARN) of a custom voice, in the form `arn:partition:polly:region:account-id:voice/voice-id`. `CreateVoice` and `GetVoice` return this field. Voices that Amazon Polly provides don't have an ARN.
Type: String
Pattern: `^arn:aws(-(cn|iso(-b)?|us-gov|eusc))?:polly:[a-z0-9_-]{1,50}:\d{12}:voice/[a-zA-Z0-9_-]+$`
Required: No

 ** CreationTime **   <a name="polly-Type-Voice-CreationTime"></a>
The date and time when you created the custom voice. Voices that Amazon Polly provides don't include this field.
Type: Timestamp
Required: No

 ** CustomerManagedEncryption **   <a name="polly-Type-Voice-CustomerManagedEncryption"></a>
The customer managed key that encrypts your custom voice. `CreateVoice` and `GetVoice` return this field if you specified a key in `CreateVoice`.
Type: [CustomerManagedEncryption](API_CustomerManagedEncryption.md) object
Required: No

 ** Gender **   <a name="polly-Type-Voice-Gender"></a>
The gender of the voice. Custom voices don't include this field.
Type: String
Valid Values: `Female | Male`
Required: No

 ** Id **   <a name="polly-Type-Voice-Id"></a>
The voice ID that Amazon Polly assigns. You specify this ID when you call the `SynthesizeSpeech` operation. For a custom voice, Amazon Polly assigns an ID that consists of `vc-` followed by hexadecimal characters, for example, `vc-9a8fa85dd3`.
Type: String
Valid Values: `Aditi | Amy | Astrid | Bianca | Brian | Camila | Carla | Carmen | Celine | Chantal | Conchita | Cristiano | Dora | Emma | Enrique | Ewa | Filiz | Gabrielle | Geraint | Giorgio | Gwyneth | Hans | Ines | Ivy | Jacek | Jan | Joanna | Joey | Justin | Karl | Kendra | Kevin | Kimberly | Lea | Liv | Lotte | Lucia | Lupe | Mads | Maja | Marlene | Mathieu | Matthew | Maxim | Mia | Miguel | Mizuki | Naja | Nicole | Olivia | Penelope | Raveena | Ricardo | Ruben | Russell | Salli | Seoyeon | Takumi | Tatyana | Vicki | Vitoria | Zeina | Zhiyu | Aria | Ayanda | Arlet | Hannah | Arthur | Daniel | Liam | Pedro | Kajal | Hiujin | Laura | Elin | Ida | Suvi | Ola | Hala | Andres | Sergio | Remi | Adriano | Thiago | Ruth | Stephen | Kazuha | Tomoko | Niamh | Sofie | Lisa | Isabelle | Zayd | Danielle | Gregory | Burcu | Jitka | Sabrina | Jasmine | Jihye | Ambre | Beatrice | Florian | Lennart | Lorenzo | Tiffany | Arjun | Carlos | Carolina | Curtis | Hyunduk | Kenneth | Kiara | Leo | Nate | Tina`
Required: No

 ** LanguageCode **   <a name="polly-Type-Voice-LanguageCode"></a>
Language code of the voice.
Type: String
Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH | en-SG`
Required: No

 ** LanguageName **   <a name="polly-Type-Voice-LanguageName"></a>
Human readable name of the language in English.
Type: String
Required: No

 ** Name **   <a name="polly-Type-Voice-Name"></a>
The name of the voice, for example, Salli or Kendra. The name is human-readable, and you might display it in your application. For a custom voice, this is the `Name` that you specified in `CreateVoice`.
Type: String
Required: No

 ** Origin **   <a name="polly-Type-Voice-Origin"></a>
Indicates who provides the voice. The origin is one of the following:
aws
A voice that Amazon Polly provides.
customer
A custom voice that you created with `CreateVoice`.
Type: String
Valid Values: `aws | customer`
Required: No

 ** Status **   <a name="polly-Type-Voice-Status"></a>
The status of a custom voice. Voices that Amazon Polly provides don't include this field. The status is one of the following:
pending
Amazon Polly is creating the voice.
active
The voice is ready for speech synthesis.
failed
Amazon Polly couldn't create the voice. `StatusReason` describes why.
Type: String
Valid Values: `pending | active | failed`
Required: No

 ** StatusReason **   <a name="polly-Type-Voice-StatusReason"></a>
Additional information about the status of a custom voice. When the status is `failed`, this field describes why Amazon Polly couldn't create the voice.
Type: String
Required: No

 ** SupportedEngines **   <a name="polly-Type-Voice-SupportedEngines"></a>
Specifies which engines (`standard`, `neural`, `long-form` or `generative`) are supported by a given voice.
Type: Array of strings
Valid Values: `standard | neural | long-form | generative`
Required: No

 ** VoiceCreationData **   <a name="polly-Type-Voice-VoiceCreationData"></a>
The data from which you created the custom voice. `CreateVoice` and `GetVoice` return this field. The response doesn't include the audio: a recording that Amazon Polly read from Amazon S3 includes its `S3Url`, and a recording that you passed as `Bytes` has no fields in `Data`.
Type: [VoiceCreationData](API_VoiceCreationData.md) object
Required: No

## See Also
<a name="API_Voice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/Voice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/Voice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/Voice)
