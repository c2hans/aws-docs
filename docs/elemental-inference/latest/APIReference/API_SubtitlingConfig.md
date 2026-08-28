---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_SubtitlingConfig.html
---

# SubtitlingConfig
<a name="API_SubtitlingConfig"></a>

A type of OutputConfig, used when the output in a feed is for the smart subtitling feature. smart subtitling uses automatic speech recognition (ASR) to generate live TTML subtitles from the audio in your source media.

## Contents
<a name="API_SubtitlingConfig_Contents"></a>

 ** language **   <a name="elementalinference-Type-SubtitlingConfig-language"></a>
The language of the audio in the source media. Elemental Inference uses this setting to optimize transcription accuracy. Specify the language using an ISO 639-2/T three-letter code, optionally with a region subtag. Supported values: eng, eng-au, eng-gb, eng-us, fra, ita, deu, spa, por.
Type: String
Valid Values: `eng | eng-au | eng-gb | eng-us | fra | ita | deu | spa | por`
Required: Yes

 ** aspectRatio **   <a name="elementalinference-Type-SubtitlingConfig-aspectRatio"></a>
The aspect ratio of the output video, specified as width and height integer values. Elemental Inference uses the aspect ratio to determine subtitle layout and line lengths.
Type: [AspectRatio](API_AspectRatio.md) object
Required: No

 ** dictionary **   <a name="elementalinference-Type-SubtitlingConfig-dictionary"></a>
The ID of a custom dictionary to improve transcription accuracy for domain-specific terminology. Use the CreateDictionary operation to create a dictionary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** profanityFilter **   <a name="elementalinference-Type-SubtitlingConfig-profanityFilter"></a>
Controls how profanity is handled in the generated subtitles. Valid values: DISABLED (no filtering, default), CENSOR (replace profanity with asterisks), DROP (remove profanity from the transcript).
Type: String
Valid Values: `DISABLED | CENSOR | DROP`
Required: No

## See Also
<a name="API_SubtitlingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/SubtitlingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/SubtitlingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/SubtitlingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
