---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_SearchFixtures.html
---

# SearchFixtures
<a name="API_SearchFixtures"></a>

Searches for the fixtures (sports events, such as a specific basketball game) that are available for a sport in a date window. Each fixture in the response includes a fixtureId that you specify in the clipping output of a feed, so that Elemental Inference maps the event data for that fixture onto the clipping metadata. This operation is paginated: if there are more fixtures than fit in one page, the response includes a nextToken that you pass in a subsequent request.

## Request Syntax
<a name="API_SearchFixtures_RequestSyntax"></a>

```
POST /v1/fixtures HTTP/1.1
Content-type: application/json

{
   "endDate": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sport": "{{string}}",
   "startDate": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchFixtures_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchFixtures_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endDate](#API_SearchFixtures_RequestSyntax) **   <a name="elementalinference-SearchFixtures-request-endDate"></a>
The last day of the search window, in UTC. The search includes fixtures that are scheduled on this day. Specify the date in ISO 8601 format, as `YYYY-MM-DD`.
If you omit this parameter, Elemental Inference searches only the day that you specified in startDate. The window from startDate through endDate must not exceed seven days.
Type: String
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** [filters](#API_SearchFixtures_RequestSyntax) **   <a name="elementalinference-SearchFixtures-request-filters"></a>
An array of filters that narrow the results. Each filter applies to one dimension of a fixture, such as the competitor. You can specify up to 10 filters.
A fixture must satisfy every filter in the array in order to appear in the results. Within one filter, a fixture must match at least one of the values.
Type: Array of [SearchFilter](API_SearchFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_SearchFixtures_RequestSyntax) **   <a name="elementalinference-SearchFixtures-request-maxResults"></a>
The maximum number of fixtures to return for each API request.
The service might return fewer fixtures than the maxResults value. When more fixtures match the search, the response also includes a nextToken value that you can use to fetch the next batch of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_SearchFixtures_RequestSyntax) **   <a name="elementalinference-SearchFixtures-request-nextToken"></a>
The token that identifies the batch of results that you want to see.
For example, you submit a SearchFixtures request with maxResults set at 5. The service returns the first batch of results (up to 5) and a nextToken value. To see the next batch of results, you submit the SearchFixtures request a second time, with the same search criteria, and specify the nextToken value.
Type: String
Required: No

 ** [sport](#API_SearchFixtures_RequestSyntax) **   <a name="elementalinference-SearchFixtures-request-sport"></a>
The sport to search for fixtures. Valid values: basketball (search for basketball fixtures), american-football (search for american-football fixtures).
Type: String
Valid Values: `basketball | american-football`
Required: Yes

 ** [startDate](#API_SearchFixtures_RequestSyntax) **   <a name="elementalinference-SearchFixtures-request-startDate"></a>
The first day of the search window, in UTC. The search includes fixtures that are scheduled on this day.
Specify the date in ISO 8601 format, as `YYYY-MM-DD`. For example, 2026-03-14.
Type: String
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

## Response Syntax
<a name="API_SearchFixtures_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fixtures": [
      {
         "competitors": [
            {
               "isHome": boolean,
               "name": "string"
            }
         ],
         "fixtureGroup": "string",
         "fixtureId": "string",
         "name": "string",
         "scheduledStart": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_SearchFixtures_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fixtures](#API_SearchFixtures_ResponseSyntax) **   <a name="elementalinference-SearchFixtures-response-fixtures"></a>
An array of FixtureSummary objects, one for each fixture that matches the search. The array is empty if no fixtures match.
Type: Array of [FixtureSummary](API_FixtureSummary.md) objects

 ** [nextToken](#API_SearchFixtures_ResponseSyntax) **   <a name="elementalinference-SearchFixtures-response-nextToken"></a>
The token that identifies the next batch of results. To see the next batch, submit the SearchFixtures request again, with the same search criteria, and specify this value in nextToken.
This parameter is absent when there are no more results to return.
Type: String

## Errors
<a name="API_SearchFixtures_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** GatewayTimedOutException **
The request timed out before the service returned a response. This is a temporary condition. Retry the request. If the problem persists, contact AWS Support.
HTTP Status Code: 504

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is temporarily unable to handle the request. Retry the request. If the problem persists, contact AWS Support.
HTTP Status Code: 503

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_SearchFixtures_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/SearchFixtures)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/SearchFixtures)
