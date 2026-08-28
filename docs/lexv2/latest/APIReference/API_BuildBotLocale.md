---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BuildBotLocale.html
---

# BuildBotLocale
<a name="API_BuildBotLocale"></a>

Builds a bot, its intents, and its slot types into a specific locale. A bot can be built into multiple locales. At runtime the locale is used to choose a specific build of the bot.

## Request Syntax
<a name="API_BuildBotLocale_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_BuildBotLocale_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_BuildBotLocale_RequestSyntax) **   <a name="lexv2-BuildBotLocale-request-uri-botId"></a>
The identifier of the bot to build. The identifier is returned in the response from the [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) operation.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_BuildBotLocale_RequestSyntax) **   <a name="lexv2-BuildBotLocale-request-uri-botVersion"></a>
The version of the bot to build. This can only be the draft version of the bot.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_BuildBotLocale_RequestSyntax) **   <a name="lexv2-BuildBotLocale-request-uri-localeId"></a>
The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_BuildBotLocale_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BuildBotLocale_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botLocaleStatus": "string",
   "botVersion": "string",
   "lastBuildSubmittedDateTime": number,
   "localeId": "string"
}
```

## Response Elements
<a name="API_BuildBotLocale_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_BuildBotLocale_ResponseSyntax) **   <a name="lexv2-BuildBotLocale-response-botId"></a>
The identifier of the specified bot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botLocaleStatus](#API_BuildBotLocale_ResponseSyntax) **   <a name="lexv2-BuildBotLocale-response-botLocaleStatus"></a>
The bot's build status. When the status is `ReadyExpressTesting` you can test the bot using the utterances defined for the intents and slot types. When the status is `Built`, the bot is ready for use and can be tested using any utterance.
Type: String
Valid Values: `Creating | Building | Built | ReadyExpressTesting | Failed | Deleting | NotBuilt | Importing | Processing`

 ** [botVersion](#API_BuildBotLocale_ResponseSyntax) **   <a name="lexv2-BuildBotLocale-response-botVersion"></a>
The version of the bot that was built. This is only the draft version of the bot.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [lastBuildSubmittedDateTime](#API_BuildBotLocale_ResponseSyntax) **   <a name="lexv2-BuildBotLocale-response-lastBuildSubmittedDateTime"></a>
A timestamp indicating the date and time that the bot was last built for this locale.
Type: Timestamp

 ** [localeId](#API_BuildBotLocale_ResponseSyntax) **   <a name="lexv2-BuildBotLocale-response-localeId"></a>
The language and locale specified of where the bot can be used.
Type: String

## Errors
<a name="API_BuildBotLocale_Errors"></a>

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
<a name="API_BuildBotLocale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/BuildBotLocale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BuildBotLocale)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
