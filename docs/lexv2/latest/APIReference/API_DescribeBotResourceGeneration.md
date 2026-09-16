---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotResourceGeneration.html
---

# DescribeBotResourceGeneration
<a name="API_DescribeBotResourceGeneration"></a>

Returns information about a request to generate a bot through natural language description, made through the `StartBotResource` API. Use the `generatedBotLocaleUrl` to retrieve the Amazon S3 object containing the bot locale configuration. You can then modify and import this configuration.

## Request Syntax
<a name="API_DescribeBotResourceGeneration_RequestSyntax"></a>

```
GET /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/generations/{{generationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBotResourceGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeBotResourceGeneration_RequestSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-request-uri-botId"></a>
The unique identifier of the bot for which to return the generation details.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DescribeBotResourceGeneration_RequestSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-request-uri-botVersion"></a>
The version of the bot for which to return the generation details.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [generationId](#API_DescribeBotResourceGeneration_RequestSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-request-uri-generationId"></a>
The unique identifier of the generation request for which to return the generation details.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [localeId](#API_DescribeBotResourceGeneration_RequestSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-request-uri-localeId"></a>
The locale of the bot for which to return the generation details.
Required: Yes

## Request Body
<a name="API_DescribeBotResourceGeneration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBotResourceGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "failureReasons": [ "string" ],
   "generatedBotLocaleUrl": "string",
   "generationId": "string",
   "generationInputPrompt": "string",
   "generationStatus": "string",
   "lastUpdatedDateTime": number,
   "localeId": "string",
   "modelArn": "string"
}
```

## Response Elements
<a name="API_DescribeBotResourceGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-botId"></a>
The unique identifier of the bot for which the generation request was made.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-botVersion"></a>
The version of the bot for which the generation request was made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [creationDateTime](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-creationDateTime"></a>
The date and time at which the item was generated.
Type: Timestamp

 ** [failureReasons](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-failureReasons"></a>
A list of reasons why the generation of bot resources through natural language description failed.
Type: Array of strings

 ** [generatedBotLocaleUrl](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-generatedBotLocaleUrl"></a>
The Amazon S3 location of the generated bot locale configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [generationId](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-generationId"></a>
The generation ID for which to return the generation details.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [generationInputPrompt](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-generationInputPrompt"></a>
The prompt used in the generation request.
Type: String
Length Constraints: Minimum length of 100. Maximum length of 2000.

 ** [generationStatus](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-generationStatus"></a>
The status of the generation request.
Type: String
Valid Values: `Failed | Complete | InProgress`

 ** [lastUpdatedDateTime](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-lastUpdatedDateTime"></a>
The date and time at which the generated item was updated.
Type: Timestamp

 ** [localeId](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-localeId"></a>
The locale of the bot for which the generation request was made.
Type: String

 ** [modelArn](#API_DescribeBotResourceGeneration_ResponseSyntax) **   <a name="lexv2-DescribeBotResourceGeneration-response-modelArn"></a>
The ARN of the model used to generate the bot resources.
Type: String
Pattern: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model\/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}$`

## Errors
<a name="API_DescribeBotResourceGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## Examples
<a name="API_DescribeBotResourceGeneration_Examples"></a>

### Example request
<a name="API_DescribeBotResourceGeneration_Example_1"></a>

This example illustrates one usage of DescribeBotResourceGeneration.

```
GET https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/botversions/DRAFT/botlocales/en_GB/generations/GEN1234567
```

### Example response
<a name="API_DescribeBotResourceGeneration_Example_2"></a>

This example illustrates one usage of DescribeBotResourceGeneration.

```
{
    "botId": "BOT1234567",
    "botVersion": "DRAFT",
    "creationDateTime": 1.699570064977E9,
    "failureReasons": null,
    "generatedBotLocaleUrl": "https://lex-botresourcegenerations-us-east-1-prod.s3.amazonaws.com/901559830335/BOT1234567/DRAFT/en_GB/GEN1234567/generated-LexJson-54481014-ef11-42a5-a3e6-eac6062044b9.zip",
    "generationId": "GEN1234567",
    "generationInputPrompt": "We want a bot to help customers order food (using item id, quantity, size), check order status, and cancel an order. Use Order ID for indexing order.",
    "generationStatus": "Complete",
    "lastUpdatedDateTime": 1.699570064977E9,
    "localeId": "en_GB",
    "modelArn ": null
}
```

## See Also
<a name="API_DescribeBotResourceGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeBotResourceGeneration)
