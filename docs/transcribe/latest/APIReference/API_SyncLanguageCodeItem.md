---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_SyncLanguageCodeItem.html
---

# SyncLanguageCodeItem

A language identified in your audio, and how long it's spoken.

## Contents
<a name="API_SyncLanguageCodeItem_Contents"></a>

 ** DurationInSeconds **   <a name="transcribe-Type-SyncLanguageCodeItem-DurationInSeconds"></a>
The total time, in seconds, the identified language is spoken in your audio.
Type: Float
Required: No

 ** LanguageCode **   <a name="transcribe-Type-SyncLanguageCodeItem-LanguageCode"></a>
The identified language, as a locale (for example, `en-US`).
Type: String
Valid Values: `en-US | en-AB | en-AU | en-GB | en-IE | en-IN | en-WL | en-ZA | en-NZ | es-US | es-ES | es-MX | fr-FR | fr-CA | it-IT | de-DE | de-CH | ja-JP | pt-BR | pt-PT | zh-CN | zh-TW | zh-HK | ko-KR`
Required: No

## See Also
<a name="API_SyncLanguageCodeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/SyncLanguageCodeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/SyncLanguageCodeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/SyncLanguageCodeItem)
