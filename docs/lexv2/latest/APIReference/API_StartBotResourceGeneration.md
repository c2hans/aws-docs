---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotResourceGeneration.html
---

# StartBotResourceGeneration
<a name="API_StartBotResourceGeneration"></a>

Starts a request for the descriptive bot builder to generate a bot locale configuration based on the prompt you provide it. After you make this call, use the `DescribeBotResourceGeneration` operation to check on the status of the generation and for the `generatedBotLocaleUrl` when the generation is complete. Use that value to retrieve the Amazon S3 object containing the bot locale configuration. You can then modify and import this configuration.

## Request Syntax
<a name="API_StartBotResourceGeneration_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/startgeneration HTTP/1.1
Content-type: application/json

{
   "generationInputPrompt": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartBotResourceGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_StartBotResourceGeneration_RequestSyntax) **   <a name="lexv2-StartBotResourceGeneration-request-uri-botId"></a>
The unique identifier of the bot for which to generate intents and slot types.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_StartBotResourceGeneration_RequestSyntax) **   <a name="lexv2-StartBotResourceGeneration-request-uri-botVersion"></a>
The version of the bot for which to generate intents and slot types.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_StartBotResourceGeneration_RequestSyntax) **   <a name="lexv2-StartBotResourceGeneration-request-uri-localeId"></a>
The locale of the bot for which to generate intents and slot types.
Required: Yes

## Request Body
<a name="API_StartBotResourceGeneration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [generationInputPrompt](#API_StartBotResourceGeneration_RequestSyntax) **   <a name="lexv2-StartBotResourceGeneration-request-generationInputPrompt"></a>
The prompt to generate intents and slot types for the bot locale. Your description should be both *detailed* and *precise* to help generate appropriate and sufficient intents for your bot. Include a list of actions to improve the intent creation process.
Type: String
Length Constraints: Minimum length of 100. Maximum length of 2000.
Required: Yes

## Response Syntax
<a name="API_StartBotResourceGeneration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "generationId": "string",
   "generationInputPrompt": "string",
   "generationStatus": "string",
   "localeId": "string"
}
```

## Response Elements
<a name="API_StartBotResourceGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-botId"></a>
The unique identifier of the bot for which the generation request was made.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-botVersion"></a>
The version of the bot for which the generation request was made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [creationDateTime](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-creationDateTime"></a>
The date and time at which the generation request was made.
Type: Timestamp

 ** [generationId](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-generationId"></a>
The unique identifier of the generation request.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [generationInputPrompt](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-generationInputPrompt"></a>
The prompt that was used generate intents and slot types for the bot locale.
Type: String
Length Constraints: Minimum length of 100. Maximum length of 2000.

 ** [generationStatus](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-generationStatus"></a>
The status of the generation request.
Type: String
Valid Values: `Failed | Complete | InProgress`

 ** [localeId](#API_StartBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-StartBotResourceGeneration-response-localeId"></a>
The locale of the bot for which the generation request was made.
Type: String

## Errors
<a name="API_StartBotResourceGeneration_Errors"></a>

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

## Examples
<a name="API_StartBotResourceGeneration_Examples"></a>

### Example request
<a name="API_StartBotResourceGeneration_Example_1"></a>

This example illustrates one usage of StartBotResourceGeneration.

```
PUT https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/botversions/DRAFT/botlocales/en_GB/startgeneration

Payload:
{
    "generationInputPrompt": "We want a bot to help customers order food (using item id, quantity, size), check order status, and cancel an order. Use Order ID for indexing order."
}
```

### Example response
<a name="API_StartBotResourceGeneration_Example_2"></a>

This example illustrates one usage of StartBotResourceGeneration.

```
{
    "botId": "BOT1234567",
    "botVersion": "DRAFT",
    "creationDateTime": 1.699570064977E9,
    "generationId": "GEN1234567",
    "generationInputPrompt": null,
    "generationStatus": "InProgress",
    "localeId": "en_GB"
}
```

## See Also
<a name="API_StartBotResourceGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StartBotResourceGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StartBotResourceGeneration)
