---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotLocale.html
---

# DeleteBotLocale
<a name="API_DeleteBotLocale"></a>

Removes a locale from a bot.

When you delete a locale, all intents, slots, and slot types defined for the locale are also deleted.

## Request Syntax
<a name="API_DeleteBotLocale_RequestSyntax"></a>

```
DELETE /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBotLocale_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DeleteBotLocale_RequestSyntax) **   <a name="lexv2-DeleteBotLocale-request-uri-botId"></a>
The unique identifier of the bot that contains the locale.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DeleteBotLocale_RequestSyntax) **   <a name="lexv2-DeleteBotLocale-request-uri-botVersion"></a>
The version of the bot that contains the locale.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_DeleteBotLocale_RequestSyntax) **   <a name="lexv2-DeleteBotLocale-request-uri-localeId"></a>
The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_DeleteBotLocale_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBotLocale_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botLocaleStatus": "string",
   "botVersion": "string",
   "localeId": "string"
}
```

## Response Elements
<a name="API_DeleteBotLocale_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DeleteBotLocale_ResponseSyntax) **   <a name="lexv2-DeleteBotLocale-response-botId"></a>
The identifier of the bot that contained the deleted locale.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botLocaleStatus](#API_DeleteBotLocale_ResponseSyntax) **   <a name="lexv2-DeleteBotLocale-response-botLocaleStatus"></a>
The status of deleting the bot locale. The locale first enters the `Deleting` status. Once the locale is deleted it no longer appears in the list of locales for the bot.
Type: String
Valid Values: `Creating | Building | Built | ReadyExpressTesting | Failed | Deleting | NotBuilt | Importing | Processing`

 ** [botVersion](#API_DeleteBotLocale_ResponseSyntax) **   <a name="lexv2-DeleteBotLocale-response-botVersion"></a>
The version of the bot that contained the deleted locale.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [localeId](#API_DeleteBotLocale_ResponseSyntax) **   <a name="lexv2-DeleteBotLocale-response-localeId"></a>
The language and locale of the deleted locale.
Type: String

## Errors
<a name="API_DeleteBotLocale_Errors"></a>

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
<a name="API_DeleteBotLocale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DeleteBotLocale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DeleteBotLocale)
