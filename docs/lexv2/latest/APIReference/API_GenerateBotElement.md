---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GenerateBotElement.html
---

# GenerateBotElement
<a name="API_GenerateBotElement"></a>

Generates sample utterances for an intent.

## Request Syntax
<a name="API_GenerateBotElement_RequestSyntax"></a>

```
POST /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/generate HTTP/1.1
Content-type: application/json

{
   "intentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GenerateBotElement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_GenerateBotElement_RequestSyntax) **   <a name="lexv2-GenerateBotElement-request-uri-botId"></a>
The bot unique Id for the bot request to generate utterances.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_GenerateBotElement_RequestSyntax) **   <a name="lexv2-GenerateBotElement-request-uri-botVersion"></a>
The bot version for the bot request to generate utterances.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [localeId](#API_GenerateBotElement_RequestSyntax) **   <a name="lexv2-GenerateBotElement-request-uri-localeId"></a>
The unique locale Id for the bot request to generate utterances.
Required: Yes

## Request Body
<a name="API_GenerateBotElement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [intentId](#API_GenerateBotElement_RequestSyntax) **   <a name="lexv2-GenerateBotElement-request-intentId"></a>
The intent unique Id for the bot request to generate utterances.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Response Syntax
<a name="API_GenerateBotElement_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "intentId": "string",
   "localeId": "string",
   "sampleUtterances": [
      {
         "utterance": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GenerateBotElement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_GenerateBotElement_ResponseSyntax) **   <a name="lexv2-GenerateBotElement-response-botId"></a>
The unique bot Id for the bot which received the response.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_GenerateBotElement_ResponseSyntax) **   <a name="lexv2-GenerateBotElement-response-botVersion"></a>
The unique bot version for the bot which received the response.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [intentId](#API_GenerateBotElement_ResponseSyntax) **   <a name="lexv2-GenerateBotElement-response-intentId"></a>
The unique intent Id for the bot which received the response.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [localeId](#API_GenerateBotElement_ResponseSyntax) **   <a name="lexv2-GenerateBotElement-response-localeId"></a>
The unique locale Id for the bot which received the response.
Type: String

 ** [sampleUtterances](#API_GenerateBotElement_ResponseSyntax) **   <a name="lexv2-GenerateBotElement-response-sampleUtterances"></a>
The sample utterances for the bot which received the response.
Type: Array of [SampleUtterance](API_SampleUtterance.md) objects

## Errors
<a name="API_GenerateBotElement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

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

## Examples
<a name="API_GenerateBotElement_Examples"></a>

### Example request
<a name="API_GenerateBotElement_Example_1"></a>

This example illustrates one usage of GenerateBotElement.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/BOT1234567/botversions/DRAFT/botlocales/en_US/generate

Payload:
{
   "intentId":"INTENT1234"
}
```

### Example response
<a name="API_GenerateBotElement_Example_2"></a>

This example illustrates one usage of GenerateBotElement.

```
{
    "botId": "BOT1234567",
    "botVersion": "DRAFT",
    "intentId": "INTENT1234",
    "localeId": "en_US",
    "sampleUtterances": [{
        "utterance": "I need to cancel my order {OrderId} due to {CancellationReason}"
    }, {
        "utterance": "Please cancel order {OrderId} as {CancellationReason}"
    }, {
        "utterance": "{OrderId} requires cancellation because of {CancellationReason}"
    }, {
        "utterance": "Cancel order {OrderId} . {CancellationReason}"
    }, {
        "utterance": "I have to cancel my order {OrderId} . The reason is {CancellationReason}"
    }]
}
```

## See Also
<a name="API_GenerateBotElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/GenerateBotElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/GenerateBotElement)
