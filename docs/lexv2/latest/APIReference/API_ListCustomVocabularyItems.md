---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListCustomVocabularyItems.html
---

# ListCustomVocabularyItems
<a name="API_ListCustomVocabularyItems"></a>

Paginated list of custom vocabulary items for a given bot locale's custom vocabulary.

## Request Syntax
<a name="API_ListCustomVocabularyItems_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/customvocabulary/DEFAULT/list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCustomVocabularyItems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListCustomVocabularyItems_RequestSyntax) **   <a name="lexv2-ListCustomVocabularyItems-request-uri-botId"></a>
The identifier of the version of the bot associated with this custom vocabulary.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_ListCustomVocabularyItems_RequestSyntax) **   <a name="lexv2-ListCustomVocabularyItems-request-uri-botVersion"></a>
The bot version of the bot to the list custom vocabulary request.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_ListCustomVocabularyItems_RequestSyntax) **   <a name="lexv2-ListCustomVocabularyItems-request-uri-localeId"></a>
The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_ListCustomVocabularyItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListCustomVocabularyItems_RequestSyntax) **   <a name="lexv2-ListCustomVocabularyItems-request-maxResults"></a>
The maximum number of items returned by the list operation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListCustomVocabularyItems_RequestSyntax) **   <a name="lexv2-ListCustomVocabularyItems-request-nextToken"></a>
The nextToken identifier to the list custom vocabulary request.
Type: String
Required: No

## Response Syntax
<a name="API_ListCustomVocabularyItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "customVocabularyItems": [
      {
         "displayAs": "string",
         "itemId": "string",
         "phrase": "string",
         "weight": number
      }
   ],
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomVocabularyItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListCustomVocabularyItems_ResponseSyntax) **   <a name="lexv2-ListCustomVocabularyItems-response-botId"></a>
The identifier of the bot associated with this custom vocabulary.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_ListCustomVocabularyItems_ResponseSyntax) **   <a name="lexv2-ListCustomVocabularyItems-response-botVersion"></a>
The identifier of the version of the bot associated with this custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [customVocabularyItems](#API_ListCustomVocabularyItems_ResponseSyntax) **   <a name="lexv2-ListCustomVocabularyItems-response-customVocabularyItems"></a>
The custom vocabulary items from the list custom vocabulary response.
Type: Array of [CustomVocabularyItem](API_CustomVocabularyItem.md) objects

 ** [localeId](#API_ListCustomVocabularyItems_ResponseSyntax) **   <a name="lexv2-ListCustomVocabularyItems-response-localeId"></a>
The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see [ Supported Languages ](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Type: String

 ** [nextToken](#API_ListCustomVocabularyItems_ResponseSyntax) **   <a name="lexv2-ListCustomVocabularyItems-response-nextToken"></a>
The nextToken identifier to the list custom vocabulary response.
Type: String

## Errors
<a name="API_ListCustomVocabularyItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListCustomVocabularyItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListCustomVocabularyItems)
