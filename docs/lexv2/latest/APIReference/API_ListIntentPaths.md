---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListIntentPaths.html
---

# ListIntentPaths
<a name="API_ListIntentPaths"></a>

Retrieves summary statistics for a path of intents that users take over sessions with your bot. The following fields are required:
+  `startDateTime` and `endDateTime` – Define a time range for which you want to retrieve results.
+  `intentPath` – Define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the `intentPath` field with `/BookCar/BookHotel` to see details about how many times users invoked the `BookCar` and `BookHotel` intents in that order.

Use the optional `filters` field to filter the results.

## Request Syntax
<a name="API_ListIntentPaths_RequestSyntax"></a>

```
POST /bots/{{botId}}/analytics/intentpaths HTTP/1.1
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
   "intentPath": "{{string}}",
   "startDateTime": {{number}}
}
```

## URI Request Parameters
<a name="API_ListIntentPaths_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_ListIntentPaths_RequestSyntax) **   <a name="lexv2-ListIntentPaths-request-uri-botId"></a>
The identifier for the bot for which you want to retrieve intent path metrics.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_ListIntentPaths_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endDateTime](#API_ListIntentPaths_RequestSyntax) **   <a name="lexv2-ListIntentPaths-request-endDateTime"></a>
The date and time that marks the end of the range of time for which you want to see intent path metrics.
Type: Timestamp
Required: Yes

 ** [filters](#API_ListIntentPaths_RequestSyntax) **   <a name="lexv2-ListIntentPaths-request-filters"></a>
A list of objects, each describes a condition by which you want to filter the results.
Type: Array of [AnalyticsPathFilter](API_AnalyticsPathFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [intentPath](#API_ListIntentPaths_RequestSyntax) **   <a name="lexv2-ListIntentPaths-request-intentPath"></a>
The intent path for which you want to retrieve metrics. Use a forward slash to separate intents in the path. For example:
+ /BookCar
+ /BookCar/BookHotel
+ /BookHotel/BookCar
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [startDateTime](#API_ListIntentPaths_RequestSyntax) **   <a name="lexv2-ListIntentPaths-request-startDateTime"></a>
The date and time that marks the beginning of the range of time for which you want to see intent path metrics.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_ListIntentPaths_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nodeSummaries": [
      {
         "intentCount": number,
         "intentLevel": number,
         "intentName": "string",
         "intentPath": "string",
         "nodeType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListIntentPaths_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nodeSummaries](#API_ListIntentPaths_ResponseSyntax) **   <a name="lexv2-ListIntentPaths-response-nodeSummaries"></a>
A list of objects, each of which contains information about a node in the intent path for which you requested metrics.
Type: Array of [AnalyticsIntentNodeSummary](API_AnalyticsIntentNodeSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_ListIntentPaths_Errors"></a>

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
<a name="API_ListIntentPaths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/ListIntentPaths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ListIntentPaths)
