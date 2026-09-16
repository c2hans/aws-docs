---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BatchUpdateCustomVocabularyItem.html
---

# BatchUpdateCustomVocabularyItem
<a name="API_BatchUpdateCustomVocabularyItem"></a>

Update a batch of custom vocabulary items for a given bot locale's custom vocabulary.

## Request Syntax
<a name="API_BatchUpdateCustomVocabularyItem_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/customvocabulary/DEFAULT/batchupdate HTTP/1.1
Content-type: application/json

{
   "customVocabularyItemList": [
      {
         "displayAs": "{{string}}",
         "itemId": "{{string}}",
         "phrase": "{{string}}",
         "weight": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateCustomVocabularyItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_BatchUpdateCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-request-uri-botId"></a>
The identifier of the bot associated with this custom vocabulary
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_BatchUpdateCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-request-uri-botVersion"></a>
The identifier of the version of the bot associated with this custom vocabulary.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_BatchUpdateCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-request-uri-localeId"></a>
The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see [ Supported Languages ](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_BatchUpdateCustomVocabularyItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [customVocabularyItemList](#API_BatchUpdateCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-request-customVocabularyItemList"></a>
A list of custom vocabulary items with updated fields. Each entry must contain a phrase and can optionally contain a displayAs and/or a weight.
Type: Array of [CustomVocabularyItem](API_CustomVocabularyItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateCustomVocabularyItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "itemId": "string"
      }
   ],
   "localeId": "string",
   "resources": [
      {
         "displayAs": "string",
         "itemId": "string",
         "phrase": "string",
         "weight": number
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateCustomVocabularyItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_BatchUpdateCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-response-botId"></a>
The identifier of the bot associated with this custom vocabulary.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_BatchUpdateCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-response-botVersion"></a>
The identifier of the version of the bot associated with this custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [errors](#API_BatchUpdateCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-response-errors"></a>
A list of custom vocabulary items that failed to update during the operation. The reason for the error is contained within each error object.
Type: Array of [FailedCustomVocabularyItem](API_FailedCustomVocabularyItem.md) objects

 ** [localeId](#API_BatchUpdateCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-response-localeId"></a>
The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see [ Supported Languages ](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Type: String

 ** [resources](#API_BatchUpdateCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchUpdateCustomVocabularyItem-response-resources"></a>
A list of custom vocabulary items that were successfully updated during the operation.
Type: Array of [CustomVocabularyItem](API_CustomVocabularyItem.md) objects

## Errors
<a name="API_BatchUpdateCustomVocabularyItem_Errors"></a>

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
<a name="API_BatchUpdateCustomVocabularyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BatchUpdateCustomVocabularyItem)
