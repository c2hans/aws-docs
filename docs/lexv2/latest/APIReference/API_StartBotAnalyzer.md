---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotAnalyzer.html
---

# StartBotAnalyzer
<a name="API_StartBotAnalyzer"></a>

Initiates an asynchronous analysis of your bot configuration using AI-powered analysis to identify potential issues and recommend improvements based on AWS best practices.

The analysis examines your bot's configuration, including intents, utterances, slots, and conversation flows, to provide actionable recommendations for optimization.

## Request Syntax
<a name="API_StartBotAnalyzer_RequestSyntax"></a>

```
POST /bots/{{botId}}/botanalyzer/ HTTP/1.1
Content-type: application/json

{
   "analysisScope": "{{string}}",
   "botVersion": "{{string}}",
   "localeId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartBotAnalyzer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_StartBotAnalyzer_RequestSyntax) **   <a name="lexv2-StartBotAnalyzer-request-uri-botId"></a>
The unique identifier of the bot to analyze.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_StartBotAnalyzer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisScope](#API_StartBotAnalyzer_RequestSyntax) **   <a name="lexv2-StartBotAnalyzer-request-analysisScope"></a>
The scope of analysis to perform. Currently only `BotLocale` scope is supported.
Valid Values: `BotLocale`
Type: String
Valid Values: `BotLocale`
Required: Yes

 ** [botVersion](#API_StartBotAnalyzer_RequestSyntax) **   <a name="lexv2-StartBotAnalyzer-request-botVersion"></a>
The version of the bot to analyze. Defaults to `DRAFT` if not specified.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: No

 ** [localeId](#API_StartBotAnalyzer_RequestSyntax) **   <a name="lexv2-StartBotAnalyzer-request-localeId"></a>
The locale identifier for the bot locale to analyze. Required when `analysisScope` is `BotLocale`.
Type: String
Required: No

## Response Syntax
<a name="API_StartBotAnalyzer_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botAnalyzerRequestId": "string",
   "botAnalyzerStatus": "string",
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "localeId": "string"
}
```

## Response Elements
<a name="API_StartBotAnalyzer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botAnalyzerRequestId](#API_StartBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StartBotAnalyzer-response-botAnalyzerRequestId"></a>
A unique identifier for this analysis request. Use this identifier to check the status and retrieve results.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [botAnalyzerStatus](#API_StartBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StartBotAnalyzer-response-botAnalyzerStatus"></a>
The current status of the analysis. The initial status is `Processing`.
Valid Values: `Processing | Available | Failed | Stopping | Stopped`
Type: String
Valid Values: `Processing | Available | Failed | Stopping | Stopped`

 ** [botId](#API_StartBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StartBotAnalyzer-response-botId"></a>
The unique identifier of the bot being analyzed.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_StartBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StartBotAnalyzer-response-botVersion"></a>
The version of the bot being analyzed.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_StartBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StartBotAnalyzer-response-creationDateTime"></a>
The date and time when the analysis was initiated.
Type: Timestamp

 ** [localeId](#API_StartBotAnalyzer_ResponseSyntax) **   <a name="lexv2-StartBotAnalyzer-response-localeId"></a>
The locale identifier of the bot locale being analyzed.
Type: String

## Errors
<a name="API_StartBotAnalyzer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

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
<a name="API_StartBotAnalyzer_Examples"></a>

### Example request
<a name="API_StartBotAnalyzer_Example_1"></a>

This example illustrates one usage of StartBotAnalyzer.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/<BotId>/botanalyzer/

Payload:
{
    "analysisScope": "BotLocale",
    "botId": "<BotId>",
    "localeId": "en_US",
    "botVersion": "DRAFT"
}
```

### Example response
<a name="API_StartBotAnalyzer_Example_2"></a>

This example illustrates one usage of StartBotAnalyzer.

```
{
    "botId": "<BotId>",
    "botVersion": "DRAFT",
    "localeId": "en_US",
    "botAnalyzerStatus": "Processing",
    "creationDateTime": 1729570423.948,
    "botAnalyzerRequestId": "<RequestId>"
}
```

## See Also
<a name="API_StartBotAnalyzer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StartBotAnalyzer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StartBotAnalyzer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
