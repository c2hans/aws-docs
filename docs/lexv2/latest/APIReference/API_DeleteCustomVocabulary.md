---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteCustomVocabulary.html
---

# DeleteCustomVocabulary
<a name="API_DeleteCustomVocabulary"></a>

Removes a custom vocabulary from the specified locale in the specified bot.

## Request Syntax
<a name="API_DeleteCustomVocabulary_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/customvocabulary HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCustomVocabulary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DeleteCustomVocabulary_RequestSyntax) **   <a name="lexv2-DeleteCustomVocabulary-request-uri-botId"></a>
The unique identifier of the bot to remove the custom vocabulary from.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DeleteCustomVocabulary_RequestSyntax) **   <a name="lexv2-DeleteCustomVocabulary-request-uri-botVersion"></a>
The version of the bot to remove the custom vocabulary from.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_DeleteCustomVocabulary_RequestSyntax) **   <a name="lexv2-DeleteCustomVocabulary-request-uri-localeId"></a>
The locale identifier for the locale that contains the custom vocabulary to remove.
Required: Yes

## Request Body
<a name="API_DeleteCustomVocabulary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCustomVocabulary_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "customVocabularyStatus": "string",
   "localeId": "string"
}
```

## Response Elements
<a name="API_DeleteCustomVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DeleteCustomVocabulary_ResponseSyntax) **   <a name="lexv2-DeleteCustomVocabulary-response-botId"></a>
The identifier of the bot that the custom vocabulary was removed from.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DeleteCustomVocabulary_ResponseSyntax) **   <a name="lexv2-DeleteCustomVocabulary-response-botVersion"></a>
The version of the bot that the custom vocabulary was removed from.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [customVocabularyStatus](#API_DeleteCustomVocabulary_ResponseSyntax) **   <a name="lexv2-DeleteCustomVocabulary-response-customVocabularyStatus"></a>
The status of removing the custom vocabulary.
Type: String
Valid Values: `Ready | Deleting | Exporting | Importing | Creating`

 ** [localeId](#API_DeleteCustomVocabulary_ResponseSyntax) **   <a name="lexv2-DeleteCustomVocabulary-response-localeId"></a>
The locale identifier for the locale that the custom vocabulary was removed from.
Type: String

## Errors
<a name="API_DeleteCustomVocabulary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

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
<a name="API_DeleteCustomVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteCustomVocabulary)
