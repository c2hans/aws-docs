---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_TranscribeAudio.html
---

# TranscribeAudio

Transcribes a media file and returns the transcript in the same response. There is no job to start and no status to poll.

Use `TranscribeAudio` when you already have a complete media file and want the transcript right away. For large files, long audio, or bulk processing, use [StartTranscriptionJob](API_StartTranscriptionJob.md).

You must include the following parameters in your `TranscribeAudio` request:
+  `Media`: Your audio, either as inline bytes (`MediaBytes`) or as the Amazon S3 location of a media file (`MediaFileUri`).
+ One of `Language` or `LanguageDetectionMode`: Specify the language of your audio, or have Amazon Transcribe identify it.

Your audio must be between 0.5 seconds and 1 hour long. Supported formats are WAV, MP3, FLAC, M4A, MP4, Ogg, WebM, and AMR.

If you send your audio in the request (`MediaBytes`), the file can be up to 25 MB. If you provide an Amazon S3 location (`MediaFileUri`), the file can be up to 500 MB.

Amazon Transcribe always turns on smart formatting, also known as inverse text normalization (ITN). It writes numbers, dates, currency, and similar items in their usual written form. For example, "one hundred" becomes "100". You can't turn smart formatting off.

By default, Amazon Transcribe returns the transcript in `TranscriptResponse`. If you include `OutputConfiguration`, Amazon Transcribe writes the transcript to the Amazon S3 location you specify instead, and the response contains only that location.

## Request Syntax
<a name="API_TranscribeAudio_RequestSyntax"></a>

