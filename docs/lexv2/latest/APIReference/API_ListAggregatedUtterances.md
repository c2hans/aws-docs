---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html
---

# ListAggregatedUtterances
<a name="API_ListAggregatedUtterances"></a>

Provides a list of utterances that users have sent to the bot.

Utterances are aggregated by the text of the utterance. For example, all instances where customers used the phrase "I want to order pizza" are aggregated into the same line in the response.

You can see both detected utterances and missed utterances. A detected utterance is where the bot properly recognized the utterance and activated the associated intent. A missed utterance was not recognized by the bot and didn't activate an intent.

Utterances can be aggregated for a bot alias or for a bot version, but not both at the same time.

Utterances statistics are not generated under the following conditions:
+ The `childDirected` field was set to true when the bot was created.
+ You are using slot obfuscation with one or more slots.
+ You opted out of participating in improving Amazon Lex.

## Request Syntax
<a name="API_ListAggregatedUtterances_RequestSyntax"></a>

```
POST /bots/{{botId}}/aggregatedutterances/ HTTP/1.1
Content-type: application/json

{
   "aggregationDuration": {
      "relativeAggregationDuration": {
         "timeDimension": "{{string}}",
         "timeValue": {{number}}
      }
   },
   "botAliasId": "{{string}}",
   "botVersion": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "localeId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": {
      "attribute": "{{string}}",
      "order": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListAggregatedUtterances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-uri-botId"></a>
The unique identifier of the bot associated with this request.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListAggregatedUtterances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationDuration](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-aggregationDuration"></a>
The time window for aggregating the utterance information. You can specify a time between one hour and two weeks.
Type: [UtteranceAggregationDuration](API_UtteranceAggregationDuration.md) object
Required: Yes

 ** [botAliasId](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-botAliasId"></a>
The identifier of the bot alias associated with this request. If you specify the bot alias, you can't specify the bot version.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: No

 ** [botVersion](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-botVersion"></a>
The identifier of the bot version associated with this request. If you specify the bot version, you can't specify the bot alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: No

 ** [filters](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-filters"></a>
Provides the specification of a filter used to limit the utterances in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.
Type: Array of [AggregatedUtterancesFilter](API_AggregatedUtterancesFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [localeId](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-localeId"></a>
The identifier of the language and locale where the utterances were collected. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Type: String
Required: Yes

 ** [maxResults](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-maxResults"></a>
The maximum number of utterances to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. If you don't specify the `maxResults` parameter, 1,000 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-nextToken"></a>
If the response from the `ListAggregatedUtterances` operation contains more results that specified in the `maxResults` parameter, a token is returned in the response. Use that token in the `nextToken` parameter to return the next page of results.
Type: String
Required: No

 ** [sortBy](#API_ListAggregatedUtterances_RequestSyntax) **   <a name="lexv2-ListAggregatedUtterances-request-sortBy"></a>
Specifies sorting parameters for the list of utterances. You can sort by the hit count, the missed count, or the number of distinct sessions the utterance appeared in.
Type: [AggregatedUtterancesSortBy](API_AggregatedUtterancesSortBy.md) object
Required: No

## Response Syntax
<a name="API_ListAggregatedUtterances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregatedUtterancesSummaries": [
      {
         "containsDataFromDeletedResources": boolean,
         "hitCount": number,
         "missedCount": number,
         "utterance": "string",
         "utteranceFirstRecordedInAggregationDuration": number,
         "utteranceLastRecordedInAggregationDuration": number
      }
   ],
   "aggregationDuration": {
      "relativeAggregationDuration": {
         "timeDimension": "string",
         "timeValue": number
      }
   },
   "aggregationLastRefreshedDateTime": number,
   "aggregationWindowEndTime": number,
   "aggregationWindowStartTime": number,
   "botAliasId": "string",
   "botId": "string",
   "botVersion": "string",
   "localeId": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAggregatedUtterances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregatedUtterancesSummaries](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-aggregatedUtterancesSummaries"></a>
Summaries of the aggregated utterance data. Each response contains information about the number of times that the utterance was seen during the time period, whether it was detected or missed, and when it was seen during the time period.
Type: Array of [AggregatedUtterancesSummary](API_AggregatedUtterancesSummary.md) objects

 ** [aggregationDuration](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-aggregationDuration"></a>
The time period used to aggregate the utterance data.
Type: [UtteranceAggregationDuration](API_UtteranceAggregationDuration.md) object

 ** [aggregationLastRefreshedDateTime](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-aggregationLastRefreshedDateTime"></a>
The last date and time that the aggregated data was collected. The time period depends on the length of the aggregation window.
+  **Hours** - for 1 hour time window, every half hour; otherwise every hour.
+  **Days** - every 6 hours
+  **Weeks** - for a one week time window, every 12 hours; otherwise, every day
Type: Timestamp

 ** [aggregationWindowEndTime](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-aggregationWindowEndTime"></a>
The date and time that the aggregation window ends. Only data collected between the start time and the end time are returned in the results.
Type: Timestamp

 ** [aggregationWindowStartTime](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-aggregationWindowStartTime"></a>
The date and time that the aggregation window begins. Only data collected after this time is returned in the results.
Type: Timestamp

 ** [botAliasId](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-botAliasId"></a>
The identifier of the bot alias that contains the utterances. If you specified the bot version, the bot alias ID isn't returned.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`

 ** [botId](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-botId"></a>
The identifier of the bot that contains the utterances.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-botVersion"></a>
The identifier of the bot version that contains the utterances. If you specified the bot alias, the bot version isn't returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [localeId](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-localeId"></a>
The identifier of the language and locale that the utterances are in.
Type: String

 ** [nextToken](#API_ListAggregatedUtterances_ResponseSyntax) **   <a name="lexv2-ListAggregatedUtterances-response-nextToken"></a>
A token that indicates whether there are more results to return in a response to the `ListAggregatedUtterances` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListAggregatedUtterances` operation request to get the next page of results.
Type: String

## Errors
<a name="API_ListAggregatedUtterances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListAggregatedUtterances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListAggregatedUtterances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListAggregatedUtterances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
