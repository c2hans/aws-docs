---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListUtteranceMetrics.html
---

# ListUtteranceMetrics
<a name="API_ListUtteranceMetrics"></a>

**Note**
To use this API operation, your IAM role must have permissions to perform the [ListAggregatedUtterances](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html) operation, which provides access to utterance-related analytics. See [Viewing utterance statistics](https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html) for the IAM policy to apply to the IAM role.

Retrieves summary metrics for the utterances in your bot. The following fields are required:
+  `metrics` – A list of [AnalyticsUtteranceMetric](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsUtteranceMetric.html) objects. In each object, use the `name` field to specify the metric to calculate, the `statistic` field to specify whether to calculate the `Sum`, `Average`, or `Max` number, and the `order` field to specify whether to sort the results in `Ascending` or `Descending` order.
+  `startDateTime` and `endDateTime` – Define a time range for which you want to retrieve results.

Of the optional fields, you can organize the results in the following ways:
+ Use the `filters` field to filter the results, the `groupBy` field to specify categories by which to group the results, and the `binBy` field to specify time intervals by which to group the results.
+ Use the `maxResults` field to limit the number of results to return in a single response and the `nextToken` field to return the next batch of results if the response does not return the full set of results.

Note that an `order` field exists in both `binBy` and `metrics`. Currently, you can specify it in either field, but not in both.

## Request Syntax
<a name="API_ListUtteranceMetrics_RequestSyntax"></a>

```
POST /bots/{{botId}}/analytics/utterancemetrics HTTP/1.1
Content-type: application/json

{
   "attributes": [
      {
         "name": "{{string}}"
      }
   ],
   "binBy": [
      {
         "interval": "{{string}}",
         "name": "{{string}}",
         "order": "{{string}}"
      }
   ],
   "endDateTime": {{number}},
   "filters": [
      {
         "name": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "groupBy": [
      {
         "name": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "metrics": [
      {
         "name": "{{string}}",
         "order": "{{string}}",
         "statistic": "{{string}}"
      }
   ],
   "nextToken": "{{string}}",
   "startDateTime": {{number}}
}
```

## URI Request Parameters
<a name="API_ListUtteranceMetrics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-uri-botId"></a>
The identifier for the bot for which you want to retrieve utterance metrics.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListUtteranceMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-attributes"></a>
A list containing attributes related to the utterance that you want the response to return. The following attributes are possible:
+  `LastUsedIntent` – The last used intent at the time of the utterance.
Type: Array of [AnalyticsUtteranceAttribute](API_AnalyticsUtteranceAttribute.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [binBy](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-binBy"></a>
A list of objects, each of which contains specifications for organizing the results by time.
Type: Array of [AnalyticsBinBySpecification](API_AnalyticsBinBySpecification.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [endDateTime](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-endDateTime"></a>
The date and time that marks the end of the range of time for which you want to see utterance metrics.
Type: Timestamp
Required: Yes

 ** [filters](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-filters"></a>
A list of objects, each of which describes a condition by which you want to filter the results.
Type: Array of [AnalyticsUtteranceFilter](API_AnalyticsUtteranceFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 9 items.
Required: No

 ** [groupBy](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-groupBy"></a>
A list of objects, each of which specifies how to group the results. You can group by the following criteria:
+  `UtteranceText` – The transcription of the utterance.
+  `UtteranceState` – The state of the utterance. The possible states are detailed in [Key definitions](https://docs.aws.amazon.com/analytics-key-definitions-utterances) in the user guide.
Type: Array of [AnalyticsUtteranceGroupBySpecification](API_AnalyticsUtteranceGroupBySpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [maxResults](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-maxResults"></a>
The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [metrics](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-metrics"></a>
A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.
Type: Array of [AnalyticsUtteranceMetric](API_AnalyticsUtteranceMetric.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: Yes

 ** [nextToken](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-nextToken"></a>
If the response from the ListUtteranceMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.
Use the returned token in the nextToken parameter of a ListUtteranceMetrics request to return the next page of results. For a complete set of results, call the ListUtteranceMetrics operation until the nextToken returned in the response is null.
Type: String
Required: No

 ** [startDateTime](#API_ListUtteranceMetrics_RequestSyntax) **   <a name="lexv2-ListUtteranceMetrics-request-startDateTime"></a>
The date and time that marks the beginning of the range of time for which you want to see utterance metrics.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_ListUtteranceMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "nextToken": "string",
   "results": [
      {
         "attributeResults": [
            {
               "lastUsedIntent": "string"
            }
         ],
         "binKeys": [
            {
               "name": "string",
               "value": number
            }
         ],
         "groupByKeys": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "metricsResults": [
            {
               "name": "string",
               "statistic": "string",
               "value": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListUtteranceMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_ListUtteranceMetrics_ResponseSyntax) **   <a name="lexv2-ListUtteranceMetrics-response-botId"></a>
The identifier for the bot for which you retrieved utterance metrics.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [nextToken](#API_ListUtteranceMetrics_ResponseSyntax) **   <a name="lexv2-ListUtteranceMetrics-response-nextToken"></a>
If the response from the ListUtteranceMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.
Use the returned token in the nextToken parameter of a ListUtteranceMetrics request to return the next page of results. For a complete set of results, call the ListUtteranceMetrics operation until the nextToken returned in the response is null.
Type: String

 ** [results](#API_ListUtteranceMetrics_ResponseSyntax) **   <a name="lexv2-ListUtteranceMetrics-response-results"></a>
The results for the utterance metrics.
Type: Array of [AnalyticsUtteranceResult](API_AnalyticsUtteranceResult.md) objects

## Errors
<a name="API_ListUtteranceMetrics_Errors"></a>

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
<a name="API_ListUtteranceMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListUtteranceMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListUtteranceMetrics)
