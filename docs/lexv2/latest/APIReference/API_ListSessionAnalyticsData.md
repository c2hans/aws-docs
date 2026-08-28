---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListSessionAnalyticsData.html
---

# ListSessionAnalyticsData
<a name="API_ListSessionAnalyticsData"></a>

Retrieves a list of metadata for individual user sessions with your bot. The `startDateTime` and `endDateTime` fields are required. These fields define a time range for which you want to retrieve results. Of the optional fields, you can organize the results in the following ways:
+ Use the `filters` field to filter the results and the `sortBy` field to specify the values by which to sort the results.
+ Use the `maxResults` field to limit the number of results to return in a single response and the `nextToken` field to return the next batch of results if the response does not return the full set of results.

## Request Syntax
<a name="API_ListSessionAnalyticsData_RequestSyntax"></a>

```
POST /bots/{{botId}}/analytics/sessions HTTP/1.1
Content-type: application/json

{
   "endDateTime": {{number}},
   "filters": [
      {
         "name": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": {
      "name": "{{string}}",
      "order": "{{string}}"
   },
   "startDateTime": {{number}}
}
```

## URI Request Parameters
<a name="API_ListSessionAnalyticsData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-uri-botId"></a>
The identifier for the bot for which you want to retrieve session analytics.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListSessionAnalyticsData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endDateTime](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-endDateTime"></a>
The date and time that marks the end of the range of time for which you want to see session analytics.
Type: Timestamp
Required: Yes

 ** [filters](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-filters"></a>
A list of objects, each of which describes a condition by which you want to filter the results.
Type: Array of [AnalyticsSessionFilter](API_AnalyticsSessionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-maxResults"></a>
The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-nextToken"></a>
If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.
Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.
Type: String
Required: No

 ** [sortBy](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-sortBy"></a>
An object specifying the measure and method by which to sort the session analytics data.
Type: [SessionDataSortBy](API_SessionDataSortBy.md) object
Required: No

 ** [startDateTime](#API_ListSessionAnalyticsData_RequestSyntax) **   <a name="lexv2-ListSessionAnalyticsData-request-startDateTime"></a>
The date and time that marks the beginning of the range of time for which you want to see session analytics.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_ListSessionAnalyticsData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "nextToken": "string",
   "sessions": [
      {
         "botAliasId": "string",
         "botVersion": "string",
         "channel": "string",
         "conversationDurationSeconds": number,
         "conversationEndState": "string",
         "conversationEndTime": number,
         "conversationStartTime": number,
         "invokedIntentSamples": [
            {
               "intentName": "string"
            }
         ],
         "localeId": "string",
         "mode": "string",
         "numberOfTurns": number,
         "originatingRequestId": "string",
         "sessionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSessionAnalyticsData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListSessionAnalyticsData_ResponseSyntax) **   <a name="lexv2-ListSessionAnalyticsData-response-botId"></a>
The unique identifier of the bot that the sessions belong to.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [nextToken](#API_ListSessionAnalyticsData_ResponseSyntax) **   <a name="lexv2-ListSessionAnalyticsData-response-nextToken"></a>
If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.
Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.
Type: String

 ** [sessions](#API_ListSessionAnalyticsData_ResponseSyntax) **   <a name="lexv2-ListSessionAnalyticsData-response-sessions"></a>
A list of objects, each of which contains information about a session with the bot.
Type: Array of [SessionSpecification](API_SessionSpecification.md) objects

## Errors
<a name="API_ListSessionAnalyticsData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListSessionAnalyticsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListSessionAnalyticsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListSessionAnalyticsData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
