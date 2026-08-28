---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotAnalyzerHistory.html
---

# ListBotAnalyzerHistory
<a name="API_ListBotAnalyzerHistory"></a>

Retrieves a list of historical bot analysis executions for a specific bot. You can filter the results by locale and bot version.

The history includes all analysis executions regardless of their status, allowing you to track past analyses and their outcomes.

## Request Syntax
<a name="API_ListBotAnalyzerHistory_RequestSyntax"></a>

```
POST /bots/{{botId}}/botanalyzer/history/ HTTP/1.1
Content-type: application/json

{
   "botVersion": "{{string}}",
   "localeId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListBotAnalyzerHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListBotAnalyzerHistory_RequestSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-request-uri-botId"></a>
The unique identifier of the bot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListBotAnalyzerHistory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [botVersion](#API_ListBotAnalyzerHistory_RequestSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-request-botVersion"></a>
The bot version to filter the history. If not specified, defaults to `DRAFT`.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: No

 ** [localeId](#API_ListBotAnalyzerHistory_RequestSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-request-localeId"></a>
The locale identifier to filter the history. If not specified, returns history for all locales.
Type: String
Required: No

 ** [maxResults](#API_ListBotAnalyzerHistory_RequestSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-request-maxResults"></a>
The maximum number of history entries to return in the response. The default is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListBotAnalyzerHistory_RequestSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-request-nextToken"></a>
If the response from a previous request was truncated, the `nextToken` value is used to retrieve the next page of history entries.
Type: String
Required: No

## Response Syntax
<a name="API_ListBotAnalyzerHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botAnalyzerHistoryList": [
      {
         "botAnalyzerRequestId": "string",
         "botAnalyzerStatus": "string",
         "creationDateTime": number
      }
   ],
   "botId": "string",
   "botVersion": "string",
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBotAnalyzerHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botAnalyzerHistoryList](#API_ListBotAnalyzerHistory_ResponseSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-response-botAnalyzerHistoryList"></a>
A list of historical analysis executions, ordered by creation date with the most recent first.
Type: Array of [BotAnalyzerHistorySummary](API_BotAnalyzerHistorySummary.md) objects

 ** [botId](#API_ListBotAnalyzerHistory_ResponseSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-response-botId"></a>
The unique identifier of the bot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_ListBotAnalyzerHistory_ResponseSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-response-botVersion"></a>
The bot version used to filter the history.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [localeId](#API_ListBotAnalyzerHistory_ResponseSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-response-localeId"></a>
The locale identifier used to filter the history.
Type: String

 ** [nextToken](#API_ListBotAnalyzerHistory_ResponseSyntax) **   <a name="lexv2-ListBotAnalyzerHistory-response-nextToken"></a>
If the response is truncated, this token can be used in a subsequent request to retrieve the next page of history entries.
Type: String

## Errors
<a name="API_ListBotAnalyzerHistory_Errors"></a>

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
<a name="API_ListBotAnalyzerHistory_Examples"></a>

### Example request
<a name="API_ListBotAnalyzerHistory_Example_1"></a>

This example illustrates one usage of ListBotAnalyzerHistory.

```
POST https://models-v2-lex.us-east-1.amazonaws.com/bots/<BotId>/botanalyzer/history/

Payload:
{
    "localeId": "en_US",
    "botVersion": "DRAFT"
}
```

### Example response
<a name="API_ListBotAnalyzerHistory_Example_2"></a>

This example illustrates one usage of ListBotAnalyzerHistory.

```
{
    "botId": "<BotId>",
    "localeId": "en_US",
    "botVersion": "DRAFT",
    "botAnalyzerHistoryList": [
        {
            "botAnalyzerStatus": "Available",
            "creationDateTime": 1729570423.948,
            "botAnalyzerRequestId": "<RequestId1>"
        },
        {
            "botAnalyzerStatus": "Failed",
            "creationDateTime": 1729484530.123,
            "botAnalyzerRequestId": "<RequestId2>"
        }
    ],
    "nextToken": "<NextToken>"
}
```

## See Also
<a name="API_ListBotAnalyzerHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListBotAnalyzerHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