```
{
   "ChannelIdentification": {{boolean}},
   "ContentRedaction": {
      "PiiEntityTypes": [ "{{string}}" ],
      "RedactionOutput": "{{string}}",
      "RedactionType": "{{string}}"
   },
   "Language": "{{string}}",
   "LanguageDetectionMode": "{{string}}",
   "LanguageOptions": [ "{{string}}" ],
   "MaxSpeakerLabels": {{number}},
   "Media": { ... },
   "OutputConfiguration": {
      "OutputMediaFileUri": "{{string}}"
   },
   "ShowSpeakerLabels": {{boolean}},
   "VocabularyFilterSettings": {
      "Filters": [
         {
            "Language": "{{string}}",
            "VocabularyFilterName": "{{string}}",
            "Words": [ "{{string}}" ]
         }
      ],
      "VocabularyFilterMethod": "{{string}}"
   },
   "VocabularySettings": [
      {
         "Language": "{{string}}",
         "Phrases": [
            {
               "DisplayAs": "{{string}}",
               "Text": "{{string}}"
            }
         ],
         "VocabularyName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TranscribeAudio_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChannelIdentification](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-ChannelIdentification"></a>
Enables channel identification in multi-channel audio. Each channel is transcribed independently, and each item in the transcript is labeled with its channel.
Channel identification supports up to two channels.
Type: Boolean
Required: No

 ** [ContentRedaction](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-ContentRedaction"></a>
Redacts personally identifiable information (PII) from your transcript. Amazon Transcribe returns the redacted transcript in `RedactedResults`.
If you set `RedactionOutput` to `redacted_and_unredacted`, Amazon Transcribe also returns the unredacted transcript in `Results`.
In Sync, content redaction has these limits:
+  **Languages:** English (`en`), Spanish (`es`), French (`fr`), Italian (`it`), German (`de`), and Portuguese (`pt`).
+  **Language identification:** If you use `LanguageDetectionMode`, you must also include `LanguageOptions`, and every language in it must be one of the languages above. A request that has no `LanguageOptions`, or that lists a language that isn't supported, returns a `BadRequestException`.
+  **Regions:** Content redaction isn't available in the South America (São Paulo) Region (`sa-east-1`). It's available in the other AWS Regions where Sync is available.
Type: [ContentRedaction](API_ContentRedaction.md) object
Required: No

 ** [Language](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-Language"></a>
The language spoken in your audio, as a base language code (for example, `en` or `es`).
Include either `Language` or `LanguageDetectionMode` in your request, but not both.
Type: String
Valid Values: `en | es | fr | it | de | ja | pt | ko | zh-CN | zh-TW | zh-HK`
Required: No

 ** [LanguageDetectionMode](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-LanguageDetectionMode"></a>
Enables automatic language identification. Use `IDENTIFY_LANGUAGE` if your audio contains a single language that you don't know in advance.
You can optionally include `LanguageOptions` to limit identification to languages you think may be present, which can improve accuracy.
Amazon Transcribe returns the identified language, as a locale (for example, `en-US`), in the response metadata.
Include either `Language` or `LanguageDetectionMode` in your request, but not both.
Type: String
Valid Values: `IDENTIFY_LANGUAGE`
Required: No

 ** [LanguageOptions](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-LanguageOptions"></a>
A list of two or more languages that you think may be present in your audio, as base language codes (for example, `en` and `es`). Each language can appear only once. A list with only one language returns a `BadRequestException`.
You can use `LanguageOptions` only with `LanguageDetectionMode`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `en | es | fr | it | de | ja | pt | ko | zh-CN | zh-TW | zh-HK`
Required: No

 ** [MaxSpeakerLabels](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-MaxSpeakerLabels"></a>
Specify the maximum number of speakers you want to partition in your media.
Note that if your media contains more speakers than the specified number, Amazon Transcribe treats multiple speakers as a single speaker.
You can set `MaxSpeakerLabels` only if `ShowSpeakerLabels` is `true`.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 30.
Required: No

 ** [Media](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-Media"></a>
The audio to transcribe. Specify exactly one of `MediaBytes` or `MediaFileUri`.
Audio sent in the request (`MediaBytes`) can be up to 25 MB. Audio in Amazon S3 (`MediaFileUri`) can be up to 500 MB.
Type: [SyncMedia](API_SyncMedia.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [OutputConfiguration](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-OutputConfiguration"></a>
Writes the transcript to an Amazon S3 location instead of returning it in the response. If you include `OutputConfiguration`, the response contains only the output location.
You must have write permission for the location you specify.
Type: [SyncOutputConfiguration](API_SyncOutputConfiguration.md) object
Required: No

 ** [ShowSpeakerLabels](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-ShowSpeakerLabels"></a>
Enables speaker partitioning (diarization) in your transcript. Speaker partitioning labels the speech from individual speakers in your media file.
If you set `ShowSpeakerLabels` to `true`, you must also include `MaxSpeakerLabels`.
For more information, see [Partitioning speakers (diarization)](https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html).
Type: Boolean
Required: No

 ** [VocabularyFilterSettings](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-VocabularyFilterSettings"></a>
Custom vocabulary filters to apply to your transcript, and how to apply them.
Type: [VocabularyFilterSettings](API_VocabularyFilterSettings.md) object
Required: No

 ** [VocabularySettings](#API_TranscribeAudio_RequestSyntax) **   <a name="transcribe-TranscribeAudio-request-VocabularySettings"></a>
Custom vocabularies to apply to your transcript, with one entry per language. In each entry, you can reference a custom vocabulary you created or provide phrases inline. All entries must use the same type, either all by name or all inline.
If you specify `Language`, include exactly one entry, and its `Language` must match. If you use `LanguageDetectionMode`, you can include one entry for each language in `LanguageOptions`.
Type: Array of [VocabularySettingsEntry](API_VocabularySettingsEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_TranscribeAudio_ResponseSyntax"></a>

```
{
   "OutputConfiguration": {
      "OutputMediaFileUri": "string"
   },
   "TranscriptResponse": {
      "Metadata": {
         "LanguageCode": "string",
         "LanguageCodes": [
            {
               "DurationInSeconds": number,
               "LanguageCode": "string"
            }
         ],
         "MediaFormat": "string",
         "MediaSampleRateHertz": number,
         "NumberOfChannels": number,
         "SpeakersCount": number
      },
      "RedactedResults": {
         "Items": [
            {
               "ChannelLabel": "string",
               "Content": "string",
               "EndTime": number,
               "Id": number,
               "LanguageCode": "string",
               "Redactions": [
                  {
                     "Type": "string"
                  }
               ],
               "SpeakerLabel": "string",
               "StartTime": number,
               "VocabularyFilterMatch": boolean
            }
         ],
         "Transcript": "string"
      },
      "Results": {
         "Items": [
            {
               "ChannelLabel": "string",
               "Content": "string",
               "EndTime": number,
               "Id": number,
               "LanguageCode": "string",
               "Redactions": [
                  {
                     "Type": "string"
                  }
               ],
               "SpeakerLabel": "string",
               "StartTime": number,
               "VocabularyFilterMatch": boolean
            }
         ],
         "Transcript": "string"
      }
   }
}
```

## Response Elements
<a name="API_TranscribeAudio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OutputConfiguration](#API_TranscribeAudio_ResponseSyntax) **   <a name="transcribe-TranscribeAudio-response-OutputConfiguration"></a>
The Amazon S3 location where your transcript was written. Present only if you included `OutputConfiguration` in your request. In that case, `TranscriptResponse` isn't returned.
Type: [SyncOutputConfiguration](API_SyncOutputConfiguration.md) object

 ** [TranscriptResponse](#API_TranscribeAudio_ResponseSyntax) **   <a name="transcribe-TranscribeAudio-response-TranscriptResponse"></a>
Your transcript and information about your audio. Present only if you didn't include `OutputConfiguration` in your request.
Type: [TranscriptResponse](API_TranscriptResponse.md) object

## Errors
<a name="API_TranscribeAudio_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
Your request didn't pass one or more validation tests. This can occur when a parameter has an invalid value, when you combine parameters in a way that isn't supported, when the entity you're trying to delete doesn't exist, or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.
 ** Reason **
A code that identifies why the audio in your request was rejected. Currently, `TranscribeAudio` returns this field, and only for problems with your audio. It isn't returned for other validation errors.
Possible values:
+  `audioTooLong`: The audio is longer than the maximum duration of 1 hour.
+  `audioTooShort`: The audio is shorter than 0.5 seconds.
+  `audioFileTooLarge`: The audio is larger than the maximum size.
+  `unsupportedAudioFormat`: The media format isn't supported.
+  `unsupportedChannelCount`: You enabled `ChannelIdentification` and the audio has more than two channels.
+  `invalidAudio`: Amazon Transcribe couldn't decode the audio.
+  `mediaDownloadFailed`: Amazon Transcribe couldn't download the audio at your `MediaFileUri`.
HTTP Status Code: 400

 ** InternalFailureException **
There was an internal error. Check the error message, correct the issue, and try your request again.
HTTP Status Code: 500

 ** LimitExceededException **
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_TranscribeAudio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/TranscribeAudio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/TranscribeAudio)
