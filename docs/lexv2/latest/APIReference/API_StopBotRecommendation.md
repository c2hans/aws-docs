---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StopBotRecommendation.html
---

# StopBotRecommendation
<a name="API_StopBotRecommendation"></a>

Stop an already running Bot Recommendation request.

## Request Syntax
<a name="API_StopBotRecommendation_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/botrecommendations/{{botRecommendationId}}/stopbotrecommendation HTTP/1.1
```

## URI Request Parameters
<a name="API_StopBotRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_StopBotRecommendation_RequestSyntax) **   <a name="lexv2-StopBotRecommendation-request-uri-botId"></a>
The unique identifier of the bot containing the bot recommendation to be stopped.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botRecommendationId](#API_StopBotRecommendation_RequestSyntax) **   <a name="lexv2-StopBotRecommendation-request-uri-botRecommendationId"></a>
The unique identifier of the bot recommendation to be stopped.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_StopBotRecommendation_RequestSyntax) **   <a name="lexv2-StopBotRecommendation-request-uri-botVersion"></a>
The version of the bot containing the bot recommendation.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_StopBotRecommendation_RequestSyntax) **   <a name="lexv2-StopBotRecommendation-request-uri-localeId"></a>
The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)
Required: Yes

## Request Body
<a name="API_StopBotRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopBotRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "botId": "string",
   "botRecommendationId": "string",
   "botRecommendationStatus": "string",
   "botVersion": "string",
   "localeId": "string"
}
```

## Response Elements
<a name="API_StopBotRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_StopBotRecommendation_ResponseSyntax) **   <a name="lexv2-StopBotRecommendation-response-botId"></a>
The unique identifier of the bot containing the bot recommendation that is being stopped.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botRecommendationId](#API_StopBotRecommendation_ResponseSyntax) **   <a name="lexv2-StopBotRecommendation-response-botRecommendationId"></a>
The unique identifier of the bot recommendation that is being stopped.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botRecommendationStatus](#API_StopBotRecommendation_ResponseSyntax) **   <a name="lexv2-StopBotRecommendation-response-botRecommendationStatus"></a>
The status of the bot recommendation. If the status is Failed, then the reasons for the failure are listed in the failureReasons field.
Type: String
Valid Values: `Processing | Deleting | Deleted | Downloading | Updating | Available | Failed | Stopping | Stopped`

 ** [botVersion](#API_StopBotRecommendation_ResponseSyntax) **   <a name="lexv2-StopBotRecommendation-response-botVersion"></a>
The version of the bot containing the recommendation that is being stopped.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [localeId](#API_StopBotRecommendation_ResponseSyntax) **   <a name="lexv2-StopBotRecommendation-response-localeId"></a>
The identifier of the language and locale of the bot response to stop. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)
Type: String

## Errors
<a name="API_StopBotRecommendation_Errors"></a>

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

## See Also
<a name="API_StopBotRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StopBotRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StopBotRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
