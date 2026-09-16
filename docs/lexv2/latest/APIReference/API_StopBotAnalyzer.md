---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StopBotAnalyzer.html
---

# StopBotAnalyzer
<a name="API_StopBotAnalyzer"></a>

Cancels an ongoing bot analysis execution. Once stopped, the analysis cannot be resumed and no recommendations will be generated.

## Request Syntax
<a name="API_StopBotAnalyzer_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botanalyzer/{{botAnalyzerRequestId}}/stop/ HTTP/1.1
```

## URI Request Parameters
<a name="API_StopBotAnalyzer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botAnalyzerRequestId](#API_StopBotAnalyzer_RequestSyntax) **   <a name="lexv2-StopBotAnalyzer-request-uri-botAnalyzerRequestId"></a>
The unique identifier of the analysis request to stop.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [botId](#API_StopBotAnalyzer_RequestSyntax) **   <a name="lexv2-StopBotAnalyzer-request-uri-botId"></a>
The unique identifier of the bot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_StopBotAnalyzer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopBotAnalyzer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botAnalyzerRequestId": "string",
   "botAnalyzerStatus": "string",
   "botId": "string",
   "botVersion": "string",
   "localeId": "string"
}
```

## Response Elements
<a name="API_StopBotAnalyzer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botAnalyzerRequestId](#API_StopBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StopBotAnalyzer-response-botAnalyzerRequestId"></a>
The unique identifier of the analysis request.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [botAnalyzerStatus](#API_StopBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StopBotAnalyzer-response-botAnalyzerStatus"></a>
The updated status of the analysis. The status will be `Stopping` and will eventually transition to `Stopped`.
Valid Values: `Processing | Available | Failed | Stopping | Stopped`
Type: String
Valid Values: `Processing | Available | Failed | Stopping | Stopped`

 ** [botId](#API_StopBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StopBotAnalyzer-response-botId"></a>
The unique identifier of the bot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_StopBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StopBotAnalyzer-response-botVersion"></a>
The version of the bot.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [localeId](#API_StopBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StopBotAnalyzer-response-localeId"></a>
The locale identifier of the bot locale.
Type: String

## Errors
<a name="API_StopBotAnalyzer_Errors"></a>

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
<a name="API_StopBotAnalyzer_Examples"></a>

### Example request
<a name="API_StopBotAnalyzer_Example_1"></a>

This example illustrates one usage of StopBotAnalyzer.

```
PUT https://models-v2-lex.us-east-1.amazonaws.com/bots/<BotId>/botanalyzer/<RequestId>/stop/
```

### Example response
<a name="API_StopBotAnalyzer_Example_2"></a>

This example illustrates one usage of StopBotAnalyzer.

```
{
    "botId": "<BotId>",
    "botVersion": "DRAFT",
    "localeId": "en_US",
    "botAnalyzerStatus": "Stopping",
    "botAnalyzerRequestId": "<RequestId>"
}
```

## See Also
<a name="API_StopBotAnalyzer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StopBotAnalyzer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StopBotAnalyzer)
