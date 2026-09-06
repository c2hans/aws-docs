---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html
---

# TranslateText
<a name="API_TranslateText"></a>

Translates input text from the source language to the target language. For a list of available languages and language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.

## Request Syntax
<a name="API_TranslateText_RequestSyntax"></a>

```
{
   "Settings": {
      "Brevity": "{{string}}",
      "Formality": "{{string}}",
      "Profanity": "{{string}}"
   },
   "SourceLanguageCode": "{{string}}",
   "TargetLanguageCode": "{{string}}",
   "TerminologyNames": [ "{{string}}" ],
   "Text": "{{string}}"
}
```

## Request Parameters
<a name="API_TranslateText_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Settings](#API_TranslateText_RequestSyntax) **   <a name="translate-TranslateText-request-Settings"></a>
Settings to configure your translation output. You can configure the following options:
+ Brevity: reduces the length of the translated output for most translations.
+ Formality: sets the formality level of the output text.
+ Profanity: masks profane words and phrases in your translation output.
Type: [TranslationSettings](API_TranslationSettings.md) object
Required: No

 ** [SourceLanguageCode](#API_TranslateText_RequestSyntax) **   <a name="translate-TranslateText-request-SourceLanguageCode"></a>
The language code for the language of the source text. For a list of language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
To have Amazon Translate determine the source language of your text, you can specify `auto` in the `SourceLanguageCode` field. If you specify `auto`, Amazon Translate will call [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html) to determine the source language.
If you specify `auto`, you must send the `TranslateText` request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: Yes

 ** [TargetLanguageCode](#API_TranslateText_RequestSyntax) **   <a name="translate-TranslateText-request-TargetLanguageCode"></a>
The language code requested for the language of the target text. For a list of language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: Yes

 ** [TerminologyNames](#API_TranslateText_RequestSyntax) **   <a name="translate-TranslateText-request-TerminologyNames"></a>
The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.
Use the [ListTerminologies](API_ListTerminologies.md) operation to get the available terminology lists.
For more information about custom terminology lists, see [Custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) in the Amazon Translate Developer Guide.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

 ** [Text](#API_TranslateText_RequestSyntax) **   <a name="translate-TranslateText-request-Text"></a>
The text to translate. The text string can be a maximum of 10,000 bytes long. Depending on your character set, this may be fewer than 10,000 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[\P{M}\p{M}]{1,10000}`
Required: Yes

## Response Syntax
<a name="API_TranslateText_ResponseSyntax"></a>

```
{
   "AppliedSettings": {
      "Brevity": "string",
      "Formality": "string",
      "Profanity": "string"
   },
   "AppliedTerminologies": [
      {
         "Name": "string",
         "Terms": [
            {
               "SourceText": "string",
               "TargetText": "string"
            }
         ]
      }
   ],
   "SourceLanguageCode": "string",
   "TargetLanguageCode": "string",
   "TranslatedText": "string"
}
```

## Response Elements
<a name="API_TranslateText_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppliedSettings](#API_TranslateText_ResponseSyntax) **   <a name="translate-TranslateText-response-AppliedSettings"></a>
Optional settings that modify the translation output.
Type: [TranslationSettings](API_TranslationSettings.md) object

 ** [AppliedTerminologies](#API_TranslateText_ResponseSyntax) **   <a name="translate-TranslateText-response-AppliedTerminologies"></a>
The names of the custom terminologies applied to the input text by Amazon Translate for the translated text response.
Type: Array of [AppliedTerminology](API_AppliedTerminology.md) objects

 ** [SourceLanguageCode](#API_TranslateText_ResponseSyntax) **   <a name="translate-TranslateText-response-SourceLanguageCode"></a>
The language code for the language of the source text.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.

 ** [TargetLanguageCode](#API_TranslateText_ResponseSyntax) **   <a name="translate-TranslateText-response-TargetLanguageCode"></a>
The language code for the language of the target text.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.

 ** [TranslatedText](#API_TranslateText_ResponseSyntax) **   <a name="translate-TranslateText-response-TranslatedText"></a>
The translated text.
Type: String
Length Constraints: Maximum length of 20000.
Pattern: `[\P{M}\p{M}]{0,20000}`

## Errors
<a name="API_TranslateText_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DetectedLanguageLowConfidenceException **
The confidence that Amazon Comprehend accurately detected the source language is low. If a low confidence level is acceptable for your application, you can use the language in the exception to call Amazon Translate again. For more information, see the [DetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectDominantLanguage.html) operation in the *Amazon Comprehend Developer Guide*.
 ** DetectedLanguageCode **
The language code of the auto-detected language from Amazon Comprehend.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
 The request that you made is not valid. Check your request to determine why it's not valid and then retry the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource you are looking for has not been found. Review the resource you're looking for and see if a different resource will accomplish your needs before retrying the revised request.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The Amazon Translate service is temporarily unavailable. Wait a bit and then retry your request.
HTTP Status Code: 500

 ** TextSizeLimitExceededException **
 The size of the text you submitted exceeds the size limit. Reduce the size of the text or use a smaller document and then retry your request.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again.
HTTP Status Code: 400

 ** UnsupportedLanguagePairException **
Amazon Translate does not support translation from the language of the source text into the requested target language. For more information, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
 ** SourceLanguageCode **
The language code for the language of the input text.
 ** TargetLanguageCode **
The language code for the language of the translated text.
HTTP Status Code: 400

## See Also
<a name="API_TranslateText_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/translate-2017-07-01/TranslateText)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/translate-2017-07-01/TranslateText)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/TranslateText)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/translate-2017-07-01/TranslateText)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/TranslateText)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/translate-2017-07-01/TranslateText)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/translate-2017-07-01/TranslateText)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/translate-2017-07-01/TranslateText)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/translate-2017-07-01/TranslateText)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/TranslateText)
