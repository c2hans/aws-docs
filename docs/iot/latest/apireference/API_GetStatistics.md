---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetStatistics.html
---

# GetStatistics
<a name="API_GetStatistics"></a>

Returns the count, average, sum, minimum, maximum, sum of squares, variance, and standard deviation for the specified aggregated field. If the aggregation field is of type `String`, only the count statistic is returned.

Requires permission to access the [GetStatistics](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetStatistics_RequestSyntax"></a>

```
POST /indices/statistics HTTP/1.1
Content-type: application/json

{
   "aggregationField": "{{string}}",
   "indexName": "{{string}}",
   "queryString": "{{string}}",
   "queryVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationField](#API_GetStatistics_RequestSyntax) **   <a name="iot-GetStatistics-request-aggregationField"></a>
The aggregation field name.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [indexName](#API_GetStatistics_RequestSyntax) **   <a name="iot-GetStatistics-request-indexName"></a>
The name of the index to search. The default value is `AWS_Things`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [queryString](#API_GetStatistics_RequestSyntax) **   <a name="iot-GetStatistics-request-queryString"></a>
The query used to search. You can specify "\*" for the query string to get the count of all indexed things in your AWS account.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [queryVersion](#API_GetStatistics_RequestSyntax) **   <a name="iot-GetStatistics-request-queryVersion"></a>
The version of the query used to search.
Type: String
Required: No

## Response Syntax
<a name="API_GetStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "statistics": {
      "average": number,
      "count": number,
      "maximum": number,
      "minimum": number,
      "stdDeviation": number,
      "sum": number,
      "sumOfSquares": number,
      "variance": number
   }
}
```

## Response Elements
<a name="API_GetStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [statistics](#API_GetStatistics_ResponseSyntax) **   <a name="iot-GetStatistics-response-statistics"></a>
The statistics returned by the Fleet Indexing service based on the query and aggregation field.
Type: [Statistics](API_Statistics.md) object

## Errors
<a name="API_GetStatistics_Errors"></a>

 ** IndexNotReadyException **
The index is not ready.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidAggregationException **
The aggregation is invalid.
HTTP Status Code: 400

 ** InvalidQueryException **
The query is invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_GetStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetStatistics)
