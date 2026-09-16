---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateDocument.html
---

# TranslateDocument
<a name="API_TranslateDocument"></a>

Translates the input document from the source language to the target language. This synchronous operation supports text, HTML, or Word documents as the input document. `TranslateDocument` supports translations from English to any supported language, and from any supported language to English. Therefore, specify either the source language code or the target language code as “en” (English).

 If you set the `Formality` parameter, the request will fail if the target language does not support formality. For a list of target languages that support formality, see [Setting formality](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html) in the Amazon Translate Developer Guide.

## Request Syntax
<a name="API_TranslateDocument_RequestSyntax"></a>

```
{
   "Document": {
      "Content": {{blob}},
      "ContentType": "{{string}}"
   },
   "Settings": {
      "Brevity": "{{string}}",
      "Formality": "{{string}}",
      "Profanity": "{{string}}"
   },
   "SourceLanguageCode": "{{string}}",
   "TargetLanguageCode": "{{string}}",
   "TerminologyNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_TranslateDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Document](#API_TranslateDocument_RequestSyntax) **   <a name="translate-TranslateDocument-request-Document"></a>
The content and content type for the document to be translated. The document size must not exceed 100 KB.
Type: [Document](API_Document.md) object
Required: Yes

 ** [Settings](#API_TranslateDocument_RequestSyntax) **   <a name="translate-TranslateDocument-request-Settings"></a>
Settings to configure your translation output. You can configure the following options:
+ Brevity: not supported.
+ Formality: sets the formality level of the output text.
+ Profanity: masks profane words and phrases in your translation output.
Type: [TranslationSettings](API_TranslationSettings.md) object
Required: No

 ** [SourceLanguageCode](#API_TranslateDocument_RequestSyntax) **   <a name="translate-TranslateDocument-request-SourceLanguageCode"></a>
The language code for the language of the source text. For a list of supported language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) in the Amazon Translate Developer Guide.
To have Amazon Translate determine the source language of your text, you can specify `auto` in the `SourceLanguageCode` field. If you specify `auto`, Amazon Translate will call [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html) to determine the source language.
If you specify `auto`, you must send the `TranslateDocument` request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: Yes

 ** [TargetLanguageCode](#API_TranslateDocument_RequestSyntax) **   <a name="translate-TranslateDocument-request-TargetLanguageCode"></a>
The language code requested for the translated document. For a list of supported language codes, see [Supported languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: Yes

 ** [TerminologyNames](#API_TranslateDocument_RequestSyntax) **   <a name="translate-TranslateDocument-request-TerminologyNames"></a>
The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.
Use the [ListTerminologies](API_ListTerminologies.md) operation to get the available terminology lists.
For more information about custom terminology lists, see [Custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) in the Amazon Translate Developer Guide.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([A-Za-z0-9-]_?)+$`
Required: No

## Response Syntax
<a name="API_TranslateDocument_ResponseSyntax"></a>

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
   "TranslatedDocument": {
      "Content": blob
   }
}
```

## Response Elements
<a name="API_TranslateDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppliedSettings](#API_TranslateDocument_ResponseSyntax) **   <a name="translate-TranslateDocument-response-AppliedSettings"></a>
Settings to configure your translation output. You can configure the following options:
+ Brevity: reduces the length of the translation output for most translations. Available for `TranslateText` only.
+ Formality: sets the formality level of the translation output.
+ Profanity: masks profane words and phrases in the translation output.
Type: [TranslationSettings](API_TranslationSettings.md) object

 ** [AppliedTerminologies](#API_TranslateDocument_ResponseSyntax) **   <a name="translate-TranslateDocument-response-AppliedTerminologies"></a>
The names of the custom terminologies applied to the input text by Amazon Translate to produce the translated text document.
Type: Array of [AppliedTerminology](API_AppliedTerminology.md) objects

 ** [SourceLanguageCode](#API_TranslateDocument_ResponseSyntax) **   <a name="translate-TranslateDocument-response-SourceLanguageCode"></a>
The language code of the source document.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.

 ** [TargetLanguageCode](#API_TranslateDocument_ResponseSyntax) **   <a name="translate-TranslateDocument-response-TargetLanguageCode"></a>
The language code of the translated document.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.

 ** [TranslatedDocument](#API_TranslateDocument_ResponseSyntax) **   <a name="translate-TranslateDocument-response-TranslatedDocument"></a>
The document containing the translated content. The document format matches the source document format.
Type: [TranslatedDocument](API_TranslatedDocument.md) object

## Errors
<a name="API_TranslateDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
 The request that you made is not valid. Check your request to determine why it's not valid and then retry the request.
HTTP Status Code: 400

 ** LimitExceededException **
The specified limit has been exceeded. Review your request and retry it with a quantity below the stated limit.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource you are looking for has not been found. Review the resource you're looking for and see if a different resource will accomplish your needs before retrying the revised request.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The Amazon Translate service is temporarily unavailable. Wait a bit and then retry your request.
HTTP Status Code: 500

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
<a name="API_TranslateDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/translate-2017-07-01/TranslateDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/TranslateDocument)
