---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BatchDeleteCustomVocabularyItem.html
---

# BatchDeleteCustomVocabularyItem
<a name="API_BatchDeleteCustomVocabularyItem"></a>

Delete a batch of custom vocabulary items for a given bot locale's custom vocabulary.

## Request Syntax
<a name="API_BatchDeleteCustomVocabularyItem_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/customvocabulary/DEFAULT/batchdelete HTTP/1.1
Content-type: application/json

{
   "customVocabularyItemList": [
      {
         "itemId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteCustomVocabularyItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_BatchDeleteCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-request-uri-botId"></a>
The identifier of the bot associated with this custom vocabulary.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_BatchDeleteCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-request-uri-botVersion"></a>
The identifier of the version of the bot associated with this custom vocabulary.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_BatchDeleteCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-request-uri-localeId"></a>
The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see [ Supported Languages ](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_BatchDeleteCustomVocabularyItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [customVocabularyItemList](#API_BatchDeleteCustomVocabularyItem_RequestSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-request-customVocabularyItemList"></a>
A list of custom vocabulary items requested to be deleted. Each entry must contain the unique custom vocabulary entry identifier.
Type: Array of [CustomVocabularyEntryId](API_CustomVocabularyEntryId.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_BatchDeleteCustomVocabularyItem_ResponseSyntax"></a>

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
<a name="API_BatchDeleteCustomVocabularyItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_BatchDeleteCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-response-botId"></a>
The identifier of the bot associated with this custom vocabulary.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_BatchDeleteCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-response-botVersion"></a>
The identifier of the version of the bot associated with this custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [errors](#API_BatchDeleteCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-response-errors"></a>
A list of custom vocabulary items that failed to delete during the operation. The reason for the error is contained within each error object.
Type: Array of [FailedCustomVocabularyItem](API_FailedCustomVocabularyItem.md) objects

 ** [localeId](#API_BatchDeleteCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-response-localeId"></a>
The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Type: String

 ** [resources](#API_BatchDeleteCustomVocabularyItem_ResponseSyntax) **   <a name="lexv2-BatchDeleteCustomVocabularyItem-response-resources"></a>
A list of custom vocabulary items that were successfully deleted during the operation.
Type: Array of [CustomVocabularyItem](API_CustomVocabularyItem.md) objects

## Errors
<a name="API_BatchDeleteCustomVocabularyItem_Errors"></a>

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
<a name="API_BatchDeleteCustomVocabularyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BatchDeleteCustomVocabularyItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
