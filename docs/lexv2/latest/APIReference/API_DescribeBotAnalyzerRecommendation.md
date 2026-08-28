---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotAnalyzerRecommendation.html
---

# DescribeBotAnalyzerRecommendation
<a name="API_DescribeBotAnalyzerRecommendation"></a>

Retrieves the analysis results and recommendations for bot optimization. The analysis must be in `Available` status before recommendations can be retrieved.

Recommendations are returned with pagination support. Each recommendation includes the issue location, priority level, detailed description, and proposed fix.

## Request Syntax
<a name="API_DescribeBotAnalyzerRecommendation_RequestSyntax"></a>

```
POST /bots/{{botId}}/botanalyzer/describe/{{botAnalyzerRequestId}}/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeBotAnalyzerRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botAnalyzerRequestId](#API_DescribeBotAnalyzerRecommendation_RequestSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-request-uri-botAnalyzerRequestId"></a>
The unique identifier of the analysis request.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [botId](#API_DescribeBotAnalyzerRecommendation_RequestSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-request-uri-botId"></a>
The unique identifier of the bot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeBotAnalyzerRecommendation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeBotAnalyzerRecommendation_RequestSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-request-maxResults"></a>
The maximum number of recommendations to return in the response. The default is 5.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeBotAnalyzerRecommendation_RequestSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-request-nextToken"></a>
If the response from a previous request was truncated, the `nextToken` value is used to retrieve the next page of recommendations.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeBotAnalyzerRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botAnalyzerRecommendationList": [
      {
         "issueDescription": "string",
         "issueLocation": {
            "botLocale": "string",
            "intentId": "string",
            "slotId": "string"
         },
         "priority": "string",
         "proposedFix": "string"
      }
   ],
   "botAnalyzerStatus": "string",
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeBotAnalyzerRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botAnalyzerRecommendationList](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-botAnalyzerRecommendationList"></a>
A list of recommendations for optimizing your bot configuration. Each recommendation includes the issue location, priority, description, and proposed fix.
Type: Array of [BotAnalyzerRecommendation](API_BotAnalyzerRecommendation.md) objects

 ** [botAnalyzerStatus](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-botAnalyzerStatus"></a>
The current status of the analysis.
Valid Values: `Processing | Available | Failed | Stopping | Stopped`
Type: String
Valid Values: `Processing | Available | Failed | Stopping | Stopped`

 ** [botId](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-botId"></a>
The unique identifier of the bot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-botVersion"></a>
The version of the bot that was analyzed.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-creationDateTime"></a>
The date and time when the analysis was initiated.
Type: Timestamp

 ** [localeId](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-localeId"></a>
The locale identifier of the bot locale that was analyzed.
Type: String

 ** [nextToken](#API_DescribeBotAnalyzerRecommendation_ResponseSyntax) **   <a name="lexv2-DescribeBotAnalyzerRecommendation-response-nextToken"></a>
If the response is truncated, this token can be used in a subsequent request to retrieve the next page of recommendations.
Type: String

## Errors
<a name="API_DescribeBotAnalyzerRecommendation_Errors"></a>

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
<a name="API_DescribeBotAnalyzerRecommendation_Examples"></a>

### Example request
<a name="API_DescribeBotAnalyzerRecommendation_Example_1"></a>

This example illustrates one usage of DescribeBotAnalyzerRecommendation.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/<BotId>/botanalyzer/describe/<RequestId>/

Payload:
{
    "nextToken": ""
}
```

### Example response
<a name="API_DescribeBotAnalyzerRecommendation_Example_2"></a>

This example illustrates one usage of DescribeBotAnalyzerRecommendation.

```
{
    "botId": "<BotId>",
    "localeId": "en_US",
    "botVersion": "DRAFT",
    "creationDateTime": 1729570423.948,
    "botAnalyzerStatus": "Available",
    "botAnalyzerRecommendationList": [
        {
            "issueLocation": {
                "botLocale": "en_US",
                "intentId": "BookHotel",
                "slotId": null
            },
            "priority": "High",
            "issueDescription": "Intent 'BookHotel' has overlapping utterances with 'ReserveRoom' intent that may cause routing confusion",
            "proposedFix": "Consider consolidating these intents or making utterances more distinct. For example, use 'book a hotel room' vs 'reserve a conference room'"
        }
    ],
    "nextToken": "<NextToken>"
}
```

## See Also
<a name="API_DescribeBotAnalyzerRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeBotAnalyzerRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
